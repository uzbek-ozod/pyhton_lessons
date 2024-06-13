# 18 - dars while metodida lugat va royxat bln ishlash.
   # 1 while metodi yordamida royxat bilan ishlash.
   
print("yaqin do'stlaringiz royxatini tuzamziz.".title())
ismlar=[]
n=1
while True:
    savol=f"{n}-do'stingizni kiriting."
    ism=input(savol)
    ismlar.append(ism)
    takroran= input("yana do'stingizni ismini kiritasizmi.? (ha/yo'q)")
    n+=1
    if takroran != "ha":
        break
print("do'stingiznig ro'yxati.".title())
for ism in ismlar:
    print(ism.title())  
  # 2  while yordamida royxat ichidan bironta qiymatni ochirish kodi.
    fruits=['apple', 'strawberry', 'apple', 'apricot', 'apple']
    while 'apple' in fruits:
        fruits.remove('apple')
        print(fruits)
  # 3 while metodida lugat bilan ishlash/
    print("do'tingizni  yoshini saqlaymiz.".title())
    dostlar={}
    ishora=True
    while ishora:
        ism=input("do'stingizni ismini kiriting. ".title())
        yosh=input(f"{ism.title()}ni yoshini kiritng.")
        dostlar[ism]=int(yosh)
        
        javob = input("yana do'stingizn kiritaszmi. ? (ha/yo'q) ")
        if javob=="yo'q":
           ishora= False

    print("do'stlaringiz ro'yxati.".title())
    for ism, yosh in dostlar.items():
        print(f"{ism.title()} {yosh} yoshda.")        