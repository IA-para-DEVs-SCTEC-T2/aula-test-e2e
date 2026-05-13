import re
from pathlib import Path
from playwright.sync_api import Page, expect


BASE_URL = Path(__file__).parent.resolve().as_uri()
LOGIN_URL = f"{BASE_URL}/login.html"


def test_login_flow_success(page: Page) -> None:
    page.goto(LOGIN_URL)

    page.fill("#email", "user@test.com")
    page.fill("#senha", "123456")
    page.click("#btn-login")

    expect(page).to_have_url(re.compile(r"dashboard\.html"))
    expect(page.locator("#btn-logout")).to_be_visible()
