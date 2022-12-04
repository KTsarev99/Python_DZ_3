# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и 
# последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

from random import randint

print('введите количество элементов в списке :')
n = int(input())

list1 = []
for g in range(n):
    list1.append(randint(1, 10))
print(list1)

com=0

i=0

g= len(list1)

list2 = []

while i < len(list1)//2:
    while g > len(list1)//2:
        i+=1
        g-=1
        l = list1[i-1]*list1[g]
        list2.append(l)

print(f'Произведение пар чисел: = {list2}')
