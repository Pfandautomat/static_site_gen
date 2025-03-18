from markdown_to_html import markdown_to_html_node
from os import path, listdir, mkdir
from shutil import copy, rmtree
from extract_title_func import generate_page
import os


def extract_title(markdown):

    lines = markdown.strip().split('\n')
    header = ""

    for i, line in enumerate(lines):

        if line.strip().startswith('# '):
              return line.strip()[2:]

    
    raise Exception("no H1 Header")



def generate_page(from_path, template_path, dest_path): 
     
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r', encoding='utf-8') as markdown_file:
     markdown_content = markdown_file.read()

    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    title = extract_title(markdown_content)

    full_html = template_content.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)

    with open(dest_path, 'w', encoding='utf-8') as output_file:
        output_file.write(full_html)
    
    print(f"Successfully generated {dest_path}")



def  generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    current_objects = listdir(dir_path_content)

    for obj in current_objects:

        source_path = path.join(dir_path_content, obj)
        dest_path = path.join(dest_dir_path, obj)

        if path.isfile(source_path):
            generate_page(source_path,template_path,dest_path)
        else:
            if not path.exists(dest_path):
                mkdir(dest_path)
            
            generate_pages_recursive(source_path,template_path,dest_path)




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
