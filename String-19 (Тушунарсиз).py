#String-19.  Satr berilgan. Agar satrda butun son ifodalangan bo’lsa 1
#chiqarilsin, agar haqiqiy son bo’lsa 2 chiqarilsin. Agar satrni songa
#aylantirish imkoni bo’lmasa 0 chiqarilsin. Haqiqiy sonning kasr qismi
#nuqta “.” Bilan ajratilgan deb qabul qilinsin.

satr = input('Satrni kiriting: ')
i=0 
sanoq=0
while i<=len(satr):    
    if int(i)>='0' and i<='9':
        sanoq+=1
if sanoq==len(satr):
    print('Butun son kiritildi')
