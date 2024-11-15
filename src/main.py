from os import path, mkdir, listdir
from shutil import copy, rmtree
from generate_page import generate_page

def main():
    if path.exists('public'):
        print("deleting existing public directory")
        rmtree('public')

    copy_tree("static", "public") 

    generate_page("content/index.md", "template.html", "public/index.html")

def copy_tree(src, dst):
    if path.isfile(src):
        copy(src, dst)
        print(f"file copied from: {src} \n copied to: {dst}")
    else:
        
        if not path.exists(dst):
            mkdir(dst)

        for file in listdir(src):
            copy_tree(path.join(src, file), path.join(dst, file))


main()