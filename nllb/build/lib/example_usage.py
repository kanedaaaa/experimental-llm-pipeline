from lib import Translator

translator = Translator()
toTranslate = """
The smallest jet engines are known as turbofans or turbojets that are used in miniature
unmanned aerial vehicles (UAVs) and other small aircraft. These tiny engines are driven
by a combination of forces, primarily internal combustion and the principles of gas
dynamics.
"""
trns = translator.run_translator(toTranslate, translator.engine.eng_code, translator.engine.geo_code)

print(trns)