print('Введите диапазон чисел:')
a = int(input('OT: \n'))
b = int(input('До: \n'))
from random import randint
list = [randint(a,b+1) for i in range(20)]
print(list)
print('Введите нужное число: ')
c = int(input())
if c not in list:
    print('Нет такой цифры в списке!')
y=0
for i in list:
    y=y+1
    if i==c:
        print('место в списке')
        print(y)