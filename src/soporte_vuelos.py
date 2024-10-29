import os
import requests
from dotenv import load_dotenv
load_dotenv()
import pandas as pd


def obtener_token():
    client_id = os.getenv("AMADEUS_CLIENT_ID")
    client_secret = os.getenv("AMADEUS_CLIENT_SECRET")
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        return None
    
def obtener_vuelos(token_acceso, inicio, destino, fecha_ida, fecha_vuelta, n_personas):
    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    params = {
        "originLocationCode": inicio,  
        "destinationLocationCode": destino,  
        "departureDate": fecha_ida,
        "returnDate": fecha_vuelta,
        "adults": n_personas,  
    }
    print(params)
    headers = {
        "Authorization": f"Bearer {token_acceso}"
    }
    print(headers)  # Para ver si el token está en el encabezado

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def procesar_vuelos_a_dataframe(vuelos):
   
    vuelos_lista = []

    for vuelo in vuelos['data']:
      
        precio_total = vuelo['price']['total']
        aerolinea = vuelo['validatingAirlineCodes'][0]
        itinerario = vuelo['itineraries'][0]  
       
        segmento = itinerario['segments'][0]
        salida = segmento['departure']['at']  
        llegada = segmento['arrival']['at'] 
        origen = segmento['departure']['iataCode'] 
        destino = segmento['arrival']['iataCode']  
        duracion = itinerario['duration']  

        vuelos_lista.append({
            'Precio Total (EUR)': precio_total,
            'Aerolínea': aerolinea,
            'Origen': origen,
            'Destino': destino,
            'Salida': salida,
            'Llegada': llegada,
            'Duración': duracion
        })

    vuelos_df = pd.DataFrame(vuelos_lista)

    return vuelos_df