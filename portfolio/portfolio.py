import reflex as rx

from portfolio.pages.index import index
from portfolio.pages.works import works
from portfolio.pages.projects.projects import projects
from portfolio.pages.projects.myhomecloud import my_home_cloud
from portfolio.pages.projects.portfolio_reflex import portfolio_reflex
from portfolio.pages.projects.cloudy import cloudy
from portfolio.pages.projects.sqly import sqly
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
app.add_page(my_home_cloud)
app.add_page(portfolio_reflex)
app.add_page(cloudy)
app.add_page(sqly)
app.add_page(contact)
app.compile()
