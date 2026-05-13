from pathlib import Path
from playwright.sync_api import sync_playwright, expect


def test_login_flow():
    """Teste E2E do fluxo de login com redirecionamento para dashboard"""
    
    # Definir caminhos dos arquivos HTML
    project_root = Path(__file__).parent
    login_path = project_root / "login.html"
    dashboard_path = project_root / "dashboard.html"
    
    # Converter para URIs
    login_uri = login_path.as_uri()
    dashboard_uri = dashboard_path.as_uri()
    
    # Dados de entrada
    email = "user@test.com"
    senha = "123456"
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # 1. Abrir a página de login
        page.goto(login_uri)
        
        # 2. Preencher email
        page.fill("#email", email)
        
        # 3. Preencher senha
        page.fill("#senha", senha)
        
        # 4. Clicar no botão de login
        page.click("#btn-login")
        
        # 5. Validar redirecionamento para dashboard
        expect(page).to_have_url(dashboard_uri)
        
        # 6. Validar que o botão de logout está visível
        expect(page.locator("#btn-logout")).to_be_visible()
        
        browser.close()
