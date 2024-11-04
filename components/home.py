from fasthtml.common import *

# local
from variables import WEBSITE_TITLE, FAVICON_PATH, BLOGS_FOLDER
from functions.loader import load_blog_entries
from styles.global_style import global_style


def fetch_home():
  entries = load_blog_entries(BLOGS_FOLDER)

  return Html(
    Head(
      global_style,
      Title(WEBSITE_TITLE),
      Link(rel="icon", href=FAVICON_PATH, type="image/x-icon")
    ),
    Body(
      Div(
        H2("welcome to sat's logs"),
        P(
          "i am satrajit (sat) chatterjee, a software engineer from canada working as an ai developer. ",
          "you can find more about me at:",
        ),
        H3(A("satrajit.ca", href="https://satrajit.ca")),
        P(I("this website is made using fasthtml (+ fastapi)")),
        Div(
          *[
            Div(
              Div("-> (", entry['date'], ") ",),
              Div(
                A(
                  H4(entry['title']), 
                  href=f"/entry/{entry['filename']}"
                )
              )
            )
            for entry in entries
          ], cls="list-entries"
        ), cls="full-container"
      )
    )
  )
