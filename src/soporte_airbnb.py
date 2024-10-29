import os
import requests
from dotenv import load_dotenv
import json
import pandas as pd

load_dotenv()

rapidapi_key = os.getenv("RAPIDAPI_KEY")

def obtener_listado_airbnb(ciudad, checkin, checkout, adultos=5):
    url = "https://airbnb13.p.rapidapi.com/search-location"
    
    params = {
        "location": ciudad,
        "checkin": checkin,
        "checkout": checkout,
        "adults": adultos,
        "currency": "EUR",
        "locale": "en"
    }

    headers = {
        "X-RapidAPI-Key": rapidapi_key,  
        "X-RapidAPI-Host": "airbnb13.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
    
def procesar_listado_airbnb_a_dataframe(listado_data):
    if listado_data is None or 'results' not in listado_data:
        print("No se encontraron listados o error en la API.")
        return pd.DataFrame()

    alojamientos_lista = []
    
    for alojamiento in listado_data['results']:
        nombre = alojamiento.get('name', 'No especificado')
        precio_total = alojamiento['price']['total']
        moneda = alojamiento['price']['currency']
        latitud = alojamiento.get('lat', 'No especificado')
        longitud = alojamiento.get('lng', 'No especificado')
        direccion = alojamiento.get('address', 'No especificado')
        url = alojamiento.get('url', 'No especificado')

        alojamientos_lista.append({
            'Nombre': nombre,
            'Precio Total': f"{precio_total} {moneda}",
            'Latitud': latitud,
            'Longitud': longitud,
            'Dirección': direccion,
            'URL': url
        })

    df = pd.DataFrame(alojamientos_lista)
    return df