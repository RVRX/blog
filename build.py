import os
import markdown


def piece_together(body):
    prependee = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link href="/css/glow-style-terminal.css" rel="stylesheet">

    <title>RVRX</title>
</head>
<body>
<header><span style="color: #89982e">RVRX</span>@<span id="page-host">localhost</span> <span style="color: #89982e" id="page-path">~/blog</span> (<span style="color: #6d71be;">master</span>) $ <span style="color: #76b8cb"><a href="https://github.com/charmbracelet/glow#glow" target="_blank">glow</a> <span id="page-name">index.md</span></span></header>
"""

    appendee = """
<script src="/js/glow-style-terminal-styler.js"></script>
</body>
</html>
"""

    return prependee + body + appendee


def generate_html_from_file(path_to_file):
    with open(path_to_file, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    html = markdown.markdown(text)
    with open(path_to_file.split(".")[0] + ".html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(piece_together(html))


# BUILD INDEX FILE
print('[build]: index.md')
generate_html_from_file("index.md")
# BUILD POST FILES
with os.scandir('posts/') as entries:
    for entry in entries:
        print('[build]: ' + entry.name)
        generate_html_from_file("posts/" + entry.name)
