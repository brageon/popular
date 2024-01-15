with open("ap1.txt", "r") as fin:
    v1, v2, v3, v4 = [float((i).replace(',','.')) for i in fin.readline().split()]
# 7,4 % : 12,4 128,7 26,8 70 : KV - BS = 7,8 : 116-43/10 = 7,3 >> 65, EE not exist
# (Likviditet/Vinst - Brutto/Soliditet)-(d)^-1 = secure accounting score
# Wolter has 1 year and Recco has 30 years. W is 2 % while R is 3 %. 
se = v2 / v1
te = v4 / v3
alu = se - te
sel = v1 - v2
tel = v3 - v4
alux = sel - tel
print((alu - alux)/2)
