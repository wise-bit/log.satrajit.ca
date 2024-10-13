from fasthtml.common import *

# local
from components.home import fetch_home
from components.entry import fetch_entry

app, rt = fast_app()


@rt('/')
def home():
  home = fetch_home()
  return home


@rt('/entry/{filename}')
def show_entry(filename: str):
  return fetch_entry(filename)


serve()
