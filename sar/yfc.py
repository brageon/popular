import numpy as np
import yfinance as yf
import math, statistics
from scipy.stats import norm

data = yf.download("BTC-USD", start="2023-01-01", end="2024-09-28")
prices = data['Close'].tolist()
def forex(*args, type=float):
    for arg in args:
        return round(arg, 2)
def rolex(*args, type=float):
    return tuple(round(arg, 2) for arg in args)

def calculate_std(data):
    mean = sum(data) / len(data)
    squared_differences = [(x - mean) ** 2 for x in data]
    variance = sum(squared_differences) / len(data)
    std = statistics.sqrt(variance)
    return forex(std)

def calculate_rsi(gains, period):
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    rs = avg_gain / avg_loss
    rsi = 100 - 100 / (1 + rs)
    return forex(rsi)
def typical_price(low, high, rsi):
    return low + high + rsi

def calculate_trend(typical_price, volume, rsi):
    trend = math.log(typical_price * volume[0]) * (1 - rsi / 100)
    return forex(trend)
def calculate_ema(price, prev_ema, alpha):
    ema = price * alpha + prev_ema * (1 - alpha)
    return forex(ema)

def mean_gap_size(prices, period):
    gaps = [high - low for high, low in zip(prices[period:], prices[:-period])]
    mean_gap = sum(gaps) / len(gaps)
    return forex(mean_gap)

def calculate_aroon(prices, fain):
    highest_high = max(fain[:])
    lowest_low = min(fain[:])
    sain = int(highest_high - lowest_low)
    aroon_up = (fain.index(highest_high) + 1) / sain * 100
    aroon_down = (fain.index(lowest_low) + 1) / sain * 100
    return rolex(aroon_up, aroon_down)

def calculate_fast_stochastic(prices, period):
    lowest_low = min(prices[-period:])
    highest_high = max(prices[-period:])
    slow_k = [100 * ((price - lowest_low) / (highest_high - lowest_low)) for price in prices[-period:]]
    slow_d = sum(slow_k[-period:]) / period
    return forex(slow_d)

def bollinger(prices, window_size, stdev_multiple):
    sma = sum(prices[-window_size:]) / window_size
    squared_differences = [(price - sma)**2 for price in prices[-window_size:]]
    variance = sum(squared_differences) / (window_size - 1)
    stdev = math.sqrt(variance)
    upper_band = sma + stdev_multiple * stdev
    lower_band = sma - stdev_multiple * stdev
    return rolex(upper_band, lower_band)

def calculate_emv(high, low, volume):
    delta = (high + low) / 2
    easy = (delta * volume) / 100000000
    return forex(easy)

def black_scholes_call(S, K, T, r, sigma):
    d1 = (math.log(S/K) + (r + sigma**2/2)*T) / (sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)
    call_price = S*norm.cdf(d1) - K*math.exp(-r*T)*norm.cdf(d2)
    return forex(call_price)

def calculate_vix(prices, window_size, call_price):
    returns = np.diff(np.log(prices)) * 100
    squared_returns = returns**2
    variance = np.mean(squared_returns[-window_size:])
    vix = np.sqrt(variance * call_price)
    return forex(vix)

def gains():
    gains, losses = [], []
    for i in range(1, len(prices)):
        change = prices[i] - prices[i-1]
        if change > 0:
            gains.append(change)
        elif change < 0:
            losses.append(-change)
    return gains, losses

def calculate_sar(prices, initial_sar, acceleration_factor):
    sar = [initial_sar]
    trend = 1
    for i in range(1, len(prices)):
        if trend == 1:
            if prices[i] < sar[-1]:
                trend = -1
                sar.append(sar[-1])
            else:
                sar.append(sar[-1] + acceleration_factor * (prices[i] - sar[-1]))
        else:
            if prices[i] > sar[-1]:
                trend = 1
                sar.append(sar[-1])
            else:
                sar.append(sar[-1] - acceleration_factor * (sar[-1] - prices[i]))
    return sar

start_price = prices[:-60]
end_price = prices[:-1]
stdev_multiple = 2
window_size = 20
period = len(end_price) - len(start_price)
drain = prices[-period:]
high = max(prices[:])  # 3rd Day
low = min(prices[:])  # 9th Day
volume = data['Volume'].tolist()
alpha = 0.15

gains, losses = gains()
std = calculate_std(prices)
mgs = mean_gap_size(prices, period)
rsi = calculate_rsi(gains, period)
typical_price = typical_price(low, high, rsi)
trend = calculate_trend(typical_price, volume, rsi)
slow_d = calculate_fast_stochastic(prices, period)
bu, lb = bollinger(gains, window_size, stdev_multiple)
aroon_up, aroon_down = calculate_aroon(prices, drain)
emv = calculate_emv(high, low, volume[0])

insar = 0.04 * emv
acceleration_factor = 0.04
sar = calculate_sar(prices, insar, acceleration_factor)
T = 0.25  # Time to expiration (in years)
r = 0.02  # Risk-free interest rate
sigma = 0.2  # Volatility
call_price = black_scholes_call(insar, high, T, r, sigma)
vix = calculate_vix(drain, window_size, call_price) + mgs

print("\nMGS:", mgs)
print("RSI:", rsi)
print("STD:", std)
print("Trend:", trend)
print("Dlow:", slow_d)
print("EMV:", emv)
print("UB:", bu)
print("LB:", lb)
print("AU:", aroon_up)
print("AD:", aroon_down)
print("Call:", call_price)
print("Flux:", vix)  # LV-HM, calm market, big guys
print("Stop:", rolex(sar[-1] + mgs))
print("Sell:", rolex(sar[0] - call_price))
