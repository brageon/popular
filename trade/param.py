import math, statistics
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
    return forex(rsi), rolex(avg_loss)
def calculate_trend(typical_price, volume, rsi):
    trend = math.log(typical_price * volume) * (1 - rsi / 100)
    return forex(trend)
def calculate_ema(price, prev_ema, alpha):
    ema = price * alpha + prev_ema * (1 - alpha)
    return forex(ema)
def calculate_bollinger_bands(prices, window_size, stdev_multiple):
    sma = sum(prices[-window_size:]) / window_size
    squared_differences = [(price - sma)**2 for price in prices[-window_size:]]
    variance = sum(squared_differences) / (window_size - 1)
    stdev = math.sqrt(variance)
    upper_band = sma + stdev_multiple * stdev
    lower_band = sma - stdev_multiple * stdev
    return rolex(upper_band, lower_band)
def calculate_fibonacci(high, low):
    delta = high - low
    abc = 0.236 * delta
    bcd = 0.382 * delta
    cde = 0.500 * delta
    efg = 0.618 * delta
    fgh = 0.786 * delta
    return rolex(abc, bcd, cde, efg, fgh)
start_price = 66339
end_price = 67846
stdev_multiple = 2
window_size = 20
period = 57
high = 73097
low = 40112
close = 66339
volume = 22032
alpha = 0.15
moment = calculate_moment(start_price, end_price, period)
print("Momentum:", moment)
typical_price = calculate_typical(high, low, close)
print("Type:", typical_price)
prices = [67846, 68017, 69351, 66416, 66110, 63926, 61732, 60761, 54238, 55765, 56887, 57158, 61347, 61445, 60463, 58615, 59136, 61052, 57976, 59132, 59435, 60550, 59291, 60554, 60625, 63976, 64154, 64135, 62976, 59536, 59115, 59062, 59244, 58563, 57275, 59123, 56729, 57203, 56605, 53858, 54382, 56569, 56779, 55074, 58084, 60382, 58582, 58074, 60545, 62096, 63672, 62922, 63140, 64344, 63162, 65182, 66339]
gains, losses = [], []
for i in range(1, len(prices)):
    change = prices[i] - prices[i-1]
    if change > 0:
        gains.append(change)
    elif change < 0:
        losses.append(-change)
rsi, ted = calculate_rsi(gains, period)
std = calculate_std(prices)
print("RSI:", rsi)
print("Loss:", ted)
print("STD:", std)
trend = calculate_trend(typical_price, volume, rsi)
print("Trend:", trend)
prev_ema = 65398
ema = calculate_ema(close, prev_ema, alpha)
print("EMA:", ema)
upper_band, lower_band = calculate_bollinger_bands(gains, window_size, stdev_multiple)
print("UB:", upper_band)
print("LB:", lower_band)
abc, bcd, cde, efg, fgh = calculate_fibonacci(high, low)
print("1/5F:", abc)
print("2/5F:", bcd)
print("3/5F:", cde)
print("4/5F:", efg)
print("5/5F:", fgh)                                                                                                                                                                                                                      print("5/5F:", fgh)
