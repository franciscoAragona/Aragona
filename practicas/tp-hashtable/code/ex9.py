from dictionary import *

def subconjunto(s,t):
    if len(s) == len(t):
        if s == t:
            return True
        else:
            return False
    d=creat(9)
    for car in t:
        insert(d,car,car)
    for car in s:
        if search(d,car) is None:
            return False
    return True

print(subconjunto("holaa","hola"))