'''
На доске написано 3-хзначное число. В нем переставили
цифры, отчего оно перестало делиться на 18, зато теперь 
оно стало делиться на 7 (сначала не делилось). Какое
наименьшее число могло быть записано?
'''
def number_to_list(num):
    res = [int(a) for a in str(num)]
    # res = []
    # while num > 0:
    #     res.append(num % 10)
    #     num //= 10
    res.sort()
    return res

def test(n7, n18):
    l7 = number_to_list(n7)
    l18 = number_to_list(n18)
    return l7 == l18

numbers18 = []
numbers7 = []

for i in range(100, 999+1):
    if i % 7 == 0 and i % 18 != 0:
        numbers7.append(i)
    if i % 18 == 0 and i % 7 != 0:
        numbers18.append(i)

flag = False
for num18 in numbers18:
    for num7 in numbers7:
        if test(num7, num18):
            print(num18, num7)
            flag = not flag
            break
    if flag:
        break