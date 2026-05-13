from pathlib import Path
from playwright.sync_api import Page, expect


def test_login_redireciona_para_dashboard(page: Page):
    base = Path(__file__).parent

    # Abre a página de login
    page.goto((base / "login.html").as_uri())

    # Preenche as credenciais
    page.fill("#email", "user@test.com")
    page.fill("#senha", "123456")

    # Clica no botão Entrar
    page.click("#btn-login")

    # Valida redirecionamento para dashboard.html
    expect(page).to_have_url((base / "dashboard.html").as_uri())
