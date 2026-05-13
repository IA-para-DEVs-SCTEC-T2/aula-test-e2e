# Prompt utilizado para gerar o teste

Atue como um Engenheiro de QA especializado em Automação.

**Objetivo:** Gere um script de teste funcional E2E utilizando Python, Pytest e Playwright.

## Configuração do Arquivo

- O código deve ser salvo em um arquivo dentro da pasta `teste grupo 6/`.
- Nome do arquivo seguindo a convenção do pytest: `test_login_flow.py`.

## Contexto da Aplicação

- **URL Inicial:** `login.html` (considere um caminho relativo ou localhost).
- **Seletores da tela de login:** `#email`, `#senha`, `#btn-login`.
- **Destino após login com sucesso:** `dashboard.html`.
- **Elemento esperado no Dashboard:** `#btn-logout` (deve estar visível).

## Cenário de Teste

1. O usuário navega até a página de login.
2. Preenche o campo `#email` com `"user@test.com"`.
3. Preenche o campo `#senha` com `"123456"`.
4. Clica no botão `#btn-login`.
5. Valida se a URL final contém `dashboard.html` usando `expect(page).to_have_url()`.
6. Valida se o botão `#btn-logout` está visível usando `expect(locator).to_be_visible()`.

## Requisitos Técnicos

- Utilize a fixture `page` nativa do `pytest-playwright`.
- O código deve seguir as normas da **PEP 8**.
- Não forneça explicações, gere apenas o bloco de código completo e pronto para execução.
