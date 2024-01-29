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
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".chakra-button.css-ovdjqs[data-cy='btn-trigger-profile']"))
        )
        button_entrar.click()

        # Preenche e-mail
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_input.send_keys("teste_do_danadinho@gmail.com")
        time.sleep(1)

        # Preenche senha
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("sdaasdasdas")
        time.sleep(1)

        # Clica "Entrar"
        button_entrar_final = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".chakra-button.css-ncw165[data-cy='login-submit']"))
        )
        button_entrar_final.click()

    except Exception as e:
        print("Erro ao realizar login:", e)


def favoritar_desfavoritar(driver, nome_time):
    try:
        # Seleciona "Favoritos"
        link_favoritos = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-cy='link/favoritos']"))
        )
        link_favoritos.click()
        time.sleep(1)

        # Caso tenha 1+ times selecionados, clica "Adicionar Favoritos" correto
        try:
            link_addfavoritos = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.css-1jialgf[data-cy='btn-favorite-team']"))
            )
            link_addfavoritos.click()

        except:
            # Caso tenha 0 times selecionados, clica "Adicionar Favoritos" correto
            try:
                favoritar_button = WebDriverWait(driver, 1).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.css-6inhn7[data-cy='btn-favorite-team']"))
                )
                favoritar_button.click()


            except Exception as e:
                print("Erro ao clicar no botão favoritar:", e)

        # Seleciona caixa-pesquisa
        try:
            search_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-cy='input-search-teams']"))
            )
        except:
            print("Erro ao selecionar a caixa de pesquisa.")

        # Digita nome-time
        search_input.send_keys(nome_time)
        search_input.send_keys(Keys.ENTER)
        time.sleep(1)

        # Clica "Add"
        try:
            botao_add = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.css-6cuto3"))
            )
            botao_add.click()
            time.sleep(1)

        except Exception as e:
            print("Erro ao clicar em 'Add':", e)

        # Clica "Concluir"
        botao_concluir = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.css-171me6r[data-cy='btn-submit-teams']"))
        )
        botao_concluir.click()
        time.sleep(1)

        # Clica "Editar"
        try:
            botao_editar = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-cy='btn-edit-teams']"))
            )
            botao_editar.click()
            time.sleep(1)

            # Clica remover
            botao_remover = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.css-di3rc"))
            )
            botao_remover.click()
            time.sleep(1)

            # Clica "Salvar"
            botao_salvar = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-cy='btn-save-teams']"))
            )
            botao_salvar.click()
            time.sleep(1)

            try:
                # Clica "Favoritar canal"
                favoritar_canal_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.css-6inhn7[data-cy='btn-favorite-channel']"))
                )
                favoritar_canal_button.click()
                time.sleep(1)

            except Exception as e:
                print("Erro ao clicar favoritar canal 1:", e)

            try: # Clica "Add Canal"
                add_canal_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.css-10ir859"))
                )
                add_canal_button.click()
                time.sleep(1)

            except Exception as e:
                print("Erro ao clicar add canal:", e)

            try:
                # Clica "Concluir canal"
                concluir_canal_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.css-vraz4h[data-cy='btn-submit-channels']"))
                )
                concluir_canal_button.click()
                time.sleep(1)

            except Exception as e:
                print("Erro ao clicar concluir canal:", e)

            try:
                # Clica "Editar Canal"
                editar_canal_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.css-l5syvq[data-cy='btn-edit-channels']"))
                )
                editar_canal_button.click()
                time.sleep(1)

            except Exception as e:
                print("Erro ao clicar editar canal:", e)

            try:
                # Clica ícone SVG
                svg_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.css-ju8hy0"))
                )
                svg_button.click()
            except Exception as e:
                print("Erro ao clicar no ícone SVG:", e)

            try:
                # Clica "Concluir" - canal
                concluir_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.css-vraz4h[data-cy='btn-submit-channels']"))
                )
                concluir_button.click()
                time.sleep(1)

            except Exception as e:
                print("Erro ao clicar concluir-canal:", e)

        except Exception as e:
            print("Erro ao editar o canal:", e)

    except Exception as e:
        print("Erro ao favoritar o time:", e)
    
def aba_partidas(driver):
    try:
        # Clica link 'Partidas'
        link_partidas = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.css-1de5m1v a.chakra-link[data-cy='link/'][title='Partidas']"))
        )
        link_partidas.click()
        time.sleep(1)

        try:
            # Marca-Gcalendar
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".chakra-button.css-1d6u36w[aria-label='Adicionar ao calendário']"))
            )
            button.click()
            time.sleep(1)

            # Desmarca-Gcalendar
            button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".chakra-button.css-1d6u36w[aria-label='Adicionar ao calendário']"))
            )
            button.click()
            time.sleep(1)

            # Favorita Partida
            botao_favoritar_partida = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.css-1d6u36w[aria-label='Favoritar Partida']"))
            )
            botao_favoritar_partida.click()
            time.sleep(1)

        except Exception as e:
            print("Erro ao favoritar a partida:", e)

        # Clica aba-partidas
        all_handles = driver.window_handles
        driver.switch_to.window(all_handles[0])
        time.sleep(1)

        try:
            #  botao ver plataformas
            botao_personalizado = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'chakra-button') and contains(@class,'css-me39x0')]"))
            )
            botao_personalizado.click()
            time.sleep(1)

        except Exception as e:
            print("Erro ao clicar no botão ver plataformas:", e)

        try:
            # botao aba melhores momentos
            botao_melhores_momentos = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Melhores momentos')]"))
            )
            botao_melhores_momentos.click()
            time.sleep(1)

        except Exception as e:
            print("Erro ao clicar no botão Melhores momentos:", e)

        try:
        # Fecha modal
            link_favoritos = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "svg.chakra-icon.css-onkibi"))
            )
            link_favoritos.click()
            time.sleep(1)

        except Exception as e:
            print("Erro Fechar modal:", e)
                
        # Clica aba-favoritos
        link_favoritos = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-cy='link/favoritos']"))
        )
        link_favoritos.click()
        time.sleep(1)

    except Exception as e:
        print("Erro ao interagir com a aba 'Partidas':", e)    


# Função principal
if __name__ == "__main__":
    # Configura Driver
    chrome_options = webdriver.ChromeOptions()
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    chrome_options.add_argument(f"executable_path={PATH}")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        realizar_login(driver)
        favoritar_desfavoritar(driver, "nautico")
        aba_partidas(driver)

    finally:
        time.sleep(3)
        driver.quit()