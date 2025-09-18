import os, sys, time, requests, threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# ---------------- CONFIG ----------------
base_url = "https://api.api-tennis.com/tennis/"
api_key = os.getenv("API_TENNIS_KEY")
event_date = "2025-09-18"
timer_running = True

player_cache = {}
odds_cache = {}

# ---------------- TIMER ----------------
def live_timer():
    start = time.time()
    while timer_running:
        elapsed = time.time() - start
        mins, secs = divmod(int(elapsed), 60)
        sys.stdout.write(f"\rElapsed Time: {mins:02d}:{secs:02d}")
        sys.stdout.flush()
        time.sleep(1)
    print()


# ---------------- API CALLS ----------------
def get_fixtures(date_start=event_date, date_stop=event_date):
    url = f"{base_url}?method=get_fixtures&APIkey={api_key}&date_start={date_start}&date_stop={date_stop}"
    resp = requests.get(url).json()
    return resp.get("result", [])

def fetch_player(player_key):
    if player_key in player_cache:
        return player_cache[player_key]
    url = f"{base_url}?method=get_players&player_key={player_key}&APIkey={api_key}"
    try:
        resp = requests.get(url).json()
        result = resp.get("result", [])
        if result:
            player_cache[player_key] = result[0]
            return result[0]
    except Exception as e:
        print(f"Error fetching player {player_key}: {e}")
    return None

def fetch_odds(event_key):
    if not event_key:
        return {}
    if event_key in odds_cache:
        return odds_cache[event_key]
    url = f"{base_url}?method=get_odds&match_key={event_key}&APIkey={api_key}"
    try:
        resp = requests.get(url).json()
        match_data = resp.get("result", {}).get(str(event_key), {})
        home_away = match_data.get("Home/Away", {})
        odds = {}
        if home_away:
            home_bk = home_away.get("Home", {})
            away_bk = home_away.get("Away", {})
            if home_bk and away_bk:
                first_bk = list(home_bk.keys())[0]
                odds = {"home": home_bk.get(first_bk), "away": away_bk.get(first_bk)}
        odds_cache[event_key] = odds
        return odds
    except Exception as e:
        print(f"Error fetching odds for {event_key}: {e}")
        odds_cache[event_key] = {}
        return {}


# ---------------- CONCURRENT FETCH ----------------
def fetch_players_concurrent(player_keys):
    if not player_keys:
        return
    max_workers = min(32, max(4, len(player_keys)//2))
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(fetch_player, pk): pk for pk in player_keys}
        for f in as_completed(futures):
            pass  # results auto-populate player_cache

def fetch_odds_concurrent(match_keys):
    if not match_keys:
        return
    max_workers = min(32, max(4, len(match_keys)//2))
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(fetch_odds, mk): mk for mk in match_keys}
        for f in as_completed(futures):
            pass  # results auto-populate odds_cache


# ---------------- PROCESSING ----------------
def sum_player_record(player_data):
    wins = losses = 0
    for row in player_data.get("stats", []):
        wins += int(row.get("matches_won", 0) or 0)
        losses += int(row.get("matches_lost", 0) or 0)
    total = wins + losses
    win_rate = (wins / total * 100) if total > 0 else 0
    return {
        "player": player_data.get("player_full_name"),
        "country": player_data.get("player_country"),
        "total_wins": wins,
        "total_losses": losses,
        "win_rate": f"{win_rate:.1f}%" }

def extract_h2h(fixtures, maxim, mino):
    evaluated = []

    # Gather all unique player keys and match keys
    player_keys = set()
    match_keys = set()
    for event in fixtures:
        if event.get("first_player_key"):
            player_keys.add(event["first_player_key"])
        if event.get("second_player_key"):
            player_keys.add(event["second_player_key"])
        if event.get("event_key"):
            match_keys.add(event["event_key"])

    # Fetch all players and odds in parallel
    fetch_players_concurrent(player_keys)
    fetch_odds_concurrent(match_keys)

    for event in fixtures:
        a = player_cache.get(event.get("first_player_key"))
        b = player_cache.get(event.get("second_player_key"))
        c = odds_cache.get(event.get("event_key"), {})
        if not a or not b or not c:
            continue

        waa, war = sum_player_record(a), sum_player_record(b)
        wa, wb = float(waa["win_rate"].replace("%", "")), float(war["win_rate"].replace("%", ""))
        wr_gap = abs(wa - wb)
        if wr_gap < mino or wr_gap > mino+3:
            continue

        evaluated.append({
            "gap": round(wr_gap, 2),
            "tour": event.get("tournament_name"),
            "time": event.get("event_time"),
            "player_a": waa,
            "player_b": war,
            "mate": c })

        if len(evaluated) >= maxim:
            break

    return evaluated


# ---------------- RUN SCRIPT ----------------
if __name__ == "__main__":
    timer_running = True
    t = threading.Thread(target=live_timer)
    t.start()

    d, j = 60, 8
    fixtures = get_fixtures()
    h2h_events = extract_h2h(fixtures, maxim=d, mino=j)
    h2h_events.sort(key=lambda x: x["gap"])
    print(f"\nPrecomputed {len(h2h_events)} ranked matches.")

    for idx, zen in enumerate(h2h_events, 1):
        print(f"\n--- Fixture {idx} ---\n")
        print(f"Tournament: {zen['tour']}")
        print(f"Match Time: {zen['time']}")
        print(f"Delta: {zen['gap']}")
        print(f"Odds: {zen['mate']}")

        print("\nPlayer A:")
        for k, v in zen['player_a'].items():
            print(f"{k}: {v}")

        print("\nPlayer B:")
        for k, v in zen['player_b'].items():
            print(f"{k}: {v}")

    timer_running = False
    t.join()
    print("Script finished.")
