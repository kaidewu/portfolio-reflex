import requests

def test_connection_portfolio_index_page():
    response = requests.get("http://localhost:3000/")
    assert response.status_code == 200

def test_connection_portfolio_works_page():
    response = requests.get("http://localhost:3000/works")
    assert response.status_code == 200

def test_connection_portfolio_contact_page():
    response = requests.get("http://localhost:3000/contact")
    assert response.status_code == 200

def test_connection_portfolio_source_page():
    response = requests.get("https://github.com/kaidewu/portfolio-reflex")
    assert response.status_code == 200