from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def fechar_modal(driver):
    try:
        modal_container = WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.CLASS_NAME, "chakra-modal__content-container"))
        )

        if modal_container.is_displayed():
            actions = ActionChains(driver)
            actions.move_to_element_with_offset(modal_container, -10, -10)
            actions.click()
            actions.perform()

    except Exception as e:
        pass

def realizar_cadastro(driver, nome, email, senha, confirmar_senha):
    try:
        # Fecha modal
        fechar_modal(driver)

        # Seleciona "Entrar"
        button_entrar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".chakra-button.css-ovdjqs[data-cy='btn-trigger-profile']"))
        )
        button_entrar.click()
        time.sleep(0.5)

        # Seleciona "Criar conta"
        button_criar_conta = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".chakra-button.css-1f4izxt[data-cy='login-createAccount']"))
        )
        button_criar_conta.click()

        # Preenche cadastro
        name_input = driver.find_element(By.ID, "name")
        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "password")
        confirm_password_input = driver.find_element(By.ID, "confirmPassword")

        if nome:
            name_input.send_keys(nome)

        if email:
            email_input.send_keys(email)

        if senha:
            password_input.send_keys(senha)

        if confirmar_senha:
            confirm_password_input.send_keys(confirmar_senha)

        # Seleciona "Criar conta"
        button_criar_conta_final = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".chakra-button.css-ncw165[data-cy='register-submit']"))
        )
        button_criar_conta_final.click()
        time.sleep(3)

    except Exception as e:
        print("Erro durante o cadastro:", e)

if __name__ == "__main__":
    # Instanciando Chrome driver
    chrome_options = webdriver.ChromeOptions()
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    chrome_options.add_argument(f"executable_path={PATH}")
    driver = webdriver.Chrome(options=chrome_options)


    # Abrir site do case
    driver.get("https://www.kasa.live/")

    #INICIANDO TESTES:
    
# 1 Sem nome
realizar_cadastro(driver, "", "teste@teste.com", "senha123", "senha123")

# 2 Sem email
realizar_cadastro(driver, "Testezeiro", "", "senha123", "senha123")

# 3 Sem senha
realizar_cadastro(driver, "Testezeiro", "teste@teste.com", "", "senha123")

# 4 Sem confirmar senha
realizar_cadastro(driver, "Testezeiro", "teste@teste.com", "senha123", "")

# 5 Email inválido
realizar_cadastro(driver, "Testezeiro", "email_invalido@", "senha123", "senha123")

# 6 Senhas não correspondentes
realizar_cadastro(driver, "Testezeiro", "teste@teste.com", "senha123", "senha456")

# 7 Senha com menos de 6 caracteres
realizar_cadastro(driver, "Testezeiro", "senha_menor@teste.com", "12345", "12345")

# 8 E-mail já registrado
realizar_cadastro(driver, "Testezeiro", "email_registro@teste.com", "senha123", "senha123")

driver.quit()
