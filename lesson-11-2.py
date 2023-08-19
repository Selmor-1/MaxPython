import time

''' splitter '''
class splitter():
    def __init__(self, phrase: str, operators: str) -> None:
        self.phrase = phrase
        self.items = list()
        self.action = ''
        for op in operators:
            if op in phrase:
                self.action = op
                ops = phrase.split(op)
                for it in ops:
                    subsplitter = splitter(it, operators)
                    self.items.append(subsplitter)
                break
    
    def dump(self):
        # print('-'*10)
        if self.action == '':
            print(f'{self.phrase}', end='')
        else:
            for ind, it in enumerate(self.items):
                if ind > 0:
                    print(f' {self.action} ', end='')
                it.dump()
        if self.action == '=':
            print()

    def get_str(self, alphabet: dict) -> str:
        if self.action == '':
            val = self.get_int(alphabet)
            return str(val)
        res = ''
        for ind, it in enumerate(self.items):
            s = it.get_str(alphabet)
            if ind > 0:
                res += ' ' + self.action + ' ' + s
            else:
                res = s
        return res           

    def get_int(self, alphabet: dict) -> int:
        # decode single
        res: int = 0
        if self.action == '': # empty list
            for c in self.phrase:
                res = 10 * res + alphabet[c]
                if res == 0:
                    return 0
            return res
        # decode mulptiple items
        for ind, it in enumerate(self.items):
            val = it.get_int(alphabet)
            if ind > 0:
                if self.action == '=':
                    if res == val:
                        return 1
                    return 0
                elif self.action == '+':
                    res += val
                elif self.action == '-':
                    res -= val
                elif self.action == '*':
                    res *= val
                # else: raise exception 
            else:
                res = val
        return res

''' functions '''
def search(code: str, operators: str, alone: bool):
    def get_alphabet() -> dict:
        a = set(code_spaceless)
        b = a.difference(set(operators))
        return dict.fromkeys(b, 0)
    
    def different(num) -> bool:
        s = str(num)
        return len(s) == len(set(s))

    code_spaceless = code.replace(' ', '')
    phrase = splitter(code_spaceless, operators)
    phrase.dump() # dump
    alphabet: dict = get_alphabet()
    print(f'alphabet len = {len(alphabet)}')
    to = 10 ** len(alphabet)
    fr = to // 10
    for num in range(fr, to):
        if different(num):
            for key in alphabet:
                alphabet[key] = num % 10
                num = num // 10
            if phrase.get_int(alphabet) > 0:
                s = phrase.get_str(alphabet)
                print(s, alphabet, sep='\n')
                if alone:
                    return

''' MAIN '''
### ToDo: digital constants doens't supported

# CODE = 'баклан + макака = гибрид'
# CODE = 'AAA + BDD = ACC'
# CODE = 'AAA + BBB + DDD + E = CCC'
# CODE = 'ШЕЛ * ШЕЛ = ПРИШЕЛ' # 4.46909240 seconds
CODE = 'ТЭТА + БЭТА = СУММА' # (7) 28.55961910 seconds
# CODE = 'КАФТАН + КАФТАН = ТРИШКА' # (8)
# CODE = 'АТАКА + УДАР + УДАР = НОКАУТ' # (8)
# CODE = 'ПОДАЙ - ВОДЫ = ПАША' # (8)
# CODE = 'охохо+ахаха=ахахах'
# CODE = 'This+is=easy'
OPERATORS = '=+-*'
SINGLE_ANSWER = True

start_time = time.perf_counter()
search(CODE, OPERATORS, SINGLE_ANSWER)
end_time = time.perf_counter()
print(f"Ver.2 time: {end_time - start_time:.8f} seconds")