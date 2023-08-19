# проверка на наличие цифры в числе +++++
def in_num(f, num):
    while num > 0:
        pice = num % 10
        if f == pice:
            return True
        num //= 10
    return False

def has_same(abcd):
    abc = abcd // 10
    d = abcd % 10
    return in_num(d, abc)
    
# сумма является полным квадратом 
def check_square(d, f):
    sum = d + f
    return sum == 1 or sum == 4 or sum == 9 or sum == 16
def has_square(abcd):
    d = abcd % 10
    c = abcd // 10 % 10
    return check_square(d, c)


# поиск новой цифры справа 
def search(abcd):
    if abcd > 9:
        if has_same(abcd) or not has_square(abcd):
            return 0

    res = abcd
    for f in range(10):
        n = abcd * 10 + f
        m = search(n)
        res = max(res, m)
    return res

num = 0
for i in range(1, 10):
    max_num = search(i)
    num = max(max_num, num)
print(num)
