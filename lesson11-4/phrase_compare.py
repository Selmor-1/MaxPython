from phrase_list import phrase_list

class phrase_compare(phrase_list):
    def __init__(self, phrases: list):
        super().__init__(phrases)
        if len(self._phrases) != 2:
            raise Exception('Text has not equal char!')

    def value(self, alphabet: dict) -> int:
        vals = self._phrases
        v0 = vals[0].value(alphabet)
        v1 = vals[1].value(alphabet)
        return 1 if v0 == v1 and v0 > 0 else 0
    
    @property
    def dbg_sign(self): return '='

    def dump(self, alphabet: dict = {}):
        super().dump(alphabet)
        print()