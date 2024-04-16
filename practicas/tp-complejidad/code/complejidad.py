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

def ContieneSuma(A,n):
    for i in range(len(A)):
        complemento=n-A[i]
        if complemento in A:
            return True
    return False

