import requests

API_KEY = 'YOUR_API_KEY'  # Reemplaza esto con tu API Key de GraphHopper

def obtener_datos_viaje(origen, destino, vehiculo):
    url = f"https://graphhopper.com/api/1/route?point={origen}&point={destino}&vehicle={vehiculo}&locale=es&instructions=true&calc_points=true&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

def mostrar_narrativa(data):
    for instruccion in data['paths'][0]['instructions']:
        print(f"{instruccion['distance']} metros: {instruccion['text']}")

def main():
    while True:
        print("Ingrese 's' para salir.")
        origen = input("Ingrese la Ciudad de Origen: ")
        if origen.lower() == 's':
            break
        destino = input("Ingrese la Ciudad de Destino: ")
        if destino.lower() == 's':
            break
        
        vehiculo = input("Ingrese el medio de transporte (car, bike, foot): ").lower()
        if vehiculo == 's':
            break

        try:
            data = obtener_datos_viaje(origen, destino, vehiculo)
            
            if 'paths' in data and data['paths']:
                distancia_km = data['paths'][0]['distance'] / 1000
                distancia_millas = distancia_km * 0.621371
                duracion = data['paths'][0]['time'] / 3600000  # Convierte milisegundos a horas
                
                print(f"\nDistancia entre {origen} y {destino}:")
                print(f"{distancia_millas:.2f} millas")
                print(f"{distancia_km:.2f} kilómetros")
                print(f"Duración del viaje: {duracion:.2f} horas")

                print("\nNarrativa del viaje:")
                mostrar_narrativa(data)
            else:
                print("No se pudo encontrar una ruta entre las ciudades especificadas.")

        except Exception as e:
            print(f"Error al obtener datos del viaje: {e}")

if __name__ == "__main__":
    main()
