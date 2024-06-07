son=float(input("juft son kiriting!>>>".title()))
if son%2:
    print("bu juft son emas>".title())
else:
    print("raxmat.".title())
   
yosh=int(input("quyidagi joyga yoshingizni kiriting!.".title()))
if yosh<=5:
    narx=0
elif yosh>=10:
    narx=5000
else:
    narx=10000
print(f"sizga kirish narxi {narx} ming".title())   

x=float(input("birinchi raqamni kiriting.".title()))
y=float(input("ikkinchi raqamni kiriting.".title()))

if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")

mahsulotlar=['kechup', 'meva', 'kanfet', 'ruchka va daftar', 'flash', 'ruchka']
savat=[]
for n in range(5):
    savat.append(input(f"iltmos {n+1} ta mahsulot kiritng ".title()))
    
for mahsulot in savat:
   if mahsulot in mahsulotlar:
        print(f"dokonimizda bu {mahsulotlar} bor")    
else:
        print(f"dokinimizda bu {mahsulotlar} yoq".title())
   