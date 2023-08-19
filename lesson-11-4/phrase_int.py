from phrase_abstract import phrase_abstract

class phrase_int(phrase_abstract):
    def __init__(self, subtext: str):
        self.const_value = int(subtext)

    def value(self, alphabet: dict) -> int:
        return self.const_value
    
    def dump(self, alphabet: dict = {}):
        print(str(self.const_value), end='')