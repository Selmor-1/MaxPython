from phrase_list import phrase_list

class phrase_summ(phrase_list):
    def value(self, alphabet: dict) -> int:
        res = 0
        for ph in self._phrases:
            res += ph.value(alphabet)
        return res

    @property
    def dbg_sign(self): return '+'
