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
from portfolio.pages import page404

from portfolio.state.state import State


# Add state and page to the app.
app = rx.App(
    state=State,
    stylesheets={
        "/styles.css"
    }
    )
app.add_page(index, title="Portfolio | Kaide Wu", image="/favicon.ico")
app.add_page(works, title="Portfolio | Kaide Wu", image="/favicon.ico")
app.add_page(projects, title="Portfolio | Kaide Wu", image="/favicon.ico")
app.add_page(my_home_cloud, title="Portfolio | Kaide Wu", image="/favicon.ico")
app.add_page(portfolio_reflex, title="Portfolio | Kaide Wu", image="/favicon.ico")
app.add_page(portfolio_reflex_github_api, title="Portfolio | Kaide Wu", image="/favicon.ico")
app.add_page(cloudy, title="Portfolio | Kaide Wu", image="/favicon.ico")
app.add_page(sqly, title="Portfolio | Kaide Wu", image="/favicon.ico")
app.add_page(contact, title="Portfolio | Kaide Wu", image="/favicon.ico")
app.add_custom_404_page(page404.index)
app.compile()
