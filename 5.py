# Шахматный слон ходит по диагонали. 
# Даны две различные клетки шахматной доски, определите, может ли слон попасть с первой клетки на вторую одним ходом.

def bishop (col1, pow1, col2, pow2):
    if abs(col1 - col2) == abs(pow1 - pow2):
        answer = 'YES'
    else:
        answer = 'NO'
    return answer
print(bishop(4, 4, 4, 5))

