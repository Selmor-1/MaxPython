import time

class abstract_phrase():
    def value(self, alphabet: dict) -> int:
        pass
    def dump(self, alphabet: dict = {}):
        pass



# single phrases
class int_phrase(abstract_phrase):
    def __init__(self, subtext: str):
        self.const_value = int(subtext)

    def value(self, alphabet: dict) -> int:
        return self.const_value
    
    def dump(self, alphabet: dict = {}):
        print(str(self.const_value), end='')



class str_phrase(abstract_phrase):
    def __init__(self, subtext: str):
        self.text = subtext

    def value(self, alphabet: dict) -> int:
        res = 0
        for ind, key in enumerate(self.text):
            res = 10 * res + alphabet[key]
            if ind == 0 and res == 0:
                return 0
        return res        

    def dump(self, alphabet: dict = {}):
        txt = self.text
        for key in alphabet:
            txt = txt.replace(key, str(alphabet[key]))
        print(txt, end='')



# multiple phrases
class list_phrase(abstract_phrase):
    def __init__(self, phrases: list):
        self._phrases = phrases

    @property
    def dbg_sign(self): pass

    def dump(self, alphabet: dict = {}):
        for ind, it in enumerate(self._phrases):
            if ind > 0:
                print(f' {self.dbg_sign} ', end='')
            it.dump(alphabet)



class compare_phrase(list_phrase):
    def __init__(self, phrases: list):
        super().__init__(phrases)
        if len(self._phrases) != 2:
            raise Exception('Text has not equal char!')

    def value(self, alphabet: dict) -> int:
        vals = self._phrases
        v0 = vals[0].value(alphabet)
        v1 = vals[1].value(alphabet)
        return 1 if v0 == v1 else 0
    
    @property
    def dbg_sign(self): return '='

    def dump(self, alphabet: dict = {}):
        super().dump(alphabet)
        print()



class mult_phrase(list_phrase):
    def value(self, alphabet: dict) -> int:
        res = 1
        for ph in self._phrases:
            res *= ph.value(alphabet)
        return res

    @property
    def dbg_sign(self): return '*'



class summ_phrase(list_phrase):
    def value(self, alphabet: dict) -> int:
        res = 0
        for ph in self._phrases:
            res += ph.value(alphabet)
        return res

    @property
    def dbg_sign(self): return '+'



class minus_phrase(list_phrase):
    def value(self, alphabet: dict) -> int:
        res = 0
        for ind, ph in enumerate(self._phrases):
            if ind > 0:
                res -= ph.value(alphabet)
            else:
                res = ph.value(alphabet)
        return res

    @property
    def dbg_sign(self): return '-'


# factory
class phrases_factory():
    @staticmethod
    def split_phrase(text: str) -> abstract_phrase:
        extract = lambda sep: list(map(phrases_factory.split_phrase, text.split(sep)))
        if '=' in text:
            return compare_phrase(extract('='))
        if '*' in text:
            return mult_phrase(extract('*'))
        if '+' in text:
            return summ_phrase(extract('+'))
        if '-' in text:
            return minus_phrase(extract('-'))
        text_spaceless = text.replace(' ', '')
        if text_spaceless.isdigit():
            return int_phrase(text_spaceless)
        # if text.isalpha():
        #     pass
        return str_phrase(text_spaceless)



def search(code: str, alone: bool = False):
    def different(num) -> bool:
        s = str(num)
        return len(s) == len(set(s))

    try:
        root = phrases_factory.split_phrase(code)
        # root.dump()
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


# CODE = 'AAA + BBB + DDD + E = CCC'
# CODE = 'ШЕЛ * ШЕЛ = ПРИШЕЛ' # 3.97828845 seconds
# CODE = 'АТАКА + УДАР + УДАР = НОКАУТ' # (8)
# CODE = 'ТЭТА + БЭТА = СУММА' # (7) 32.11183400 seconds
CODE = 'ПЧЕЛКА * 7 = ЖЖЖЖЖЖ' # (7) 28.39182995 seconds

if __name__ == "__main__":
    start_time = time.perf_counter()
    search(CODE)
    end_time = time.perf_counter()
    print(f"Ver.3 time: {end_time - start_time:.8f} seconds")