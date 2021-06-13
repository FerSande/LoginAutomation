import csv
import pandas as pd
from selenium import webdriver
import time

#se lee el archivo de casos de prueba 
df = pd.read_csv("C:/Users/ferhs/OneDrive/Documentos/ChallengeCrowdar/casosDePrueba.csv",delimiter=";")

#Se recorren los casos de prueba
for ind in df.index:
    driver = webdriver.Chrome(executable_path = "C:/Users/ferhs/OneDrive/Documentos/ChallengeCrowdar/chromedriver_win32/chromedriver.exe")
    #Se duplica el df en df2
    df2 = df
    #ingreso a la pagina
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    #busco el user name para ingresarle el valor
    driver.find_element_by_name("user-name").send_keys(df['user'][ind])
    time.sleep(2)
    #busco la password para ingresarle el valor
    driver.find_element_by_name("password").send_keys(df['pass'][ind])
    time.sleep(2)
    #busco el login button y ingreso
    driver.find_element_by_name("login-button").click()
    time.sleep(2)
    #si aparece el boton de menu desplegable(bm-burger-button) significa que ingreso sino fallo el login
    if len(driver.find_elements_by_class_name("bm-burger-button")):
        log = "Login successful"
        print(log)
    else:
        log = "Login failed"
        print(log)
    time.sleep(2)
    #si el log que devolvio lo anterior es igual al del archivo de prueba devuelve Anduvo sino Fallo
    if log == df['Login'][ind]:
        df2['Login'][ind] = "Anduvo"
    else:
        df2['Login'][ind] = "Fallo"
    
    driver.close()
#genero el nuevo archivo con los resultados finales
df2.to_csv("C:/Users/ferhs/OneDrive/Documentos/ChallengeCrowdar/loginRespuesta.csv",sep = ";")


        
        
        
        
        
    
    
    
    
    
    
    
    
    
    