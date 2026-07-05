import sys

distancias = {
    ("Santiago", "Lisboa"): 10500,
    ("Santiago", "Oporto"): 10800,
    ("Valparaiso", "Lisboa"): 10600,
    ("Concepcion", "Lisboa"): 11200,
    ("La Serena", "Lisboa"): 10200,
    ("Temuco", "Lisboa"): 11800,
    ("Antofagasta", "Lisboa"): 9800,
}

def calcular_distancia(origen, destino):
    clave = (origen.title(), destino.title())
    clave_inversa = (destino.title(), origen.title())
    return distancias.get(clave) or distancias.get(clave_inversa)

print("CALCULADORA DE VIAJES CHILE - PORTUGAL\n")

while True:
    print("-" * 60)
    origen = input("Ciudad de Origen (Chile): ").strip()
    if origen.lower() == 's':
        print("Gracias por usar el programa!")
        break

    destino = input("Ciudad de Destino (Portugal): ").strip()
    if destino.lower() == 's':
        print("Gracias por usar el programa!")
        break

    distancia_km = calcular_distancia(origen, destino)

    if distancia_km is None:
        print("Lo siento, no tengo informacion de distancia para esas ciudades.")
        print("Intenta con: Santiago, Valparaiso, Concepcion, Antofagasta -> Lisboa, Oporto")
        continue

    distancia_millas = round(distancia_km * 0.621371, 2)

    # Medios de transporte
    transportes = {
        "1": ("Avion", 850),
        "2": ("Barco / Crucero", 40),
        "3": ("Combinado", 600)
    }

    print("\nMedio de transporte:")
    for k, (nombre, _) in transportes.items():
        print(f"   {k}. {nombre}")
    
    opcion = input("Seleccione una opcion (1-3): ").strip()
    medio, velocidad = transportes.get(opcion, ("Avion", 850))
    
    duracion_horas = round(distancia_km / velocidad, 1)

    print("\n" + "="*70)
    print("NARRATIVA DEL VIAJE")
    print("="*70)
    print(f"Partes desde la ciudad de {origen.title()}, Chile, dejando atras")
    print("los Andes y el Oceano Pacifico.")
    print(f"Tras recorrer {distancia_km:,} kilometros hacia el este,")
    print(f"cruzas el Atlantico Sur hasta llegar a {destino.title()}, Portugal.")
    print(f"Este viaje en {medio.lower()} tendra una duracion aproximada de {duracion_horas} horas.")
    print("Un viaje lleno de aventura, cultura y paisajes inolvidables.")
    print("="*70)

    print(f"\nRESUMEN DEL VIAJE:")
    print(f"   Distancia : {distancia_km:,} km ({distancia_millas:,} millas)")
    print(f"   Transporte: {medio}")
    print(f"   Duracion  : {duracion_horas} horas aprox.")

    print("\nEscribe 's' para salir o presiona Enter para un nuevo calculo.\n")