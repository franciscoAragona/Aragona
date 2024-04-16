def ordMenor(L):
    aux=[]
    aux=sorted(L)
    if len(L) % 2 == 0:
        pivot=aux[len(L)-2]
        mid=int((len(L)/2)-1)
    else:
        pivot=aux[len(L)-1]
        mid=int((len(L)/2))
    L.remove(pivot)
    L.insert(mid,pivot)