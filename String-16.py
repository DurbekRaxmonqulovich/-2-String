#String-16. Satr berilgan. Satrdagi xamma katta lotin harflari kichigiga almashtiruvchi programma tuzilsin.
satr = input('satrni kiriting: ')
yangi=''
for i in satr:
    if (i>='A')and(i<='Z'):
        yangi=yangi+i.lower()
    else:
        yangi=yangi+i
print(yangi)
