# verificar_vlan.py
def verificar_vlan(numero_vlan):
    rango_normal = range(1, 1000)
    rango_extendido = range(1006, 4095)
    
    if numero_vlan in rango_normal:
        print(f"La VLAN {numero_vlan} pertenece al rango normal.")
    elif numero_vlan in rango_extendido:
        print(f"La VLAN {numero_vlan} pertenece al rango extendido.")
    else:
        print(f"La VLAN {numero_vlan} no pertenece a ningún rango conocido.")

def main():
    vlan = int(input("Ingrese el número de VLAN a verificar: "))
    verificar_vlan(vlan)

if __name__ == "__main__":
    main()
