from textnode import *
from os import path, listdir, mkdir,getcwd
from shutil import copy, rmtree
from extract_title_func import generate_pages_recursive, generate_page
import sys




def copy_function(copy_from, copy_to):
    # Adjust relative paths to work from the project root
    if not path.exists(copy_to):
        mkdir(copy_to)
    elif copy_to == "../docs": 
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


    basepath = "/"
    if len(sys.argv) >1:
        basepath = sys.argv[1]
        if not basepath.startswith("/"):
            basepath = "/" + basepath
        if not basepath.endswith("/"):
            basepath = basepath  + "/"

    # Get the current working directory (should be the project root when run from main.sh)
    current_dir = getcwd()
    
    # Copy static files to public directory with correct relative paths
    if path.basename(current_dir) == "src":
        # If run directly from src directory
        copy_function("../static", "../docs")
    else:
        # If run from project root (via main.sh)
        copy_function("static", "docs")

    current_dir = getcwd()

    if path.basename(current_dir) == "src":
        # If run directly from src directory
        copy_function("../static", "../docs")
        content_dir = "../content"
        template_path = "../template.html"
        public_dir = "../docs"
    else:
        # If run from project root (via main.sh)
        copy_function("static", "docs")
        content_dir = "content" 
        template_path = "template.html"
        public_dir = "docs"
    
        
    generate_pages_recursive(content_dir,template_path,public_dir)






main()