# --- SCRIPT 1: CAPA DE SANITIZACIÓN ---

nodos_isp = ["CENTRO", "ATALAYA"] # Datos ya existentes

def agregar_con_limpieza():
    print("\n--- TEST DE SANITIZACIÓN ---")
    # El usuario puede ingresar: "  atalaya  " (con espacios y minúsculas)
    entrada = input("Ingrese nuevo nodo: ")

    # TÉCNICA: Sanitización de cadena
    # .strip() elimina espacios laterales | .upper() estandariza a mayúsculas
    dato_limpio = entrada.strip().upper()

    # TÉCNICA: Validación de Unicidad
    if dato_limpio in nodos_isp:
        print(f"❌ RECHAZADO: El dato '{dato_limpio}' ya existe (Redundancia).")
    elif dato_limpio == "":
        print("❌ RECHAZADO: No se permiten entradas vacías.")
    else:
        nodos_isp.append(dato_limpio)
        print(f"✅ PERSISTIDO: '{dato_limpio}' agregado exitosamente.")

# Ejecución de prueba
agregar_con_limpieza()
print(f"Estado final de la lista: {nodos_isp}")