import pandas as pd
data = dict()
with open("dif.csv", 'r') as raw:
    for item in raw:
        if ',' in item:
            key,value = item.split(',', 1)
            data[key]=value
        else:
            pass
orders = data
sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
    print(i[0], i[1])
'''
def conva(list):
    return tuple(list)
with open("app.txt", 'r') as fh:
    orders = fh.readlines()
sort_orders = sorted(conva(orders).items(), key=lambda x: x[1], reverse=True)
for i in sort_orders:
	print(i[0], i[1])
'''
