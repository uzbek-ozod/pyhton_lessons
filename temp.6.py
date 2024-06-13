def baholar(ismlar):
   baholar={}
   while ismlar:
       ism = ismlar.pop()
       baho= input(f"{ism.title()}ning bahosini kiriting. ")
       baholar[ism]= int(baho)
   return baholar
   
talabalar= [ 'ali', ' vali', 'hakim' ] 
baholar=baholar(talabalar[:])
print(baholar)   