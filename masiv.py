def my_function(a):
    b = sum([int(x) for x in str(a)])
    print("Сумма елементов введенного числа составляет:" + str(b))
try:
    my_function(int(input("Введите число:")))
except ValueError:
    print("только числа")