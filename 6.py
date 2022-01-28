# Шоколадка имеет вид прямоугольника, разделенного на n×m долек. 
# Шоколадку можно один раз разломить по прямой на две части. 
# Определите, можно ли таким образом отломить от шоколадки часть, состоящую ровно из k долек. 
# Программа получает на вход три числа: n, m, k и должна вывести YES или NO.

def chocolate (n, m, k):
    answer = 'NO'
    if ((k>=n or k>=m) and k<m*n) and (k % m == 0 or k % n == 0):
        answer = 'YES'
    return answer
print(chocolate(10, 2, 7))
    