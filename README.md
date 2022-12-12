# How to use
Production building is done through github actions. See `.github/workflows/generate-html.yml`.

Locally building can be done with `python3 ./build.py`

## Adding new posts
add new `post-name.md` file to the `posts/` dir. This will create a post titled "Post Name".

Images should (but are not required to, just be aware of production scope) go in the `img/post-name` directory.
Reference them in the MD as `../img/post-name/image-name.png`

New posts must be made on the `develop` branch, as this is where GitHub Actions runs its updates. PR the branch to master and confirm all changes look good.
