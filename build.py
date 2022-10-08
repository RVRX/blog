import os
import markdown


def piece_together(body, post_list):
    prependee = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link href="/css/glow-style-terminal.css" rel="stylesheet">

    <title>RVRX</title>
</head>
<body class="body">
<main class="main">
<header><span style="color: #89982e">RVRX</span>@<span class="page-host">localhost</span> <span style="color: #89982e" id="page-path">~/blog</span> (<span style="color: #6d71be;">master</span>) $ <span style="color: #76b8cb"><a href="https://github.com/charmbracelet/glow#glow" target="_blank">glow</a> <span id="page-name">index.md</span></span></header>
<div class="generated-content">
"""

    appendee = """
</div>
</main>
<div class="sidebar">
    <div id="sidebar-shell">
        Last login: Fri Oct  7 21:49:25 on ttys000<br>
        <span style="color: #89982e">RVRX</span>@<span class="page-host">github.io</span> <span style="color: #89982e">~/sidebar</span> (<span style="color: #6d71be;">master</span>) $ <span style="color: #76b8cb">ls -a</span>
        <ul>"""

    appendee_the_second = """
        </ul>
    </div>
</div>
<footer class="footer">
    <div id="footer-shell">
        <span style="color: #89982e">RVRX</span>@<span class="page-host">github.io</span> <span style="color: #89982e">~/footer</span> (<span style="color: #6d71be;">master</span>) $ <span style="color: #76b8cb">cat footer.txt</span>
    </div>
    <div id="main-footer">
        <a href="https://blog.rvrx.dev">Home</a> | <a href="/about">About Blog</a>
    </div>
</footer>
<script src="/js/glow-style-terminal-styler.js"></script>
</body>
</html>
"""

    return prependee + body + appendee + post_list + appendee_the_second


def generate_html_from_file(path_to_file, post_list):
    with open(path_to_file, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    html = markdown.markdown(text)
    with open(path_to_file.split(".")[0] + ".html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(piece_together(html, post_list=post_list))


# BUILD POST FILES
with os.scandir('posts/') as entries:
    # assemble list of posts
    post_list = ""
    for entry in entries:
        if entry.name.endswith(".md"):
            substr = entry.name.split(".")[0]
            post_list += '\n            <li><a href=/posts/' + substr + ".html" + '>' + substr.replace("-", " ").title() + '</a></li>'

with os.scandir('posts/') as entries:
    for entry in entries:
        if entry.name.endswith(".md"):
            print('[build]: ' + entry.name)
            generate_html_from_file("posts/" + entry.name, post_list=post_list)

# BUILD INDEX FILE
print('[build]: index.md')
generate_html_from_file("index.md", post_list=post_list)