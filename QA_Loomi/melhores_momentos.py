from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

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


# Função principal
if __name__ == "__main__":
    # Configura Driver
    chrome_options = webdriver.ChromeOptions()
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    chrome_options.add_argument(f"executable_path={PATH}")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        realizar_login(driver)
        time.sleep(1)

        # Abre aba "Melhores momentos"
        try:
            link_melhores_momentos = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "a[data-cy='link/melhores-momentos']"))
            )
            link_melhores_momentos.click()
            time.sleep(1)

        except Exception as e:
            print("Erro ao selecionar a caixa de pesquisa")

        # Clica botão "times"
        try:
            link_buscar_partida = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "svg.chakra-icon.chakra-accordion__icon.css-4tejdh"))
            )
            link_buscar_partida.click()
            time.sleep(1)

        except Exception as e:
            print("Erro ao selecionar buscar-partida")

        # Seleciona caixa-pesquisa
        try:
            search_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "input.chakra-input.css-qrzyz6"))
            )
            search_input.send_keys("nautico")
            search_input.send_keys(Keys.ENTER)
            time.sleep(1)

        except Exception as e:
            print("Erro ao selecionar a caixa de pesquisa")

        # Seleciona filtra-time
        try:
            checkbox_span = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "span.chakra-checkbox__control.css-2ym9vx"))
            )
            checkbox_span.click()
            time.sleep(1)

        except Exception as e:
            print("Erro ao selecionar filtrar-time:", e)

        # Clica no jogo
        try:
            jogo_div = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "div.card-highlight-overlay.css-8pxqf7"))
            )
            jogo_div.click()
            time.sleep(1)
        except Exception as e:
            print("Erro ao clicar no jogo:", e)

        # Fecha video
        try:
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "img.chakra-image.css-0[src*='close.beb4a05c.svg']"))
            )
            time.sleep(5)
            close_button.click()
        except Exception as e:
            print("Erro ao clicar no botão de fechar:", e)


        # Abre Sessão-Campeonatos
        try:
            abre_campeonatos = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.chakra-accordion__button.css-1sc84r0 svg.chakra-icon.chakra-accordion__icon.css-4tejdh"))
            )
            abre_campeonatos.click()
            time.sleep(1)

        except Exception as e:
            print("Erro ao clicar caixa-Campeonatos:", e)

        # Seleciona campeonato ao filtro
        try:
            checkbox_label = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "label.chakra-checkbox.css-1f11pfv"))
            )
            checkbox_label.click()
            time.sleep(1)

        except Exception as e:
            print("Erro ao clicar no checkbox:", e)

        # Testa botão "Limpar"
        try:
            botao_limpar = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(text(),'Limpar')]"))
            )
            botao_limpar.click()

        except Exception as e:
            print("Erro ao clicar no botão 'Limpar':", e)

    finally:
        time.sleep(3)
        driver.quit()
