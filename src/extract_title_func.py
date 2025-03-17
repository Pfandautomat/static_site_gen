from markdown_to_html import markdown_to_html_node


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
