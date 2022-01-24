# Даны три целых числа. 
# Определите, сколько среди них совпадающих. 
# Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).

def numbers (num1, num2, num3):
    answer = 0
    if num1 == num2 == num3:
        answer = 3
    elif num1 == num2 or num1 == num3 or num2 == num3:
        answer = 2
    return(answer)

print(numbers(2, 2, 2))
