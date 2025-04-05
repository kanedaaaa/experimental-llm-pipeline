import argparse
import sys
import time
from translator import Translator

def main():
    parser = argparse.ArgumentParser(description="Real-time English-Georgian translator")
    parser.add_argument("--beam_size", type=int, default=4,
                        help="Beam size for translation")
    
    args = parser.parse_args()
    
    translator = Translator()
    
    try:
        
        print("\n===== Real-time English-Georgian Translator =====")
        print("Enter text to translate. Type 'en' or 'ka' followed by a colon to specify source language.")
        print("Examples: 'en: Hello, how are you?' or 'ka: გამარჯობა, როგორ ხარ?'")
        print("Type 'quit', 'exit', or press Ctrl+C to exit.")
        print("=================================================\n")
        
        while True:
            try:
                user_input = input("> ").strip()
                
                if user_input.lower() in ["quit", "exit", "q"]:
                    print("Exiting translator...")
                    break
                
                if not user_input:
                    continue
                
                if user_input.startswith("en:") or user_input.startswith("en :"):
                    source_lang = translator.engine.eng_code
                    target_lang = translator.engine.geo_code
                    text = user_input[user_input.find(":")+1:].strip()
                elif user_input.startswith("ka:") or user_input.startswith("ka :"):
                    source_lang = translator.engine.geo_code
                    target_lang = translator.engine.eng_code
                    text = user_input[user_input.find(":")+1:].strip()
                else:
                    if any(ord(c) >= 0x10A0 and ord(c) <= 0x10FF for c in user_input):
                        source_lang = translator.engine.geo_code
                        target_lang = translator.engine.eng_code
                        text = user_input
                    else:
                        source_lang = translator.engine.eng_code
                        target_lang = translator.engine.geo_code
                        text = user_input
                
                start_time = time.time()
                translation = translator.run_translator(text, source_lang, target_lang, args.beam_size)
                end_time = time.time()
                
                print(f"[{end_time - start_time:.2f}s] {translation}")
                
            except KeyboardInterrupt:
                print("\nExiting translator...")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    except Exception as e:
        print(f"Initialization error: {e}")
        return 1
        
    return 0

if __name__ == "__main__":
    sys.exit(main())