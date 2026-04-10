# =================================================================
# 1. CAPA DE DATOS (PERSISTENCIA EN MEMORIA)
# =================================================================
# Esta lista centraliza todos los nodos. Al usar una lista, pasamos
# de variables sueltas a un contenedor dinámico y organizado.
nodos_activos = ["NODO_CENTRO", "NODO_ATALAYA", "NODO_LIBERTAD"]


# =================================================================
# 2. CAPA DE OPERACIONES (LÓGICA DEL SISTEMA)
# =================================================================

def registrar_nodo():
    """
    [SCRIPT 1: Protocolo de Inserción y Sanitización]
    Objetivo: Evitar que entren datos 'sucios' o duplicados al sistema.
    """
    print("\n--- REGISTRO DE NUEVO NODO TÉCNICO ---")
    entrada = input("Identificador del servidor (Ej: Nodo Norte): ")

    # PASO 1: Sanitización (Limpieza de datos)
    # .strip() quita espacios accidentales; .upper() estandariza a mayúsculas
    nodo_validado = entrada.strip().upper()

    # PASO 2: Validación de Integridad
    if nodo_validado == "":
        print("❌ ERROR: El campo no puede quedar vacío.")
    elif nodo_validado in nodos_activos:
        # Aquí resolvemos el Problema 1: Redundancia
        print(f"❌ ALERTA: El nodo '{nodo_validado}' ya existe. Violación de Unicidad.")
    else:
        # PASO 3: Almacenamiento Dinámico
        nodos_activos.append(nodo_validado)
        print(f"✅ ÉXITO: Nodo '{nodo_validado}' registrado en la infraestructura.")


def dar_de_baja_nodo():
    """
    [SCRIPT 2: Gestión de Memoria y Depuración]
    Objetivo: Eliminar equipos de la red de forma segura.
    """
    if not nodos_activos:
        print("\n⚠️ AVISO: No hay nodos activos para dar de baja.")
        return

    print("\n--- GESTIÓN DE BAJAS TÉCNICAS (DECOMMISSION) ---")
    print("1. Retirar por NOMBRE (Eliminación por valor)")
    print("2. Retirar por RACK (Eliminación por índice)")
    opcion = input("Seleccione método de retiro: ")

    if opcion == "1":
        target = input("Escriba el nombre exacto del nodo: ").strip().upper()
        if target in nodos_activos:
            # .remove() busca el objeto y lo destruye de la memoria
            nodos_activos.remove(target)
            print(f"✅ DESINCORPORADO: El nodo '{target}' ha sido retirado.")
        else:
            print("❌ ERROR: El nombre no coincide con ningún equipo activo.")

    elif opcion == "2":
        try:
            # Mostramos el límite actual para evitar errores del estudiante
            limite = len(nodos_activos) - 1
            idx = int(input(f"Ingrese número de rack (0 a {limite}): "))

            # .pop() extrae el elemento de esa posición específica
            eliminado = nodos_activos.pop(idx)
            print(f"✅ RACK LIBERADO: Se retiró el equipo '{eliminado}' de la posición {idx}.")
        except:
            print("❌ ERROR: Posición inválida o fuera de rango técnico.")


def generar_reporte():
    """
    [SCRIPT 3: Reporte de Disponibilidad e Iteración]
    Objetivo: Visualizar el estado de toda la red de forma escalable.
    """
    print("\n" + "=" * 60)
    print(f"{'ID RACK':<10} | {'IDENTIFICADOR TÉCNICO':<25} | {'ESTADO'}")
    print("-" * 60)

    # Verificamos si hay datos para evitar reportes vacíos
    if not nodos_activos:
        print(f"{'--':<10} | {'SIN EQUIPOS DETECTADOS':<25} | {'OFFLINE'}")
    else:
        # El ciclo 'for' con 'enumerate' genera el reporte bilingüe y numerado
        for i, nodo in enumerate(nodos_activos):
            # Simulamos que cada nodo en la lista está operativo
            print(f"{i:<10} | {nodo:<25} | ONLINE / EN LÍNEA")

    print("=" * 60)
    print(f"TOTAL NODOS MONITOREADOS: {len(nodos_activos)}")


# =================================================================
# 3. INTERFAZ DE USUARIO (ORQUESTADOR)
# =================================================================

def menu_principal():
    """Mantiene el sistema operativo y gestiona la navegación."""
    while True:
        print("\n--- MONITOR DE RED ISP CÚCUTA v2.0 ---")
        print("1. Registrar Nodo (Insertar)")
        print("2. Dar de Baja (Eliminar)")
        print("3. Generar Reporte (Listar)")
        print("4. Salir del Sistema")

        op = input("\nSeleccione acción: ")

        if op == "1":
            registrar_nodo()
        elif op == "2":
            dar_de_baja_nodo()
        elif op == "3":
            generar_reporte()
        elif op == "4":
            print("Finalizando monitoreo... Conexión cerrada.")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")


# Punto de arranque del software
if __name__ == "__main__":
    menu_principal()