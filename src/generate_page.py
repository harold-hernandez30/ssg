from os import path, listdir, mkdir
from markdown_to_htmlnode import markdown_to_htmlnode
from extract_title import extract_title

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if path.isfile(dir_path_content):
        generate_page(dir_path_content, template_path, dest_dir_path)
    else:
        
        if not path.exists(dest_dir_path):
            mkdir(dest_dir_path)

        for file in listdir(dir_path_content):
            generate_pages_recursive(path.join(dir_path_content, file), template_path, path.join(dest_dir_path, file))


def generate_page(from_path, temlpate_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {temlpate_path}")

    # try:
    with open(from_path, encoding="utf-8") as f:
        read_data = f.read()
        title = extract_title(read_data)
        html = markdown_to_htmlnode(read_data).to_html()

        with open(temlpate_path) as template_file:
            template_data = template_file.read()
            with_content = template_data.replace("{{ Content }}", html)
            with_content_and_title = with_content.replace("{{ Title }}", title)

            with open(dest_path.replace(".md", ".html"), 'w') as dest_file:
                dest_file.write(with_content_and_title)
                
    # except:
    #     print(f"An error occurred while reading {from_path}")