import os
from fasthtml.common import *

# import logging
# logging.basicConfig(level=logging.DEBUG)

BLOGS_FOLDER = './blogs/'

app, rt = fast_app()


global_style = Style(
  # align-items: center;
  """
  body {
    background-color: #000;
    color: #EEE;
    font-family: monospace;
    display: flex;
    justify-content: center;
    margin: 100px;
    font-size: 16px;
    line-height: 1.5;
  }
  div {
    width: 500px;
    padding: 20px;
    text-align: left;     
  }
  h2, h3 {
      color: #DDD;
  }
  a {
    color: #EEE;
  }
  .vertspace {
    margin: 14px 0;
  }
  """
)


def load_blog_entries():
  entries = []
  for filename in sorted(os.listdir(BLOGS_FOLDER), reverse=True):
    if filename.endswith(".txt"):
      name_parts = filename.split('-')
      date, title = name_parts[0], name_parts[1:]

      date = "".join(date).replace('_', '-')
      title = " ".join(title).replace('_', ' ').replace('.txt', '')
      filename_clean = filename.replace('.txt', '')

      entries.append({'date': date, 'title': title, 'filename': filename_clean})

  return entries


@rt('/')
def home():
  entries = load_blog_entries()
  return Html(
    Head(global_style),
    Body(
      Div(
        H2("welcome to sat's logs"),
        P(
          "i am satrajit chatterjee (sat) a developer from canada working as an ai developer. ",
          "you can find more about me at ",
          A("satrajit.ca", href="https://satrajit.ca")
        ),
        P(I("this website is made using fasthtml (+ fastapi)")),
        Div(
          *[
            P(
              "-- (",
              entry['date'],
              ") ",
              A(entry['title'], href=f"/entry/{entry['filename']}")
            )
            for entry in entries
          ]
        )
      )
    )
  )


def _show_entry(title, content):
  return Html(
    Head(global_style),
    Body(
      Div(
        A(I("<- back to home"), href="/"),
        Div(Class="vertspace"),
        H1(title),
        P(content),
      )
    )
  )


@rt('/entry/{filename}')
def fetch_entry(filename: str):
  try:
    with open(os.path.join(BLOGS_FOLDER, filename + ".txt"), 'r') as f:
      content = f.read()
    title = " ".join(filename.split('-')[1:]).replace('_', ' ').replace('.txt', '')
    return _show_entry(title, content)
  except FileNotFoundError:
    return P("Blog post not found."), 404


# Start the server
serve()
