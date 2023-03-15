import time

def no_zeroes(f):
    for i in range(CELLS_COUNT):
        rw, cl = cells[i]
        if f[rw][cl] == 0:
            return False
    return True

def dump_field(f):
    for rw in indexes:
        for cl in indexes:
            if f[rw][cl] >= 100:
                print(' ` ',end='')
            else:
                print(f'{f[rw][cl]:^3}',end='')
        print()
    print()

def set_knight(f, rw, cl, d):
    f[rw][cl] += d * 100
    for mv in moves:
        f[rw + mv[0]][cl + mv[1]] += d

def start_scan_field(f):
    best = MAX_KNIGHTS + 1
    for i in range(SIZE, CELLS_COUNT):
        print(f'...{i+1} / {CELLS_COUNT}')
        res = scan_field(f, best, i, 0)
        best = min(best, res)
    print(f'BEST KNIGHTS = {best}')

def scan_field(f, best, ind, num) -> int:
    if num >= best:
        return best + 1
    if num >= FROM_NUM and no_zeroes(f): # found
        end_time = time.perf_counter()
        print(f'time> {end_time - start_time:.8f} seconds')
        print(f'KNIGHTS> {num}')
        dump_field(f)
        return num
    my_best = best
    for i in range(ind, CELLS_COUNT):
        rw, cl = cells[i]
        if f[rw][cl] < 100:
            set_knight(f, rw, cl, +1) # add knights
            scan_res = scan_field(f, my_best, i + 1, num + 1)
            set_knight(f, rw, cl, -1) # del knights
            my_best = min(scan_res, my_best)
    return my_best

SIZE = 8
CELLS_COUNT = SIZE * SIZE
TOTAL_SIZE = SIZE + 4
MAX_KNIGHTS = 11
FROM_NUM = (SIZE * (SIZE + 1) - 1) // 9
f = [] # поле представляет собой 2D-массив
for _ in range(TOTAL_SIZE):
    l = [0 for i in range(TOTAL_SIZE)]
    f.append(l)
indexes = [i+2 for i in range(SIZE)]
cells = list()
for rw in indexes:
    for cl in indexes:
        cells.append((rw, cl))
moves = ((-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1 ,-2), (+1, +2))

print('...started')
start_time = time.perf_counter()
start_scan_field(f)
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")