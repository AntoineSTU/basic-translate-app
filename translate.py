from transformers import MarianMTModel, MarianTokenizer

class Traductor:

    def __init__(self, verbose=0):
        self.model_name = 'Helsinki-NLP/opus-mt-en-roa'
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
        self.model = MarianMTModel.from_pretrained(self.model_name)
        if verbose:
            print(self.tokenizer.supported_language_codes)
    
    def translate(self, text, to="fra"):
        translated = self.model.generate(**self.tokenizer([f">>{to}<<{text}"], return_tensors="pt", padding=True))
        return translated


if __name__ == "__main__":
    traductor = Traductor(verbose=1)
    src_text = [
        {"text": "this is a sentence in english that we want to translate to french", "lang": 'fra'},
        {"text": "This should go to portuguese", "lang": "por"},
        {"text": "And this to Spanish", "lang": "esp"}
    ]
    for elt in src_text:
        print("Texte: ", elt["text"])
        print("Traduction in ", elt["lang"] , ": ", traductor.translate(elt["text"], elt["lang"]))