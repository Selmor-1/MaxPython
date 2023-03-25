from phrase_abstract import phrase_abstract

class phrase_str(phrase_abstract):
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
