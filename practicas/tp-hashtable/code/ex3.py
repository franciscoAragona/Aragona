from math import *
def hashMult(key,m):
    a=(sqrt(5)-1)/2
    return floor(m*((key*a)-floor(key*a)))

dicc = [None]*1000
for num in range(61, 66):
    print(hashMult(num, 1000))