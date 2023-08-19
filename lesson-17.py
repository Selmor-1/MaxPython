def f(it):
    s = str(it//10)
    s = '4' + s
    return int(s)


it = 14 

while True:
    if it * 4 == f(it):
        print(it, "Yes")
        # break
    it += 10