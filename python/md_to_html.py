import markdown
from bs4 import BeautifulSoup


def markdown_to_html_with_nav(md_text):
    # Convert markdown to HTML
    html_body = markdown.markdown(md_text, extensions=["toc", "fenced_code"])

    # Parse HTML to extract headings
    soup = BeautifulSoup(html_body, "html.parser")

    toc = "<ul>"
    for tag in soup.find_all(["h1", "h2", "h3"]):
        # Add an ID for linking
        if not tag.has_attr("id"):
            tag_id = tag.text.replace(" ", "-").lower()
            tag["id"] = tag_id
        else:
            tag_id = tag["id"]
        toc += f'<li style="margin-left:{(int(tag.name[1]) - 1) * 20}px;"><a href="#{tag_id}">{tag.text}</a></li>'
    toc += "</ul>"

    # Combine nav + content
    full_html = f"""
    <html>
    <head>
    <style>
        body {{ display: flex; font-family: sans-serif; }}
        nav {{ width: 250px; padding: 1em; border-right: 1px solid #ccc; }}
        main {{ padding: 1em; flex-grow: 1; }}
        li {{ list-style: none; }}
    </style>
    </head>
    <body>
        <nav>{toc}</nav>
        <main>{str(soup)}</main>
    </body>
    </html>
    """
    return full_html


md = open("../result/test.md", "r")
md = md.read()

html = open("index.html", "w")
html.write(markdown_to_html_with_nav(md))
