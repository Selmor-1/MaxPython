import time

def zeroes_count(f):
    res = 0
    for rw in indexes:
        for cl in indexes:
            if f[rw][cl] == 0:
                res += 1
    return res

def dump_field(f):
    print()
    # for rw in range(TOTAL_SIZE):
    #     print(*f[rw])
    # for rw in range(SIZE):
    #     print(*f[rw+2][2:2+SIZE])
    for rw in indexes:
        for cl in indexes:
            if f[rw][cl] >= 100:
                print(' ` ',end='')
            else:
                print(f'{f[rw][cl]:^3}',end='')
        print()
    # print(*f)

def set_knight(f, rw, cl, d):
    f[rw][cl] += d * 100
    for mv in moves:
        f[rw + mv[0]][cl + mv[1]] += d

# поле представляет собой 2D-массив
def scan_field(f, best, num = 0) -> int:
    if num >= best:
        return best + 1

    if num >= FROM_NUM and zeroes_count(f) == 0: # found
        dump_field(f)
        return num

    my_best = best
    for rw in indexes:
        for cl in indexes:
            if f[rw][cl] < 100:
                set_knight(f, rw, cl, +1) # add knights
                scan_res = scan_field(f, my_best, num + 1)
                set_knight(f, rw, cl, -1) # del knights
                my_best = min(scan_res, my_best)
    return my_best

SIZE = 5 # 8
TOTAL_SIZE = SIZE + 4
MAX_KNIGHTS = 9 # 13
FROM_NUM = (SIZE * (SIZE + 1) - 1) // 9
indexes = [i+2 for i in range(SIZE)]
moves = [[-2, -1], [-2, +1], [+2, -1], [+2, +1], [-1, -2], [-1, +2], [+1 ,-2], [+1, +2]]
f = []
for _ in range(TOTAL_SIZE):
    l = [0 for i in range(TOTAL_SIZE)]
    f.append(l)

# print(f'FROM_NUM = {FROM_NUM}')
# dump_field(f)

print('...started')

start_time = time.perf_counter()
print(scan_field(f, MAX_KNIGHTS + 1))
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")