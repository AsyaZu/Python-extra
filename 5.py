# Шахматный слон ходит по диагонали. 
# Даны две различные клетки шахматной доски, определите, может ли слон попасть с первой клетки на вторую одним ходом.
col1 = int(input())
pow1 = int(input())
col2 = int(input())
pow2 = int(input())
if (col1 + pow1) % 2 == 0 and (col2 + pow2) % 2 == 0:
    print('YES')
elif (col1 + pow1) % 2 > 0 and (col2 + pow2) % 2 > 0:
    print('YES')
else:
    print('NO')

def bishop (col1, pow1, col2, pow2):
    if (col1 + pow1) % 2 == 0 and (col2 + pow2) % 2 == 0:
        answer = 'YES'
    elif (col1 + pow1) % 2 > 0 and (col2 + pow2) % 2 > 0:
        answer = 'YES'
    else:
        answer = 'NO'
    return answer
print(bishop(4, 4, 4, 5))

