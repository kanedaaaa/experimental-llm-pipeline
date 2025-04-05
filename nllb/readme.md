# KA-ENG translation with NLLB-200 

This repository provides three versions of the NLLB-200 model: transformer, ctranslate, and a potential hybrid model.

## Model Versions:

- **Transformer Version**
    The transformer version was primarily used for testing purposes and is not optimized for performance. It may not deliver the same efficiency or accuracy as the other versions.

- **Ctranslate Version**
    The ctranslate version utilizes CTranslate2, which has been shown to deliver superior performance on various translation benchmarks. It is the recommended model for efficient and accurate translations.

- **Hybrid Version:**
    A potential hybrid model could leverage CTranslate2 for translation but use Hugging Face tokenizers for preprocessing. However, it is unlikely that this hybrid model will achieve the same level of performance as CTranslate2 alone due to the optimized nature of the latter.

## Use Case:

This model is designed to be integrated into a pipeline that provides on-demand translation, specifically aimed at improving advanced reasoning in the Georgian language with Mistral 7B.

## Model Specifications:

- **Model**: NLLB:200 (1.3B Params)
- **Tested on**: Nvidia 3090 TI with 24GB VRAM
- **Best Performance**: Achieved using the *CTranslate2* Impl.

## Misc

No deep testing was performed ATM, roughly speaking CTranslate2 did the best which was obvious already.

For ease of testing i will rewrite this to be a real-time CLI chat for translation, until i actually start implementing it in my LLM pipeline, probably on different branch to preserve current state.