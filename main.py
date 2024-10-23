import requests

# Definir la URL base de la API
base_url = "https://earthquake.usgs.gov/fdsnws/event/1/"

# Definir los parámetros para la consulta de terremotos
params = {
    "format": "geojson",         # Formato de respuesta (geojson o xml)
    "starttime": "2024-01-01",   # Fecha de inicio (YYYY-MM-DD)
    "endtime": "2024-01-02",     # Fecha de fin (YYYY-MM-DD)
    "minmagnitude": 5            # Magnitud mínima de los terremotos a consultar
}

# Método para consultar la API
def consultar_terremotos(params):
    url = f"{base_url}query"  # Método de consulta "query"
    
    try:
        response = requests.get(url, params=params)  # Hacer la solicitud GET
        response.raise_for_status()  # Verificar que no haya errores en la solicitud
        
        # Obtener los datos en formato JSON
        data = response.json()
        return data
    
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")
        return None

# Ejecutar la consulta
terremotos = consultar_terremotos(params)

# Verificar y mostrar la respuesta
if terremotos:
    print(f"Se encontraron {len(terremotos['features'])} terremotos:")
    for terremoto in terremotos['features']:
        propiedades = terremoto['properties']
        print(f"Lugar: {propiedades['place']}, Magnitud: {propiedades['mag']}")
else:
    print("No se encontraron datos o ocurrió un error.")
