from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicia Driver
driver = webdriver.Chrome()

# Login
def realizar_login(driver):
    try:
        # Abre Site
        driver.get("https://www.kasa.live/")

        # Clica "Entrar"
        button_entrar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".chakra-button.css-ovdjqs[data-cy='btn-trigger-profile']"))
        )
        button_entrar.click()

        # Preenche e-mail
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_input.send_keys("teste@gmail.com")

        # Preenche senha
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("senha123")

        # Clica "Entrar"
        button_entrar_final = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".chakra-button.css-ncw165[data-cy='login-submit']"))
        )
        button_entrar_final.click()

    except Exception as e:
        print("Erro ao realizar login:", e)


try:
    realizar_login(driver)
    time.sleep(1)

    try:
        # Encontrar o campo de entrada de data
        botao_data = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input.chakra-input.css-wpe2lc[placeholder='Jan 29, 2024']"))
        )
        botao_data.click()
        time.sleep(2) 
        botao_data.clear()

        # Clica botão do dia 17
        button_dia_17 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='rdp-button_reset rdp-button rdp-day' and .//span[text()='17']]"))
        )
        button_dia_17.click()
        time.sleep(2) 

        # Clica botão do dia 31
        button_dia_31 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='rdp-button_reset rdp-button rdp-day' and .//span[text()='31']]"))
        )
        button_dia_31.click()
        time.sleep(2) 

    except Exception as e:
        print("Erro durante a seleção dos dias:")

    try:
        # Filtra por CAMPEONATOS
        championship_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "filter-championship"))
        )
        championship_input.click()
        time.sleep(2)
        championship_input.send_keys("carioca")

        # Seleciona campeonato
        elemento_campeonato_carioca = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Campeonato Carioca')]"))
        )
        elemento_campeonato_carioca.click()
        time.sleep(4)

    except Exception as e:
        print("Erro ao selecionar caixa times")

    try:
        input_time = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input#filter-team.chakra-input.css-etjvw4"))
        )
        input_time.click()
        input_time.send_keys("fluminense")
        time.sleep(1)
    
    except Exception as e:
        print("Erro ao selecionar caixa times")


except Exception as e:
    print("Erro ao encontrar o input:")

finally:
    time.sleep(3)
    driver.quit()

