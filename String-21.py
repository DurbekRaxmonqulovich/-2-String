#String-21 
#Butun  musbat  sonni  ifodalovchi  satr  berilgan.  Uning  belgilarini
#(raqamlarini)  ongdan chapga qarab chiqaruvchi programma tuzilsin.

satr = input('Musbat son kiriting: ')
yangi=''
index=0
for i in satr[0:-1]:
    index +=1
    yangi += satr[index]
    
yangi += satr[0]
print(yangi)
