print("Verificador de Rango de VLAN\n")

try:
    vlan = int(input("Ingrese el número de VLAN: "))

    if vlan < 1 or vlan > 4094:
        print("Error: El número de VLAN debe estar entre 1 y 4094.")
    elif vlan >= 1 and vlan <= 1005:
        print(f"La VLAN {vlan} corresponde a un **rango NORMAL**.")
    else:
        print(f"La VLAN {vlan} corresponde a un **rango EXTENDIDO**.")

except ValueError:
    print("Error: Por favor ingrese solo números.")