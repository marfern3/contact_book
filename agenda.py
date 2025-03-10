def agregar_contacto(contactos):
    nombre = input("Introduce el nombre del contacto: ").strip()
    
    while True:
        telefono = input("Introduce el número de teléfono (máximo 11 dígitos): ").strip()
        if telefono.isdigit() and len(telefono) <= 11:
            break
        else:
            print("Número de teléfono inválido. Debe contener solo números y tener máximo 11 dígitos.")

    if nombre in contactos:
        print("Ese contacto ya existe. Usa la opción de actualizar.")
    else:
        contactos[nombre] = telefono
        print(f"Contacto {nombre} agregado con éxito.")

def actualizar_contacto(contactos):
    nombre = input("Introduce el nombre del contacto a actualizar: ").strip()
    if nombre in contactos:
        while True:
            nuevo_telefono = input("Introduce el nuevo número de teléfono (máximo 11 dígitos): ").strip()
            if nuevo_telefono.isdigit() and len(nuevo_telefono) <= 11:
                break
            else:
                print("Número de teléfono inválido.")
        
        contactos[nombre] = nuevo_telefono
        print(f"Contacto {nombre} actualizado con éxito.")
    else:
        print("El contacto no existe.")

def eliminar_contacto(contactos):
    nombre = input("Introduce el nombre del contacto a eliminar: ").strip()
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto {nombre} eliminado con éxito.")
    else:
        print("El contacto no existe.")

def buscar_contacto(contactos):
    nombre = input("Introduce el nombre del contacto a buscar: ").strip()
    if nombre in contactos:
        print(f"{nombre}: {contactos[nombre]}")
    else:
        print("El contacto no existe.")

def main():
    contactos = {} 

    while True:
        print("\nAgenda de Contactos")
        print("1. Agregar contacto")
        print("2. Actualizar contacto")
        print("3. Eliminar contacto")
        print("4. Buscar contacto")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            actualizar_contacto(contactos)
        elif opcion == "3":
            eliminar_contacto(contactos)
        elif opcion == "4":
            buscar_contacto(contactos)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
