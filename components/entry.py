from fasthtml.common import *

# local
from variables import WEBSITE_TITLE, FAVICON_PATH, BLOGS_FOLDER
from styles.global_style import global_style


def fetch_entry(filename: str):
  try:
    with open(os.path.join(BLOGS_FOLDER, filename + ".txt"), 'r') as f:
      content = f.read()
    title = " ".join(filename.split('-')[1:]).replace('_', ' ').replace('.txt', '')

    return Html(
      Head(
        global_style,
        Title(WEBSITE_TITLE),
        Link(rel="icon", href=f"../{FAVICON_PATH}", type="image/x-icon")
      ),
      Body(
        Div(
          A(I("<- back to home"), href="/"),
          Div(Class="vertspace"),
          H1(title),
          P(content),
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
        P("where were you trying to go?")
      )
    )
