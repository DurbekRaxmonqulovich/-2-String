#String-8. N natural soni va belgi berilgan. N ta kiritilgan belgidan iborat satr hosil qiling va ekranga chiqaring. Masalan: N = 5; Belgi = ‘A’; Natija = AAAAA

n=int(input('Son kiriting: '))
Belgi = input('Belgini kiriting: ')
if len(Belgi) ==1:
    Natija = Belgi*n
else:
    Natija = "1 ta belgi kiriting"

print(Natija)
