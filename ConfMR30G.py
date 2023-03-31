from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
import subprocess

# Executa o comando "ipconfig" e captura a saída
result = subprocess.run(["ipconfig"], capture_output=True, text=True)

# Verifica se a execução do comando foi bem-sucedida
if result.returncode == 0:
    print("Comando IPConfig executado com sucesso\n\n")
else:
    print(f"Ocorreu um erro durante a execução do comando IPConfig: {result.stderr}\n\n")

# Verifica se a saída do comando contém o endereço IP
if "Gateway" in result.stdout:
    ip_line = [line for line in result.stdout.split("\n") if "Gateway" in line][0]
    ip = ip_line.strip().split(": ")[1]
else:
    print("Não foi possível encontrar o endereço IP.")

if ip == "192.168.1.1":

    # define o caminho do diretório do perfil
    profile_path = 'C:\\Users\\Lucas\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\ucohgw2h.default-release'

    # cria um objeto FirefoxProfile com o diretório do perfil
    profile = FirefoxProfile(profile_path)

    # cria uma instância do driver do Firefox com o perfil
    driver = webdriver.Firefox(firefox_profile=profile)

    # navega até o Google

    driver.get("http://" + ip)
    sleep(3)

    # Localizando o elemento input que queremos preencher
    input_element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span[2]/input[1]")
    # Preenchendo o input com o valor desejado
    input_element.send_keys("evo@295191")
    sleep(1)

    # Localizando o elemento input que queremos preencher
    input_element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]/input[1]")
    # Preenchendo o input com o valor desejado
    input_element.send_keys("evo@295191")
    sleep(1)

    # Localizando o elemento "Logar"
    Button_list = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/a")
    # Pressionar o botão para "Logar"
    Button_list.click()
    sleep(15)

    # Localizando o elemento "Pular"
    Button_list = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div/div[4]/div[4]/div[2]/div[1]/a")
    # Pressionar o botão para "Pular"
    Button_list.click()
    sleep(4)

    # Localizando o elemento "Confirmar"
    Button_list = driver.find_element(by=By.XPATH, value="/html/body/div[5]/div[2]/div[4]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/a")
    # Pressionar o botão para "Confirmar"
    Button_list.click()
    sleep(4)

    # Localizando o elemento "Wirelles"
    Button_list = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[3]/div/div[1]/ul/li[3]/a")
    # Pressionar o botão "Wirelles"
    Button_list.click()
    sleep(3)

    # Localizando o elemento input que queremos preencher
    input_element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[5]/div[2]/div[1]/div[2]/div[1]/span[2]/input")
    # Preenchendo o input com o valor desejado
    input_element.clear()
    input_element.send_keys("EVOLUNET")
    sleep(1)

    # Localizando o elemento input que queremos preencher
    input_element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[5]/div[2]/div[4]/div[2]/div/div[2]/div[1]/span[2]/input")
    # Preenchendo o input com o valor desejado
    input_element.clear()
    input_element.send_keys("12345678")
    sleep(1)

    # Localizando o elemento input que queremos preencher
    input_element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[3]/div[2]/div[1]/div[2]/div[1]/span[2]/input")
    # Preenchendo o input com o valor desejado
    input_element.clear()
    input_element.send_keys("EVOLUNET_5G")
    sleep(1)

    # Localizando o elemento input que queremos preencher
    input_element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[3]/div[2]/div[4]/div[2]/div/div[2]/div[1]/span[2]/input")
    # Preenchendo o input com o valor desejado
    input_element.clear()
    input_element.send_keys("12345678")
    sleep(1)

    # Localizando o elemento "Salvar"
    Button_list = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/a")
    # Pressionar o botão "Salvar"
    Button_list.click()
    sleep(3)

    # Localizando o elemento "Advenced"
    Button_list = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div[1]/div[3]/div/div[1]/ul/li[4]/a")
    # Pressionar o botão "Advenced"
    Button_list.click()
    sleep(3)

    # Localizando o elemento "Sistema"
    Button_list = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div[1]/ul/li[10]/a")
    # Pressionar o botão "Sistema"
    Button_list.click()
    sleep(3)

    # Localizando o elemento "Administração"
    Button_list = driver.find_element(by=By.XPATH, value="//html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div[1]/ul/li[10]/ul/li[3]/a")
    # Pressionar o botão "Administração"
    Button_list.click()
    sleep(8)

    # Localizando o elemento "Remote"
    Button_list = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/ul/li/div/label/span[1]")
    # Pressionar o botão "Remote"
    Button_list.click()
    sleep(4)

    # Localizando o elemento input "Porta" que queremos preencher
    input_element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/span[2]/input")
    # Preenchendo o input com o valor desejado
    input_element.clear()
    input_element.send_keys("8484")
    sleep(4)

    # Localizando o elemento "Box"
    Button_list = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[3]/div[2]/div[3]/div[2]/div[1]/span[2]/input")
    # Pressionar o botão "Box"
    Button_list.click()
    sleep(5)

    # Localizando o elemento "D.E"
    Button_list = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/ul/li[2]/label")
    # Pressionar o botão "D.E"
    Button_list.click()
    sleep(3)

    # Localizando o elemento input "IP" que queremos preencher
    input_element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[3]/div[2]/div[4]/div[2]/div[1]/span[2]/input")
    # Preenchendo o input com o valor desejado
    input_element.clear()
    input_element.send_keys("177.55.128.30")
    sleep(1)

    # Localizando o elemento "Salvar"
    Button_list = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/a")
    # Pressionar o botão "Salvar"
    Button_list.click()
    sleep(3)

    #Fechando o programa
    driver.quit()
else:
    print("O computador ainda não pegou o IP do roteador, aguarde alguns segundos e rode o programa novamente.")