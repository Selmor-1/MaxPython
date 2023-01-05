def simple(n):
    i = 2
    while i * i <= n:
        if (n % i == 0):
            return False
        i += 1
    return True

n = 100

for a in range(2, n+1):
    if not simple(a):
        continue
    for b in range(a, n+1):
        if not simple(b):
            continue
        for c in range(b, n+1):
            if not simple(c):
                continue
            if a * b * c == 7 * (a + b + c):
                print(a, b, c)