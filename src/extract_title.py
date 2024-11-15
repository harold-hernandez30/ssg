
from markdown_to_blocks import markdown_to_blocks

def extract_title(markdown):

    title = markdown_to_blocks(markdown)[0]
    if title.startswith("# "):
        return title.split("# ")[1]
    else:
        raise Exception("No title found")