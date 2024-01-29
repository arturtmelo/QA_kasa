from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
        print("Erro ao realizar login:")

def clicar_em_times_e_campeonatos(driver):
    try:
        # Clica no link "Calendário" após o login
        link_calendario = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a[data-cy='link/calendario']"))
        )
        link_calendario.click()
        time.sleep(4)

    except Exception as e:
        print("Erro ao clicar no elemento 'Times e campeonatos':")

    try:
        div_popovers = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.css-1xnrnb4"))
        )
        
        if div_popovers:
            div_popovers[0].click()
            time.sleep(2.3)

        else:
            print("Nenhum elemento encontrado com o seletor fornecido.")

    except Exception as e:
        print("Erro ao clicar na div do popover:")

    try:
        # Encontrar e clicar no botão "Times e campeonatos"
        clique_time = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[@class='chakra-text css-ak7brf' and text()='Times e campeonatos']"))
        )
        clique_time.click()
        time.sleep(1)
    except Exception as e:
        print("Erro ao clicar no botão 'Times e campeonatos':")

    try:
        # Clicar para expandir a sessão do time
        expandir_time = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='css-1rtd0zn']"))
        )
        expandir_time.click()
        time.sleep(1)
        
    except Exception as e:
        print("Erro ao expandir a sessão do time:")

    try:
        # Encontrar e preencher a caixa de texto de pesquisa
        caixa_pesquisa = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Pesquisar'].chakra-input.css-qrzyz6"))
        )
        caixa_pesquisa.send_keys("nautico")
        time.sleep(1)
    except Exception as e:
        print("Erro ao preencher a caixa de pesquisa:")

    try:
        # Adiciona TIME ao FILTRO
        botao_marcar_time = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span.chakra-checkbox__control.css-2ym9vx"))
        )
        botao_marcar_time.click()
        time.sleep(1)
    except Exception as e:
        print("Erro ao selecionar o botão para marcar o time:")

    try:
        # Seleciona SESSAO CAMPEONATO
        botao_campeonatos = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[@class='chakra-text css-11brvp6']"))
        )
        botao_campeonatos.click()
        time.sleep(1)
        
    except Exception as e:
        print("Erro ao selecionar o botão para marcar o campeonato:")
    
    try:
        # Clicar para adicionar o CAMPEONATO à lista
        botao_adicionar_campeonato = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span.chakra-checkbox__control.css-2ym9vx"))
        )
        botao_adicionar_campeonato.click()
        time.sleep(1)
        
    except Exception as e:
        print("Erro ao encontrar ou interagir com o botão para adicionar CAMPEONATO à lista:")


    try:
        # Limpa lista CAMPEONATO
        botao_limpar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span.chakra-checkbox__control.css-2ym9vx"))
        )
        botao_limpar.click()
        time.sleep(1)
        
    except Exception as e:
        print("Erro ao clicar LIMPAR")


if __name__ == "__main__":
    # Configura Driver
    chrome_options = webdriver.ChromeOptions()
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    chrome_options.add_argument(f"executable_path={PATH}")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        realizar_login(driver)
        clicar_em_times_e_campeonatos(driver)
        

    finally:
        time.sleep(3)
        driver.quit()
