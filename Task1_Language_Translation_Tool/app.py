from deep_translator import GoogleTranslator

def translate_text(text, source, target):
    if not text.strip():
        return ""

    try:
        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        return translated

    except Exception as e:
        return str(e)