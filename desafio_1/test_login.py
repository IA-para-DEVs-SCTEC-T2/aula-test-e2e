import os
import re
from playwright.sync_api import Page, expect

# Caminho absoluto para login.html usando protocolo file://
LOGIN_URL = "file://" + os.path.abspath(
    os.path.join(os.path.dirname(__file__), "login.html")
)


def test_login_sucesso(page: Page):
    # 1. Abre a página de login via protocolo file://
    page.goto(LOGIN_URL)

    # 2. Preenche o campo de email com credenciais válidas
    page.fill("#email", "user@test.com")

    # 3. Preenche o campo de senha
    page.fill("#senha", "123456")

    # 4. Clica no botão de login
    page.click("#btn-login")

    # 5. Valida que a URL contém dashboard.html após redirecionamento
    expect(page).to_have_url(re.compile(r"dashboard\.html"))

    # 6. Valida que o elemento de boas-vindas está visível
    welcome = page.locator("#welcome-message")
    expect(welcome).to_be_visible()

    # 7. Valida o texto exato do elemento de boas-vindas
    expect(welcome).to_have_text("Usuário autenticado com sucesso.")
