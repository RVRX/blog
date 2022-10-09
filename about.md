# About This Site

This site is styled to mimic my local dev terminal:

- It mimics prompt of my [Fish shell](https://fishshell.com/),
- Similar [iTerm](https://iterm2.com/) terminal theme
- The same `tmux` pane borders, and most importantly:
- The same [kinda] colors as [glow](https://github.com/charmbracelet/glow)'s default markdown theme (hence the shell line at the top of this page).

![Image of my local dev environment](/img/about/terminal-example.png)

## How I Use it
This site is hosted at[](https://github.com/RVRX/blog) via GitHub Pages.
GitHub Actions is set up to automatically generate `.html` files from the `.md` files I create.
This is done via the python package `markdown` – running in a custom script on every push to the `develop` branch.
Local previewing can be done just by running `python3 build.py`, or even easier with `glow <md_filename>`.

## CREDIT
Once again, credit to the developers of [glow](https://github.com/charmbracelet/glow) for the inspiration (and for the GitHub CLI for introducing me to the project via `gh repo view`).

Also, I got lazy when making the table of contents, so that code is ripped from [this](https://webdevtrick.com/dynamic-table-of-contents/) Webdevtrick tutorial.

**Unless otherwise mentioned, the rest of the content, ideas, and code on this site are mine own ;)**
