from googletrans import Translator, LANGUAGES

def TransLate(text, src, dest):
    translator = Translator()
    try:
        translation = translator.translate(text, src=src, dest=dest)
        return translation.text
    except Exception as e:
        return str(e)

def LangDetect(text, set="all"):
    translator = Translator()
    try:
        detection = translator.detect(text)
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return str(detection.confidence)
        else:
            return f"Language: {detection.lang}, Confidence: {detection.confidence}"
    except Exception as e:
        return str(e)

def CodeLang(lang):
    try:
        if lang in LANGUAGES:
            return LANGUAGES[lang]
        else:
            return "Language not found"
    except Exception as e:
        return str(e)

def LanguageList(out="screen", text=None):
    try:
        if text is None:
            return "Text parameter is missing"
        if out == "screen":
            print("N\tLanguage\tISO-639 Code\tText")
            print("-" * 80)
            for i, (code, name) in enumerate(LANGUAGES.items(), start=1):
                translation = TransLate(text, "auto", code)
                print(f"{str(i).ljust(5)}{name.ljust(20)}{code.ljust(15)}{translation}")
            return "Ok"
    except Exception as e:
        return str(e)

# Використання функцій
text = "Створити віртуальне оточення (ім'я оточення - прізвище студента). В цьому оточенні створити проект Python"
code_of_dest_lang = "en"
detected_lang = LangDetect(text, set="lang")
translation = TransLate(text, detected_lang, code_of_dest_lang)
dest_lang = CodeLang(code_of_dest_lang)

print("Оригінальний текст: " + text)
print("Мова оригінального тексту: " + detected_lang)
print("Переклад: " + translation)
print("Мова перекладу: " + dest_lang)
print("Код мови перекладу: " + code_of_dest_lang)

LanguageList("screen", text)
