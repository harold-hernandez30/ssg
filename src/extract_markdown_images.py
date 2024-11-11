import re

def extract_markdown_images(text):
    regex_image_alt_text = r"\[(.*?)\]"
    alt_text_list = re.findall(regex_image_alt_text, text)

    def extract_image_url(alt_text, line):
        return re.findall(rf"\[{alt_text}\]\((.*?)\)", line)
    
    return list(map(lambda alt_text: (alt_text, extract_image_url(alt_text, text)[0]), alt_text_list))