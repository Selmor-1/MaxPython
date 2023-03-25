from phrase_abstract import phrase_abstract
from phrase_compare import phrase_compare
from phrase_summ import phrase_summ
from phrase_mult import phrase_mult
from phrase_minus import phrase_minus
from phrase_int import phrase_int
from phrase_str import phrase_str

class phrases_factory():
    @staticmethod
    def split_phrase(text: str) -> phrase_abstract:
        extract = lambda sep: list(map(phrases_factory.split_phrase, text.split(sep)))
        if '=' in text:
            return phrase_compare(extract('='))
        if '*' in text:
            return phrase_mult(extract('*'))
        if '+' in text:
            return phrase_summ(extract('+'))
        if '-' in text:
            return phrase_minus(extract('-'))
        text_spaceless = text.replace(' ', '')
        if text_spaceless.isdigit():
            return phrase_int(text_spaceless)
        return phrase_str(text_spaceless) # if text.isalpha():