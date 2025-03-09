

def markdown_to_blocks(markdown):

    parts = markdown.split("\n\n")

    parts = list(map(str.strip, parts))

    parts = list(filter(lambda part: part != "" ,parts))

    return parts