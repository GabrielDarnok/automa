from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By


# define o caminho do diretório do perfil
profile_path = 'C:\\Users\\Lucas\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\ucohgw2h.default-release'

# cria um objeto FirefoxProfile com o diretório do perfil
profile = FirefoxProfile(profile_path)

# cria uma instância do driver do Firefox com o perfil
driver = webdriver.Firefox(firefox_profile=profile)

# navega até o Google
url = 'http://192.168.18.1/index.asp'
driver.get(url)
sleep(3)

# Localizando o elemento input que queremos preencher
input_element = driver.find_element(by=By.ID,value="txt_Username")
# Preenchendo o input com o valor desejado
input_element.send_keys("Epadmin")
sleep(1)

# Localizando o elemento input que queremos preencher
input_element = driver.find_element(by=By.ID,value="txt_Password")
# Preenchendo o input com o valor desejado
input_element.send_keys("evo@295191")
sleep(1)

# Localizando o elemento button que queremos selecionar
Button_login = driver.find_element(by=By.NAME,value="loginbuttonOnly")
# Pressionar o botão para logar
Button_login.click()
sleep(2)


# Localizando o elemento list que queremos selecionar
Button_list = driver.find_element(by=By.ID,value="name_addconfig")
# Pressionar o list
Button_list.click()
sleep(4)

# Localizando o elemento list que queremos selecionar
Button_list = driver.find_element(by=By.ID,value="name_maintaininfo")
# Pressionar o list
Button_list.click()
sleep(4)

# Localizando o elemento list que queremos selecionar
Button_list = driver.find_element(by=By.ID,value="cfgconfig")
# Pressionar o list
Button_list.click()
sleep(4)

# Localizando o elemento list que queremos selecionar
Button_list = driver.find_element(by=By.ID,value="routerclick")
# Pressionar o list
Button_list.click()
sleep(2)

# Localizando o elemento input que queremos preencher
input_element = driver.find_element(by=By.ID,value="oldPassword")
# Preenchendo o input com o valor desejado
input_element.send_keys("adminEp")
sleep(1)

# Localizando o elemento input que queremos preencher
input_element = driver.find_element(by=By.ID,value="newPassword")
# Preenchendo o input com o valor desejado
input_element.send_keys("evo@295191")
sleep(1)

# Localizando o elemento input que queremos preencher
input_element = driver.find_element(by=By.ID,value="cfmPassword")
# Preenchendo o input com o valor desejado
input_element.send_keys("evo@295191")
sleep(1)

# Fechando o driver do Selenium
#driver.quit()
