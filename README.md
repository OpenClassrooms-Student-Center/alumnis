Page presenting our alumni to the community.

# Workflow presentation

# Commands
`pelican content -r`: convert files into static content and regenerate them when new content is added.
`python -m http.server`: launch server. Address: localhost:8000

# Run the following before anything
pip install ghp-import
pip install pelican-md-metayaml

To push on gh-pages
pelican
ghp-import output
git push origin gh-pages

http://docs.getpelican.com/en/3.0/tips.html