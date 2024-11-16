import re

def extract_markdown_links(text):
    # Stole with not so good feels from boot.dev solution
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


    