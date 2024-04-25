from selenium import webdriver
from selenium.webdriver.common.by import By
import time



# Inisialisasi WebDriver
driver = webdriver.Chrome()

print("Akan Memulai Program")

# Buka halaman Instagram
driver.get("https://www.instagram.com/")
time.sleep(5)

#Memasukan username
print("Memasukan Username")
username_element = driver.find_element(By.NAME, 'username')
username_element.send_keys("username") #ganti dengan usernmae anda
print("username sudah dimasukan")
time.sleep(2)

#memasukan password
print("Mencoba memasukan password")
PW_element = driver.find_element(By.NAME, 'password')
PW_element.send_keys("password") #ganti dengan password anda
print("Password berhasil dimasukan")
time.sleep(2)


#mencoba login
print("Mencoba login")
masuk = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')
masuk.click()
print("Sudah login")
time.sleep(10)


#mencoba searing akun pewdiepie
print("Mencoba searcing akun")
print("3")
driver.get('https://www.instagram.com/pewdiepie/')
time.sleep(2)
print("2")
print("1")
print("Berhasil serching Pewdiepie")
time.sleep(10)