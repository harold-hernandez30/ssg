
def enclosed_text(text, delimiter):
    first_index = text.find(delimiter)
    last_index = text.rfind(delimiter)

    return text[first_index + len(delimiter): last_index]