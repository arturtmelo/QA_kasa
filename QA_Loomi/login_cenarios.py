from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Login
def realizar_login(driver, email, senha):
    try:
        # Abre o site
        driver.get("https://www.kasa.live/")

        # Clica em "Entrar"
        button_entrar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".chakra-button.css-ovdjqs[data-cy='btn-trigger-profile']"))
        )
        button_entrar.click()

        # Preenche e-mail
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_input.send_keys(email)

        # Preenche senha
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(senha)

        # Clica em "Entrar"
        button_entrar_final = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".chakra-button.css-ncw165[data-cy='login-submit']"))
        )
        button_entrar_final.click()

    except Exception as e:
        print("Erro ao realizar login:", e)


if __name__ == "__main__":
    # Instanciando Chrome driver
    chrome_options = webdriver.ChromeOptions()
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    chrome_options.add_argument(f"executable_path={PATH}")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Teste de login com e-mail inválido
        realizar_login(driver, "email_inválido.com", "senha123")
        time.sleep(2)
        
        # Teste de login com senha incorreta
        realizar_login(driver, "torcedor@email.com", "senha456")
        time.sleep(2)
        
        # Teste de login sem preencher e-mail
        realizar_login(driver, "", "senha123")
        time.sleep(2)

        # Teste de login sem preencher senha
        realizar_login(driver, "torcedor@email.com", "")
        time.sleep(2)

        # Teste de login com e-mail não registrado
        realizar_login(driver, "usuario@naoregistrado.com", "senha123")
        time.sleep(2)

        # Teste de login com sucesso
        realizar_login(driver, "teste@gmail.com", "senha123")
        time.sleep(2)

    finally:
        time.sleep(2)
        driver.quit()
