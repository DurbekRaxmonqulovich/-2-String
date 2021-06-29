#String-22 
#Butun musbat sonni ifodalovchi satr berilgan. Shu son raqamlari yig’indisini
#chiqaruvchi programma tuzilsin.

son = int(input("Butun son kiriting "))

summa = 0
while (son != 0):
    summa = summa + son % 10
    son = son // 10
print("Raqamlari yig'indisi: ", summa)
