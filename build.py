import os
import markdown
from datetime import datetime
from os.path import getctime



def piece_together(body, post_list, page_title="RVRX", page_description="", page_image="https://blog.rvrx.dev/img/about/terminal-example.png"):

    file_body = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Dev Blog of Cole Manning (RVRX)">
    <meta name="keywords" content="Cole Manning, Blog, RVRX, devblog, dev-blog, WPI, Worcester Polytechnic Institute">
    
    <meta property="og:title" content="{page_title}">
    <meta property="og:site_name" content="RVRX.">
    <meta property="og:url" content=https://blog.rvrx.dev>
    <meta property="og:description" content="{page_description}">
    <meta property="og:type" content="article">
    <meta property="og:image" content={page_image}>
    
    <link href="/css/glow-style-terminal.css" rel="stylesheet">
    <title>{page_title}</title>
</head>

<body class="body">
<main class="main">
<header><a href="/"><span style="color: #89982e">RVRX</span>@<span class="page-host">localhost</span> <span style="color: #89982e" id="page-path">~/blog</span> (<span style="color: #6d71be;">master</span>)</a> $ <span style="color: #76b8cb"><a href="https://github.com/charmbracelet/glow#glow" target="_blank">glow</a> <span id="page-name">index.md</span></span></header>
<div class="generated-content">
{body}
</div>
</main>
<div class="sidebar">
    <div id="sidebar-shell">
        <span style="color: #89982e">~/posts</span> $ <span style="color: #76b8cb">ls -l</span>
        <div id="post-listing-ol">
        {post_list}
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

    return file_body


def generate_html_from_file(path_to_file, post_list):
    # Create HTML from MD
    with open(path_to_file, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    html = markdown.markdown(text)
    # write HTML to file
    path_no_ext = path_to_file.split(".")[0]
    with open(path_no_ext + ".html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        filename = path_no_ext.split("/")[-1]  # get filename from path
        filename_no_ext = filename.split(".")[0]  # remove extension
        filename_as_title = filename_no_ext.replace("-", " ").title()  # turn dashes to spaces, use title-case
        output_file.write(piece_together(html, post_list=post_list, page_title=filename_as_title))


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
