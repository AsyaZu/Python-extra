# Дано натуральное число. 
# Требуется определить, является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO. 

print('Year: ')
year = int(input())
if (year % 4) == 0 and (year % 100) > 0 or (year % 400) == 0:
    print('YES')
else:
    print('NO')