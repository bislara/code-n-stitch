from markdownify import markdownify

file = open("index.html", "r").read()
html = markdownify(file, heading_style="ATX")

print(html)
