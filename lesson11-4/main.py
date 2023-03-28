import time
from phrases_factory import phrases_factory

def get_phrase(pl):
    print('0. Свой вариант')
    for ind, it in enumerate(pl):
        print(f'{ind+1}. {it}')
    n = int(input('Введите номер строки: '))
    if n-1 in range(len(pl)):
        return pl[n-1]
    return input('Введите свой вариант: ')

def search(code: str, alone: bool = False):
    def different(num) -> bool:
        s = str(num)
        return len(s) == len(set(s))

    try:
        root = phrases_factory.split_phrase(code)
        root.dump()
    except Exception as ex:
        print(ex)
        return
    a = set([c for c in code if c.isalpha()])
    alphabet = dict.fromkeys(a, 0)
    print(f'alphabet len = {len(alphabet)}, {alphabet}')
    to = 10 ** len(alphabet)
    fr = to // 10
    for num in range(fr, to):
        if different(num):
            for key in alphabet:
                alphabet[key] = num % 10
                num = num // 10
            # print(f'{alphabet}')
            if root.value(alphabet) > 0:
                root.dump(alphabet)
                root.dump()
                if alone:
                    return
                
CODES = [
    'AAA + BBB + DDD + E = CCC',
    'ШЕЛ * ШЕЛ = ПРИШЕЛ', # 3.97828845 seconds
    'АТАКА + УДАР + УДАР = НОКАУТ', # (8)
    'ТЭТА + БЭТА = СУММА', # (7) 32.11183400 seconds
    'ПЧЕЛКА * 7 = ЖЖЖЖЖЖ', # (7) 28.39182995 seconds
    'MAKS + LINA = KATKA' #
]

if __name__ == "__main__":
    start_time = time.perf_counter()
    p = get_phrase(CODES)
    search(p)
    end_time = time.perf_counter()
    print(f"Ver.4 time: {end_time - start_time:.8f} seconds")