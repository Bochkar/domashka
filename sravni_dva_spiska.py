from random import randint
def check_list(a, b):
    c = list(set(a) & set(b))
    return c
k = int(input("Укажите количество чисел в списках:\n"))
a = [randint(1, 9) for i in range(k)]
print(a)
b = [randint(1, 9) for j in range(k)]
print(b)
try:
    finish_list = check_list(a, b)
    print("Одинаковые элементы списков:\n", sorted(finish_list))
except ValueError:
    print("Что то пошло не так, либо неверное значение...")