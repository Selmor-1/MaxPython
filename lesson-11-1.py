import time

def str_to_int(s, d):
    # res = s
    # for key in d:
    #     res = res.replace(key, str(d[key]))
    # return int(res)
    res = 0
    for c in s:
        res = 10 * res + d[c]
    return res

def different(num) -> bool:
    s = str(num)
    a = set(s)
    return len(s) == len(a)

def search(alphabet):
    d = dict.fromkeys(alphabet, 0)
    pwr = len(alphabet)
    fr = 10**(pwr-1)
    to = 10**pwr
    # print(fr, to)
    for num in range(fr, to):
        # print(num)
        if different(num):
            n = num
            for c in alphabet:
                d[c] = n % 10
                n = n // 10
            if check(d):
                print(d)

def check(d):
    # # 4
    # a = str_to_int('баклан', d)
    # b = str_to_int('макака', d)
    # c = str_to_int('гибрид', d)
    # return a + b == c
    # # 0    
    # a = str_to_int('ЛЕТО', d)
    # b = str_to_int('ПОЛЕТ', d)
    # return a + a == b
    # 1
    # a = str_to_int('ПЧЕЛКА', d)
    # # ToDo: first letter != 0
    # # ToDo: if a < 10**(len(a)) ... False
    # b = str_to_int('ЖЖЖЖЖЖ', d)
    # # ToDo: if b < 10**(len(b)) ... False
    # return a * 7 == b
    # 2
    a = str_to_int('ШЕЛ', d)
    b = str_to_int('ПРИШЕЛ', d)
    return a * a == b

# s = 'ШЕЛ * ШЕЛ = ПРИШЕЛ'
alphabet = 'ПРИШЕЛ' # 3.26808393 seconds
# alphabet = 'ПЧЕЛКАЖ'
# alphabet = 'ПОЛЕТ'
# alphabet = 'баклнмгирд' # 'баклан+макака=гибрид'

start_time = time.perf_counter()

res = search(alphabet)

end_time = time.perf_counter()
print(f"Ver.1 time: {end_time - start_time:.8f} seconds")

# print(res)
'''
d = dict.fromkeys(alphabet, 0)
d['Ш'] = 1
d['Е'] = 2
d['Л'] = 1
a = str_to_int('ШЕЛ', d)
print(a)
print(different(a))
'''