from pathlib import Path
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def login_path():
    return Path(__file__).parent / "login.html"


@pytest.fixture
def dashboard_path():
    return Path(__file__).parent / "dashboard.html"


def test_login_valido_redireciona_para_dashboard(page: Page, login_path, dashboard_path):
    page.goto(login_path.as_uri())
    page.fill("#email", "user@test.com")
    page.fill("#senha", "123456")
    page.click("#btn-login")
    expect(page).to_have_url(dashboard_path.as_uri())
    expect(page.locator("#btn-logout")).to_be_visible()


def test_mensagem_erro_credenciais_invalidas(page: Page, login_path):
    page.goto(login_path.as_uri())
    page.fill("#email", "invalido@test.com")
    page.fill("#senha", "senhaerrada")
    page.click("#btn-login")
    expect(page.locator("#mensagem")).to_contain_text("Credenciais inválidas")
    expect(page).to_have_url(login_path.as_uri())


def test_welcome_message_visivel_apos_login(page: Page, login_path, dashboard_path):
    page.goto(login_path.as_uri())
    page.fill("#email", "user@test.com")
    page.fill("#senha", "123456")
    page.click("#btn-login")
    expect(page.locator("#welcome-message")).to_be_visible()
    expect(page.locator("#welcome-message")).to_contain_text("Usuário autenticado com sucesso.")
