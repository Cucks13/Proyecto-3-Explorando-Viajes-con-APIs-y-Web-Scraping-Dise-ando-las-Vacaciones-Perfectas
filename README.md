# Descripción del Proyecto

Este proyecto tiene como objetivo realizar un Análisis Exploratorio de Datos (EDA) comparativo entre dos ciudades europeas: Berlín y Viena, basado en tres aspectos clave:
- Actividades turísticas en ambas ciudades.
- Alojamientos en Airbnb disponibles en Berlín y Viena.
- Vuelos de ida y vuelta entre Madrid y las ciudades de destino.

Este análisis está pensado específicamente para un grupo de 5 amigos que planean un viaje a una de estas dos ciudades. El objetivo es encontrar las mejores opciones en cuanto a actividades, alojamientos y vuelos, optimizando tanto el presupuesto como las experiencias disponibles.

## Tecnologías Utilizadas

- Scraping de actividades: las actividades turísticas han sido obtenidas mediante scraping de la web Civitatis usando la librería `BeautifulSoup`.
- Vuelos: los datos de vuelos han sido extraídos utilizando la API de Amadeus para obtener información en tiempo real sobre vuelos de ida y vuelta entre Madrid y Berlín/Viena.
- Alojamientos (Airbnb): los datos de alojamientos en Airbnb fueron obtenidos a través de una API disponible en `RapidAPI` para obtener listados en las fechas seleccionadas.

## Estructura del Proyecto

El proyecto está dividido en varias secciones que cubren el EDA de cada conjunto de datos:

- **Actividades**: información sobre diferentes actividades turísticas disponibles en Berlín y Viena, junto con sus precios y descripciones.
- **Alojamientos (Airbnb)**: precios, direcciones y enlaces de Airbnbs en ambas ciudades.
- **Vuelos**: análisis de precios de vuelos de ida y vuelta entre Madrid y Berlín/Viena, incluyendo detalles de aerolíneas, fechas y duración de vuelos.

## Archivos de Datos

Los datos utilizados en este proyecto se encuentran en los siguientes archivos CSV:

### Actividades:
- `actividadesberlin.csv`
- `actividadesviena.csv`

Columnas:
- Nombre actividad
- Descripción actividad
- Precio actividad

### Airbnb:
- `airbnb_berlin.csv`
- `airbnb_viena.csv`

Columnas:
- Nombre
- Precio total
- Dirección
- URL

### Vuelos:
- `vuelosidaberlin.csv`
- `vuelosidaviena.csv`
- `vuelosvueltaberlin.csv`
- `vuelosvueltaviena.csv`

Columnas:
- Precio total (EUR)
- Aerolínea
- Origen
- Destino
- Salida
- Llegada

## Instalación

### Requisitos

Este proyecto requiere las siguientes bibliotecas de Python:

- `pandas`: para la manipulación y análisis de datos estructurados.
- `matplotlib`: para la creación de gráficos.
- `seaborn`: para gráficos estadísticos.
- `BeautifulSoup`: para realizar scraping de las actividades turísticas.
- `python-dotenv`: para gestionar las credenciales de las APIs mediante un archivo `.env`.
- `requests`: para interactuar con las APIs (Amadeus y RapidAPI).

Puedes instalarlas ejecutando el siguiente comando en tu terminal:

```bash
pip install pandas matplotlib seaborn python-dotenv requests beautifulsoup4
```

## Uso de .env

Este proyecto utiliza `python-dotenv` para gestionar claves API y otras configuraciones sensibles. Asegúrate de crear un archivo `.env` en el directorio raíz de tu proyecto con el siguiente formato:

```
RAPIDAPI_KEY = tu_clave_api_rapidapi  
AMADEUS_CLIENT_ID = tu_client_id_amadeus  
AMADEUS_CLIENT_SECRET = tu_client_secret_amadeus
```

El archivo `.env` se utilizará para cargar estas variables de entorno de manera segura y eficiente.

## Estructura del Código

### EDA Individual para Cada Conjunto de Datos

#### Actividades:
- Scraping de actividades con `BeautifulSoup` desde Civitatis.
- Análisis de la distribución de precios y tipos de actividades.
- Gráficos de comparación entre Berlín y Viena.

#### Airbnb:
- Datos obtenidos a través de la API de `RapidAPI`.
- Se estudian los precios de los alojamientos y su localización.

#### Vuelos:
- Datos de vuelos obtenidos de la API de Amadeus.
- Análisis de los precios de los vuelos de ida y vuelta entre Madrid y ambas ciudades.
- Comparaciones de aerolíneas y duración de los vuelos.

### Comparaciones entre Berlín y Viena
- Visualización comparativa de los precios de actividades, alojamientos y vuelos entre las dos ciudades.

> **Nota**: Asegúrate de no compartir tus claves API públicamente para proteger la seguridad de tu proyecto.

> **Recuerda**: Para ejecutar en un Jupyter Notebook comandos de terminal deberá ir una exclamación delante del comando Ej: `!pip install pandas`