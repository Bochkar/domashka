print('Введите текст:')
str = str(input(': \n'))
print(str)

print('Введите нужный символ: ')
c = input()

s=0
for b in str:
    if b==c:
        s=s+1

if (s) > 0:
    print('количество символов в тексте', (s) ,'раз ')
else:
    print('Нет такого символа!')
