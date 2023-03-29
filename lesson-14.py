def summ(field, row, col):
    res = 0
    d = ((0, -1), (-1, -1), (-1, 0), (-1, +1))
    for it in d:
        i, j = row + it[0], col + it[1]
        res += field[i][j]
    return res

def s(n):
    res = 0
    k = n
    while k > 9:
        res += 1
        k = k // 10
    if res > 0:
        return str(n // 10**res) + 'e' + str(res)
    return str(n)

K = 25
M = 36

field = []
for _ in range(K+2):
    field.append([0 for _ in range(M+2)])

field[0][0] = 1
for row in range(1, K+1):
    for col in range(1, M+1):
        field[row][col] = summ(field, row, col)

for row in field:
    for it in row:
        print(f'{s(it):>5}', end=' ')
    print()

r = field[K][M]
print(f'ANSWER = {r}')
# ANSWER = 19863974434881155980986194449