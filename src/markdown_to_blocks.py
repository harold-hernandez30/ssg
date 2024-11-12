

def markdown_to_blocks(markdown):
    
    def strip_white_spaces(val):
        return val.strip()

    markdown_list = markdown.split('\n\n')

    stripped_markdown_lines = list(map(strip_white_spaces, markdown_list))
    return stripped_markdown_lines