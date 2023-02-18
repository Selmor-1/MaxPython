def address(index): #
    return index % 8, index // 8

def field_is_full(f):
    return False

def dump_field(f):
    print(*f)

# поле представляет собой 2D-массив
def scan_field(f, num = 1) -> int:
    for ind in range(64):
        # cl, rw = address(ind)
        cl, rw = ind % 8, ind // 8
        if f[rw][cl] < 0:
            continue
        f[rw][cl] = -1 * (f[rw][cl] + 1)
        # add knights
        if num == 1:
            dump_field(f)
        if num > 7 and field_is_full(f):
            #  print field
            return num
        # if num < 13:
        if num < 3:
            scan_field(f, num + 1)
        f[rw][cl] = -1 * f[rw][cl] - 1

f = []
for _ in range(8):
    l = [0 for i in range(8)]
    f.append(l)

scan_field(f)

# dump_field(f)