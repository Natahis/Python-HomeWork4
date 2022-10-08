# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите натуральную степень k: '))
   
for i in range (0, k+1):
    coeff = randint(0, 100)
    
    if coeff != 0:
        if i == 0: num = str(coeff)
        elif i == 1:
            if coeff > 1: num = str(coeff) + '*x' + num
            else: num = 'x' + num
        else:
            if coeff > 1: num = str(coeff) + '*x^' + str(i) + num
            else: num = 'x^' + str(i) + num
        num = '+' + num
if num[0] ==  '+': num = num[1::]
 
print(num, '= 0')

with open('Polynomial.txt', 'w') as data:
    data.write(num)



