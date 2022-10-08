# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

with open('file1.txt', 'r') as data:
    polynomial1 = data.readline()
with open('file2.txt', 'r') as data:
    polynomial2 = data.readline()

print(polynomial1)
print(polynomial2)

lst1 = polynomial1[:-3]
lst2 = polynomial2[:-3]

print(f'{lst1}+ {lst2}= 0')

with open('file3.txt', 'w') as data:
    data.write(f'{lst1}+ {lst2}= 0')
