from textnode import *
from os import path, listdir, mkdir
from shutil import copy, rmtree
import os

print("hello world")

def copy_function(copy_from, copy_to):
    # Adjust relative paths to work from the project root
    if not path.exists(copy_to):
        mkdir(copy_to)
    elif copy_to == "../public": 
        rmtree(copy_to)
        mkdir(copy_to)

    current_objects = listdir(copy_from)

    for object in current_objects:
        source_path = path.join(copy_from, object)
        dest_path = path.join(copy_to, object)

        if path.isfile(source_path):
            copy(source_path, dest_path)
        else:
            if not path.exists(dest_path):
                mkdir(dest_path)
            
            copy_function(source_path, dest_path)

def main():
    test_object = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(test_object)
    
    # Get the current working directory (should be the project root when run from main.sh)
    current_dir = os.getcwd()
    
    # Copy static files to public directory with correct relative paths
    if path.basename(current_dir) == "src":
        # If run directly from src directory
        copy_function("../static", "../public")
    else:
        # If run from project root (via main.sh)
        copy_function("static", "public")

main()