# 7,4 % : 12,4 128,7 26,8 70 : KV - BS = 7,8 : 116-43/10 = 7,3 >> 65, EE not exist
# (Likviditet/Vinst - Brutto/Soliditet)-(d)^-1 = secure cfo score. Wget from URLs list.
# Wolter has 1 year and Recco has 30 years. W is 2 %, R is 3 %. Also 27 Jones (flake8)

with open("ap1.txt", "r") as fin:
    v1, v2, v3, v4 = [float((i).replace(',','.')) for i in fin.readline().split()]
se = v2 / v1
te = v4 / v3
alu = se - te
sel = v1 - v2
tel = v3 - v4
alux = sel - tel
print((alu - alux)/2)