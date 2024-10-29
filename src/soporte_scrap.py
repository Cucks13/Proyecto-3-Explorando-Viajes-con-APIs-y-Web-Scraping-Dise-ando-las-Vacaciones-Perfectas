# Importamos las librerías que necesitamos

# Librerías de extracción de actividades
# -----------------------------------------------------------------------
from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore

# Tratamiento de actividades
# -----------------------------------------------------------------------
import pandas as pd # type: ignore
import numpy as np
import re
from time import sleep
import time
import multiprocessing

# Importar librerías para automatización de navegadores web con Selenium
# -----------------------------------------------------------------------
from selenium import webdriver  # type: ignore # Selenium es una herramienta para automatizar la interacción con navegadores web.
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore # ChromeDriverManager gestiona la instalación del controlador de Chrome.
from selenium.webdriver.common.keys import Keys  # type: ignore # Keys es útil para simular eventos de teclado en Selenium.
from selenium.webdriver.support.ui import Select  # type: ignore # Select se utiliza para interactuar con elementos <select> en páginas web.
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.common.exceptions import NoSuchElementException # type: ignore # Excepciones comunes de selenium que nos podemos encontrar

def traer_datos(url):

    try:
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        sleep(5)
        driver.close()
    except:
        print(f"Error en traer_datos: {url}")

def traer_actividades(url, datos_input):
    ciudad = datos_input[1][0]
    date_1 = datos_input[1][1]
    date_2 = datos_input[1][2]

    actividades = {
        'titulo': [],
        'descripcion': [],
        'precio': [],
    }

    try:
        print(f"call url: {url}")
        res = requests.get(url)
        print(f"respuesta url: {res.status_code}")

        if res.status_code == 200:
            list_titulos = []
            list_descripciones = []
            list_precios = []

                    
            sopa = BeautifulSoup(res.content, "html.parser")
            lista_productos = sopa.findAll("div", {"class": "o-search-list__item"} )

            if len(lista_productos) > 0:
                for i in lista_productos:
                    titulo = i.find("h2").text
                    descripcion = i.find("div",{"class":"comfort-card__text l-list-card__text"}).text
                    precio = i.find("span",{"class":"comfort-card__price__text"}).text

                    if (len(titulo) > 0):
                        list_titulos.append(str(titulo).strip())
                    else:
                        list_titulos.append(np.nan)
                    if (len(descripcion) > 0):
                        list_descripciones.append(str(descripcion).replace("\xa0"," ").strip())
                    else:
                        list_descripciones.append(np.nan)
                    if (len(precio) > 0):
                        list_precios.append(str(precio).replace("¡Gratis!","0").replace("€","").replace(",",".").strip())
                    else:
                        list_precios.append(np.nan)



                actividades['titulo'] = list_titulos
                actividades['descripcion'] = list_descripciones
                actividades['precio'] = list_precios

    except:
        print(f"Error al traer_actividades(): {datos_input}")
 
    return actividades