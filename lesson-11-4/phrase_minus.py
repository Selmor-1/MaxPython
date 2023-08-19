from phrase_list import phrase_list

class phrase_minus(phrase_list):
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