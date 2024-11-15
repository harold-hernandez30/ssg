from os import path, mkdir, listdir
from shutil import copy, rmtree
import sys

def main():
    if path.exists('public'):
        print("deleting existing public directory")
        rmtree('public')

    copy_tree("static", "public") 

def copy_tree(src, dst):
    print(f"src: {src}")
    print(f"dst: {dst}")
    if path.isfile(src):
        copy(src, dst)
        print(f"file copied from: {src} \n copied to: {dst}")
    else:
        
        if not path.exists(dst):
            print(f"dst_directory to be created: {dst}")
            mkdir(dst)

        for file in listdir(src):
            copy_tree(path.join(src, file), path.join(dst, file))


main()