import ctranslate2
import sentencepiece as spm
import os

class CTranslate:
    # i know im using the full path here and its dumb but rn this works
    def __init__(self, ct_model_path="/home/k4ta/Desktop/llm/nllb/local_models/nllb-200-3.3B-int8", sp_model_path="/home/k4ta/Desktop/llm/nllb/local_models/flores200_sacrebleu_tokenizer_spm.model", device="cuda"):
        if not os.path.exists(ct_model_path):
            raise FileNotFoundError(f"CTranslate2 model not found at: {ct_model_path}")
        if not os.path.exists(sp_model_path):
            raise FileNotFoundError(f"SentencePiece model not found at: {sp_model_path}")
            
        self.sp = spm.SentencePieceProcessor()
        self.sp.load(sp_model_path)
        
        print(f"Loading translation model on {device}...")
        self.translator = ctranslate2.Translator(ct_model_path, device=device)
        print("Model loaded successfully!")
        
        self.eng_code = "eng_Latn"
        self.geo_code = "kat_Geor"
        
    def translate(self, text, source_lang, target_lang, beam_size=4):
        source_sent = [text.strip()]
        target_prefix = [[target_lang]]
        
        source_subworded = self.sp.encode(source_sent, out_type=str)
        source_subworded = [[source_lang] + sent + ["</s>"] for sent in source_subworded]
        
        translations = self.translator.translate_batch(
            source_subworded, 
            batch_type="tokens", 
            max_batch_size=2024, 
            beam_size=beam_size, 
            target_prefix=target_prefix
        )
        
        translation = translations[0].hypotheses[0]
        
        translation_text = self.sp.decode([translation])[0]
        translation_text = translation_text[len(target_lang):]  # Remove language tag
        
        return translation_text.strip()