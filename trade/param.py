import numpy as np
import math, statistics
from scipy.stats import norm

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
def calculate_moment(start_price, end_price, period):
    return forex((end_price - start_price) / start_price * period)

def calculate_typical(high, low, close):
    return forex((high + low + close) / 3)
def calculate_rsi(gains, period):
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period
    rs = avg_gain / avg_loss
    rsi = 100 - 100 / (1 + rs)
    return forex(rsi)

def calculate_trend(typical_price, volume, rsi):
    trend = math.log(typical_price * volume) * (1 - rsi / 100)
    return forex(trend)
def calculate_ema(price, prev_ema, alpha):
    ema = price * alpha + prev_ema * (1 - alpha)
    return forex(ema)

def mean_gap_size(prices, period):
    gaps = [high - low for high, low in zip(prices[period:], prices[:-period])]
    mean_gap = sum(gaps) / len(gaps)
    return forex(mean_gap)

def calculate_aroon(prices, period):
    highest_high = max(prices[-period:])
    lowest_low = min(prices[-period:])
    aroon_up = (period - prices.index(highest_high) + 1) / period * 100
    aroon_down = (period - prices.index(lowest_low) + 1) / period * 100
    return rolex(aroon_up, aroon_down)

def calculate_fast_stochastic(prices, period):
    lowest_low = min(prices[-period:])
    highest_high = max(prices[-period:])
    slow_k = [100 * ((price - lowest_low) / (highest_high - lowest_low)) for price in prices[-period:]]
    slow_d = sum(slow_k[-period:]) / period
    return forex(slow_d)

def calculate_bollinger_bands(prices, window_size, stdev_multiple):
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

def calculate_vix(prices, window_size, period, call_price):
    returns = np.diff(np.log(prices)) * 100
    squared_returns = returns**2
    variance = np.mean(squared_returns[-window_size:])
    annualized_volatility = np.sqrt(variance * period)
    vix = annualized_volatility * call_price
    return forex(vix)

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

start_price = 66110  # 5th Day
end_price = 66339  # 57th Day
stdev_multiple = 2
window_size = 20
price = 66780

period = 57
high = 69351  # 3rd Day
low = 54238  # 9th Day
close = 66339
volume = 22032
alpha = 0.15

harmony = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
prices = [67846, 68017, 69351, 66416, 66110, 63926, 61732, 60761, 54238, 55765, 56887, 57158, 61347, 61445, 60463, 58615, 59136, 61052, 57976, 59132, 59435, 60550, 59291, 60554, 60625, 63976, 64154, 64135, 62976, 59536, 59115, 59062, 59244, 58563, 57275, 59123, 56729, 57203, 56605, 53858, 54382, 56569, 56779, 55074, 58084, 60382, 58582, 58074, 60545, 62096, 63672, 62922, 63140, 64344, 63162, 65182, 66339]
gains, losses = [], []
for i in range(1, len(prices)):
    change = prices[i] - prices[i-1]
    if change > 0:
        gains.append(change)
    elif change < 0:
        losses.append(-change)

moment = calculate_moment(start_price, end_price, period)
print("Momentum:", moment)
typical_price = calculate_typical(high, low, close)
print("Type:", typical_price)
mgs = mean_gap_size(prices, window_size)
print("MGS:", mgs)
rsi = calculate_rsi(gains, period)
std = calculate_std(prices)
print("RSI:", rsi)
print("STD:", std)

trend = calculate_trend(typical_price, volume, rsi)
print("Trend:", trend)
slow_d = calculate_fast_stochastic(prices, period)
print("Dlow:", slow_d)
prev_ema = 65182  # 56th Day
ema = calculate_ema(close, prev_ema, alpha)
print("EMA:", ema)
emv = calculate_emv(high, low, volume)
print("EMV:", emv)

upper_band, lower_band = calculate_bollinger_bands(gains, window_size, stdev_multiple)
print("UB:", upper_band)
print("LB:", lower_band)
aroon_up, aroon_down = calculate_aroon(prices, period)
print("AU:", aroon_up)
print("AD:", aroon_down)

T = 0.25  # Time to expiration (in years)
r = 0.02  # Risk-free interest rate
sigma = 0.2  # Volatility
call_price = black_scholes_call(close, high, T, r, sigma)
print("Call:", call_price)
vix = calculate_vix(prices, window_size, period, call_price)
print("VIX:", vix)

initial_sar = prices[0] - 0.02 * (max(prices[:14]) - min(prices[:14]))
acceleration_factor = 0.02
sar = calculate_sar(prices, initial_sar, acceleration_factor)
print("Stop:", rolex(sar[-1]))
print("Sell:", rolex(sar[0] - mgs/2))
