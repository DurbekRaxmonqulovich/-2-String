  
#String-3.  Kodlar jadvalida kiritilgan belgidan oldin va keyin turuvchi belgilarni chiqaruvchi programma tuzilsin.
belgi = input('Belgi kiriting: ')

if len(belgi)==1:
    print('oldingi belgi:', chr(ord(belgi)-1))
    print('oldingi belgi:', chr(ord(belgi)+1))
else:
    print('Faqat 1 ta belgi kiriting')
