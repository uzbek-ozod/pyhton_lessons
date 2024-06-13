# lambda
import math
uzunlik = lambda pi , r : 2*pi*r
print(uzunlik(math.pi , 2))

kvadrat = lambda x , y : x ** y
print(kvadrat(3 , 5))
 
def daraja(n) :
    return lambda x : x**n
kvadrat= daraja(2)
kub=daraja(3)
print(kvadrat(4))
print(f" 3-ning kvadrati {kvadrat(3)} ga teng," ' '
      f"kubi esa {kub(3)} ga teng. ")

from math import sqrt

sonlar = list(range(11))
son = list(map(sqrt, sonlar))
#print(son)

def daraja2(x):
    return x*x
print(list(map(daraja2, sonlar)))

kvadratlar=list(map(lambda x : x*x, sonlar))
print(kvadratlar)


kvadratlar1=[]
for son in sonlar:
    kvadratlar1.append(son*son)
print(kvadratlar1)

