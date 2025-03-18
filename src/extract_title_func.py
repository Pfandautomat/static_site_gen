from markdown_to_html import markdown_to_html_node
from os import path, listdir, mkdir
from shutil import copy, rmtree
import os


def extract_title(markdown):

    lines = markdown.strip().split('\n')
    header = ""

    for i, line in enumerate(lines):

        if line.strip().startswith('# '):
              return line.strip()[2:]

    
    raise Exception("no H1 Header")



def generate_page(from_path, template_path, dest_path,basepath="/"): 
     
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
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')


    with open(dest_path, 'w', encoding='utf-8') as output_file:
        output_file.write(full_html)
    
    print(f"Successfully generated {dest_path}")



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    # Print debug information to see what's happening
    print(f"Processing directory: {dir_path_content}")
    
    current_objects = listdir(dir_path_content)

    for obj in current_objects:
        source_path = path.join(dir_path_content, obj)
        
        if path.isfile(source_path):
            if obj.endswith(".md"):
                # Special case for index.md files in subdirectories
                if obj == "index.md" and dir_path_content != "content" and not dir_path_content.endswith("/content"):
                    # Get the directory name from the path
                    dir_name = path.basename(dir_path_content)
                    # Generate HTML in the parent directory with the directory name
                    parent_dir = path.dirname(dest_dir_path)
                    html_path = path.join(parent_dir, f"{dir_name}.html")
                    print(f"Clean URL: Converting {source_path} to {html_path}")
                else:
                    # Regular case - standard processing
                    html_file = obj.replace(".md", ".html") 
                    html_path = path.join(dest_dir_path, html_file)
                    print(f"Converting {source_path} to {html_path}")
                
                # Generate the HTML file
                generate_page(source_path, template_path, html_path, basepath)
        elif path.isdir(source_path):
            # Create the directory if it doesn't exist
            dest_path = path.join(dest_dir_path, obj)
            if not path.exists(dest_path):
                mkdir(dest_path)
                print(f"Created directory: {dest_path}")
            
            # Recurse into the directory
            generate_pages_recursive(source_path, template_path, dest_path, basepath)



