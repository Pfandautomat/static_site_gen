import re 

def extract_markdown_images(text):

    extract = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)


    return extract


def extract_markdown_links(text):

    extract = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

    return extract


