from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/nllb-200-1.3B"  
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

source_lang = 'eng_Latn' 
target_lang = 'kat_Geor'  

text_to_translate = "text to translate"

tokenizer.src_lang = source_lang
encoded_input = tokenizer(text_to_translate, return_tensors="pt")

target_lang_id = tokenizer.convert_tokens_to_ids(target_lang)

translated_tokens = model.generate(
    **encoded_input, 
    forced_bos_token_id=target_lang_id
)

translated_text = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
print(translated_text)
