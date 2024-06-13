
# 23-mavzu modullar.
# 1
import avto_info as alik 
avto1=alik.avto_info('gm', 'malibu', 'qizil', 'avtomat', 2019, 30000.)
alik.info_print(avto1)
# 2
from avto_info import avto_info, info_print
avto2=avto_info('gm', 'malibu', 'qizil', 'avtomat', 2019, 30000.)
info_print(avto2)
# 3
from avto_info import avto_info as ainfo, info_print as iprint
avto3=ainfo('gm', 'malibu', 'qizil', 'avtomat', 2019, 30000.)
iprint(avto3)
# modular pyhtondagi.
import math
x = 2500
print(math.sqrt(x)) # sqrt() soning ildizini hisoblaydi.
print(math.pow(4, 3)) # pow() soning darajasini hisoblaydi.
print(math.pi)
print(math.log10(10000))
print(math.log2(8))
# random moduli.
import random 
son= random.randint(1, 100) # randint() kiritilgan sonlar ichidan bironta sonni geniritatsiya qilib berad.
print(son)
# 1 choice()
ismlar=['ali', 'vali', 'abu', 'husan', 'hasan']
ism = random.choice(ismlar) # choice() bironta qiymatni tanlab beradi.
print(ism)
print(random.choice(ism))
son1=list(range(0, 101, 11))
qiymat=random.choice(son1)
print(qiymat)
# 3 shuffle() moduli, qiymatlarni arawlaw qiladi.
y= list(range( 11))
print(y)
random.shuffle(y)
print(y)