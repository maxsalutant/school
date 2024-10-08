# Операнды арифметического выражения записаны в системах счисления с основаниями 9 и 11:
# 88x4y(9) + 7x44y(11).

# В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
# Определите значения x и y, при которых значение данного арифметического выражения будет наименьшим и кратно 61. 
# Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 61 и укажите его в ответе в десятичной системе счисления. 
# Основание системы счисления в ответе указывать не нужно.

# Решение:
# При помощи цикла for будем перебирать x и y в соответствии в заданными системами счислений. Затем переведём все числа в десятичную систему счисления и найдём их сумму, 
# записав полученное значение в переменную.
# Проверим кратность переменной на 61 и выведем частное от деления значения арифметического выражения.

data = []
for x in range(9):
    for y in range(9):
        n1 = y + 4*9 + x*9*9 + 8*9*9*9 + 8*9*9*9*9
        n2 = y + 4*11 + 4*11*11 + x*11*11*11 + 7*11*11*11*11
        if (n1 + n2) % 61 == 0:
            data.append([x, y, n1+n2])
            
for d in data:
    print('x=', d[0], 'y=', d[1], 'sum=', d[2], 'sum//61=', d[2]//61)


result_search = []
for x in '012345678':
    for y in '012345678':
        t = int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11)
        if t % 61 == 0:
            result_search.append(t)
if result_search:         
    print(min(result_search) // 61)