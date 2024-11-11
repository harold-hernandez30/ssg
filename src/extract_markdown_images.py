import re

def extract_markdown_images(text):
    links = []


    alt_text_list = re.findall(r"\[(.*?)\]", text)

    return list(map(lambda alt_text: (alt_text, re.findall(rf"\[{alt_text}\]\((.*?)\)", text)[0]), alt_text_list))
    # url_list = re.findall(r"\]\((.*?)\)", text)
    # return url_list