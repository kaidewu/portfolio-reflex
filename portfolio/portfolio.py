import reflex as rx

from portfolio.pages.index import index
from portfolio.pages.works import works
from portfolio.pages.projects.projects import projects
from portfolio.pages.projects.myhomecloud import my_home_cloud
from portfolio.pages.projects.portfolio_reflex import portfolio_reflex
from portfolio.pages.projects.portfolio_reflex_github_api import portfolio_reflex_github_api
from portfolio.pages.projects.cloudy import cloudy
from portfolio.pages.projects.sqly import sqly
from portfolio.pages.contact import contact
from portfolio.pages.projects import repository_page
from portfolio.pages import page404

# Add state and page to the app.
app = rx.App(
    stylesheets={
        "/styles.css"
    }
    )
app.add_page(index)
app.add_page(works)
app.add_page(contact)
app.add_page(repository_page)
app.add_custom_404_page(page404.index)
app.compile()
