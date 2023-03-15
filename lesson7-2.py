def check_condition(abcd):
    a = list(map(int, str(abcd)))

    if len(a) != len(set(a)):
        return False
        
    # sq = [1, 4, 9, 16]
    sq = [(i+1) ** 2 for i in range(4)]
    return (a[-1] + a[-2]) in sq    

# поиск новой цифры справа 
def search(abcd = 0):
    if abcd > 9 and not check_condition(abcd):
        return 0

    start = 0 if abcd > 0 else 1
    res = abcd
    for f in range(start, 10):
        m = search(abcd * 10 + f)
        res = max(res, m)
    return res

num = search()
print(num)