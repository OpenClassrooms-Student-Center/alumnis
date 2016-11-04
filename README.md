Page presenting our alumni to the community.

# Launching it locally
Set up a virtual environment with Python 3.
Run `pip install -r requirements.txt`
Generate files: `pelican -r`
Launch a server: `python -m http.server`

# To push on gh-pages
pelican
ghp-import output
git push origin gh-pages

# Useful links
http://docs.getpelican.com/en/3.0/tips.html
http://blog.thomasemmerling.de/automatic-pelican-publishing-on-github-pages-via-travisci.html
https://gist.github.com/domenic/ec8b0fc8ab45f39403dd