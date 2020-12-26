a = int(input('Введите значение a:'))
b = int(input('Введите значение b:'))
c = int(input('Введите значение с:'))
print(a != 0 and b != 0 and c != 0 and 'Нет нулевых значений')  
nul = a or b or c or 'Введены все нули'
print(f'Первое ненуленвое значение = {nul}')
if a > b + c:
    print(a - b - c)
else:
    print(b + c - a)
if a > 50 and (b > a or c > a):
    print('Вася')
if a > 5 and (b == 7 or c == 7):
    print('Петя')
