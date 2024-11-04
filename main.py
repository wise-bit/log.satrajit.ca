from fasthtml.common import *

# local
from components.home import fetch_home
from components.entry import fetch_entry

hdrs = (MarkdownJS(), HighlightJS(langs=['python', 'javascript', 'html', 'css']), )
app, rt = fast_app(hdrs=hdrs)


@rt('/')
def home():
  home = fetch_home()
  return home


@rt('/entry/{filename}')
def show_entry(filename: str):
  return fetch_entry(filename)


serve()
