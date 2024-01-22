from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.demoblaze.com/"  # Reemplaza con la URL de la página web
ruta_chromedriver = "/home/stefania/Documentos/Cursos/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=ruta_chromedriver)

driver.get(url)


# Espera un tiempo para que aparezca el formulario (puedes ajustar este tiempo según sea necesario)
driver.implicitly_wait(10)

# Espera hasta que el formulario de inicio de sesión sea visible
formulario_login = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "login2")))

# Hacer clic en el enlace "login" usando JavaScript para evitar la interceptación
driver.execute_script("arguments[0].click();", formulario_login)

# Llenar el formulario de inicio de sesión con los datos de registro
campo_username_login = driver.find_element_by_id("loginusername")
campo_password_login = driver.find_element_by_id("loginpassword")

campo_username_login.send_keys("TuNombreDeUsuario113")
campo_password_login.send_keys("TuContraseña11")

# Hacer clic en el botón "Log in" para iniciar sesión
boton_login = driver.find_element_by_xpath('//button[@onclick="logIn()"]')
boton_login.click()

# Espera un tiempo para que se procese el inicio de sesión
driver.implicitly_wait(30)

# Resto del código...

# Cierra el navegador al finalizar
driver.quit()



