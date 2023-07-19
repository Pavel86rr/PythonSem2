# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

num = int(input('Введите число n: '))
print(f'Перед Вами ваше число: {num}')
cv = 1
count = 0
while  count*count < num:
    cv = count*count
    count+=1
    print(cv, end=",")