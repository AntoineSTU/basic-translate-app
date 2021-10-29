import pytest
from translate import Translator

def test_translate_default():
    translator = Translator()
    src_text = "this is a sentence in english that we want to translate to french"
    trad = "c'est une phrase en anglais que nous voulons traduire en français"

    out_text = translator.translate(src_text)

    assert trad == out_text

def test_translate_spanish():
    translator = Translator()
    src_text = "This should go to spanish"
    trad = "Esto debería ir a español"

    out_text = translator.translate(src_text, to="spa")

    assert trad == out_text



def test_translate_mutliple():
    translator = Translator()
    src_texts = ["This should go to french", "Another sentence", "A third (and beautiful) one"]
    trads = ['Cela devrait aller en français', 'Une autre phrase', 'Une troisième (et belle) une']

    out_texts = translator.translate(src_texts)

    assert trads == out_texts