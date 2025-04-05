from models.ctranslate import CTranslate


class Translator:
    def __init__(self):
        self.engine = CTranslate()
        
    def run_translator(self, text, source_lang, target_lang, beam_size=4):
        translation = self.engine.translate(text, source_lang, target_lang, beam_size)
    
        return translation