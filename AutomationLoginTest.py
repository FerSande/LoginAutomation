import csv
import pandas as pd
from selenium import webdriver
import time


df = pd.read_csv("C:/Users/ferhs/OneDrive/Documentos/ChallengeCrowdar/casosDePrueba.csv",delimiter=";")

for ind in df.index:
    driver = webdriver.Chrome(executable_path = "C:/Users/ferhs/OneDrive/Documentos/ChallengeCrowdar/chromedriver_win32/chromedriver.exe")
    df2 = df
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    user = driver.find_element_by_name("user-name")
    user.send_keys(df['user'][ind])
    time.sleep(2)
    password = driver.find_element_by_name("password")
    password.send_keys(df['pass'][ind])
    time.sleep(2)
    logbutton = driver.find_element_by_name("login-button")
    logbutton.click()
    time.sleep(2)
    if len(driver.find_elements_by_class_name("bm-burger-button")):
        log = "Login successful"
        print(log)
    else:
        log = "Login failed"
        print(log)
    time.sleep(2)
    if log == df['Login'][ind]:
        df2['Login'][ind] = "Anduvo"
    else:
        df2['Login'][ind] = "Fallo"
    
    driver.close()
df2.to_csv("C:/Users/ferhs/OneDrive/Documentos/ChallengeCrowdar/loginRespuesta.csv",sep = ";")


        
        
        
        
        
    
    
    
    
    
    
    
    
    
    