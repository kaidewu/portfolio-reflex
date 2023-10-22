import reflex as rx

from portfolio.pages.index import index
from portfolio.pages.works import works
from portfolio.pages.projects import projects
from portfolio.pages.contact import contact

from portfolio.state.state import State


# Add state and page to the app.
app = rx.App(
    state=State,
    stylesheets={
        "/project_style.css"
    }
    )
app.add_page(index)
app.add_page(works)
app.add_page(projects)
app.add_page(contact)
app.compile()
