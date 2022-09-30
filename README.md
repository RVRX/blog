# Blog
This blog is set up via github actions to automatically convert markdown files into html files.

Actions Stack:
  - [**Create File**](https://github.com/marketplace/actions/create-file) is used to create a list of all html files in the `posts/` directory.
  - [**Git Auto Commit**](https://github.com/marketplace/actions/git-auto-commit) is used to commit all changes made by
  - [**Markdown-HTML**](https://github.com/marketplace/actions/markdown-html) converts index.md along with all the md files in the `posts` dir into HTML files with an included style block from `style.css`
