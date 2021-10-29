from transformers import MarianMTModel, MarianTokenizer

class Translator:

    def __init__(self, verbose=0):
        self.model_name = 'Helsinki-NLP/opus-mt-en-roa'
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
        self.model = MarianMTModel.from_pretrained(self.model_name)
        if verbose:
            print(self.tokenizer.supported_language_codes)
    
    def translate(self, text, to="fra"):
        is_str = False
        if isinstance(text, str):
            is_str = True
            text = [text]
        translated = self.model.generate(**self.tokenizer([f">>{to}<<{t}" for t in text], return_tensors="pt", padding=True))
        if is_str:
            return self.tokenizer.decode(translated[0], skip_special_tokens=True)
        return [self.tokenizer.decode(t, skip_special_tokens=True) for t in translated]


if __name__ == "__main__":
    translator = Translator(verbose=1)
    src_text = [
        {"text": "this is a sentence in english that we want to translate to french", "lang": 'fra'},
        {"text": "This should go to portuguese", "lang": "por"},
        {"text": "And this to Spanish", "lang": "esp"}
    ]
    for elt in src_text:
        print("Text: ", elt["text"])
        print("Traduction in ", elt["lang"] , ": ", translator.translate(elt["text"], elt["lang"]))