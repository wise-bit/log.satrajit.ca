from fasthtml.common import *
import markdown

# local
from variables import WEBSITE_TITLE, FAVICON_PATH, BLOGS_FOLDER
from styles.global_style import global_style


def fetch_entry(filename: str):
  try:
    with open(os.path.join(BLOGS_FOLDER, filename + ".md"), 'r') as f:
      content = f.read()

    title = " ".join(filename.split('-')[1:]).replace('_', ' ').replace('.md', '')
    html_content = markdown.markdown(content)

    return Html(
      Head(
        global_style,
        Title(WEBSITE_TITLE),
        Link(rel="icon", href=f"../{FAVICON_PATH}", type="image/x-icon")
      ),
      Body(
        Div(
          Div(
            A(I("<- back to home"), href="/"),
            Div(Class="vertspace"),
            H1(title),
            Div(NotStr(html_content))
          ), cls="full-container"
        )
      )
    )
  except FileNotFoundError:
    return Html(
      Head(
        global_style,
        Title(WEBSITE_TITLE),
        Link(rel="icon", href=f"../{FAVICON_PATH}", type="image/x-icon")
      ),
      Body(
        Div(
          P("error 404:"),
          P("where were you trying to go?")
        )
      )
    )
