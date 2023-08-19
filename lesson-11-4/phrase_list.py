from phrase_abstract import phrase_abstract

class phrase_list(phrase_abstract):
    def __init__(self, phrases: list):
        self._phrases = phrases

    @property
    def dbg_sign(self): pass

    def dump(self, alphabet: dict = {}):
        for ind, it in enumerate(self._phrases):
            if ind > 0:
                print(f' {self.dbg_sign} ', end='')
            it.dump(alphabet)