import os
import markdown
from datetime import datetime
from os.path import getctime



def piece_together(body, post_list, page_title="RVRX", page_description="", page_image="https://blog.rvrx.dev/img/about/terminal-example.png"):
    prependee = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Dev Blog of Cole Manning (RVRX)">
    <meta name="keywords" content="Cole Manning, Blog, RVRX, devblog, dev-blog, WPI, Worcester Polytechnic Institute">"""

    og_title = f'<meta property="og:title" content="{page_title}">'
    og_sitename = f'<meta property="og:site_name" content="RVRX.">'
    og_url = f'<meta property="og:url" content=https://blog.rvrx.dev>'
    og_desc = f'<meta property="og:description" content="{page_description}">'
    og_type = '<meta property="og:type" content="article">'
    og_image = f'<meta property="og:image" content={page_image}>'
    open_graph = f'\n\t{og_title}\n\t{og_sitename}\n\t{og_url}\n\t{og_desc}\n\t{og_type}\n\t{og_image}'

    post_prependee = """
    <link href="/css/glow-style-terminal.css" rel="stylesheet">
    <title>RVRX</title>
</head>
<body class="body">
<main class="main">
<header><a href="/"><span style="color: #89982e">RVRX</span>@<span class="page-host">localhost</span> <span style="color: #89982e" id="page-path">~/blog</span> (<span style="color: #6d71be;">master</span>)</a> $ <span style="color: #76b8cb"><a href="https://github.com/charmbracelet/glow#glow" target="_blank">glow</a> <span id="page-name">index.md</span></span></header>
<div class="generated-content">
"""

    appendee = """
</div>
</main>
<div class="sidebar">
    <div id="sidebar-shell">
        <span style="color: #89982e">~/posts</span> $ <span style="color: #76b8cb">ls -l</span>
        <div id="post-listing-ol">"""

    appendee_the_second = """
        </div>
        <aside id="heading-listing">
            <span style="color: #89982e">~</span> $ <span style="color: #76b8cb">cd ../contents</span><br>
            <span style="color: #89982e">~/contents</span> $ <span style="color: #76b8cb">cat headings.txt</span>
            <div id="heading-listing-paragraph">Unable to render table of contents without JS, sorry!</div>
        </aside>
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
<script src="/js/table-of-contents.js"></script>
</body>
</html>
"""

    return prependee + open_graph + post_prependee + body + appendee + post_list + appendee_the_second


def generate_html_from_file(path_to_file, post_list):
    with open(path_to_file, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    html = markdown.markdown(text)
    path_no_ext = path_to_file.split(".")[0]
    with open(path_no_ext + ".html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(piece_together(html, post_list=post_list, page_title=path_no_ext.split("/")[-1].replace("-", " ").title()))


# BUILD POST FILES
with os.scandir('posts/') as entries:
    # assemble list of posts
    post_list = ""
    for entry in entries:
        if entry.name.endswith(".md"):
            substr = entry.name.split(".")[0]
            post_list += '\n            <p>rvrx <span class="date">' + datetime.fromtimestamp(getctime(entry)).strftime("%d  %b %H:%M") + '</span><br><a href=/posts/' + substr + ".html" + '>' + substr.replace("-", " ").title() + '</a></p>'

with os.scandir('posts/') as entries:
    for entry in entries:
        if entry.name.endswith(".md"):
            print('[build]: ' + entry.name)
            generate_html_from_file("posts/" + entry.name, post_list=post_list)

# BUILD INDEX FILE
print('[build]: index.md')
generate_html_from_file("index.md", post_list=post_list)

# BUILD ABOUT FILE
print('[build]: about.md')
generate_html_from_file("about.md", post_list=post_list)
