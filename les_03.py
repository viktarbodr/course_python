m = int(input('Введите Ваш вес (в килограммах) :  '))
h = float(input('Введите Ваш рост (в метрах) :  '))
bmi = m / h ** 2

steps_1 = round(bmi) - 11
steps_2 = 49 - round(bmi)
print(f'Ваш индекс массы тела равен: {round(bmi)}\n')
print('10' + '=' * (steps_1) +'|'+ '=' * (steps_2) + '50')
