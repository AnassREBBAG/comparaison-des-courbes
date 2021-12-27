import numpy as np
import pylab as pl
from math import exp,cos

#developpement limité de qlq fcts usuelles

#factoriel
def facto(n):
    P=n
    if n==0 or n==1:
        return 1
    else:
        for i in range(1,n):
            P=P*i
    return P



#dl(n)(exp)

n=4                  #ordre du dev limité
def dl_expo(x):
    S=0
    for i in range(n):
        S+=(1/facto(i))*(x**i)
    return S


T=np.linspace(-4,4,100)
C=[dl_expo(t) for t in T]
E=[exp(t) for t in T]
pl.plot(T,C,T,E,)
pl.show()
