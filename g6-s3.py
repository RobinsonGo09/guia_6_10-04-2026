# =================================================================
# SCRIPT 3: MODELO CRUD PARA GESTIÓN DE TRÁNSITO (AVANCE 6)
# =================================================================

# CAPA DE DATOS: Sustituimos múltiples variables por una colección dinámica.
# Esta lista centraliza todos los registros en un único bloque de memoria.
inventario_transito = ["HGT210", "JUR456", "KLO987"]


def mostrar_inventario():
    """
    CAPA DE VISUALIZACIÓN (READ):
    Genera un reporte técnico estructurado y bilingüe.
    """
    # El '\n' salta una línea y '=' * 40 dibuja una línea divisoria estética.
    print("\n" + "=" * 40)

    # FORMATO F-STRING: :<5 alinea a la izquierda con 5 espacios de reserva.
    # :<20 alinea la placa reservando 20 espacios para mantener la verticalidad.
    print(f"{'#':<5} | {'PLACA REGISTRADA':<20}")
    print("-" * 40)

    # TÉCNICA DE ITERACIÓN: 'enumerate' extrae simultáneamente el índice (i)
    # y el valor (placa), evitando el uso de contadores manuales externos.
    for i, placa in enumerate(inventario_transito):
        # Imprime la fila actual alineada exactamente con el encabezado superior.
        print(f"{i:<5} | {placa:<20}")

    print("=" * 40)

    # FUNCIÓN LEN(): Retorna la cardinalidad (cantidad total) de la lista.
    print(f"Total registros / Total records: {len(inventario_transito)}")


def registrar_placa():
    """
    CAPA DE INSERCIÓN (CREATE):
    Gestiona la entrada de datos aplicando protocolos de seguridad e integridad.
    """
    # SANITIZACIÓN: .strip() elimina espacios basura y .upper() normaliza a mayúsculas.
    # Esto garantiza que ' hgt210 ' y 'HGT210' se traten como el mismo dato.
    nueva = input("\nIngrese nueva placa a registrar: ").strip().upper()

    # VALIDACIÓN DE INTEGRIDAD:
    # 1. 'nueva' verifica que el usuario no envíe un dato vacío.
    # 2. 'not in' busca en la lista para evitar la redundancia (duplicados).
    if nueva and nueva not in inventario_transito:
        # MÉTODO APPEND: Inserta el nuevo elemento al final de la estructura mutable.
        inventario_transito.append(nueva)
        print("✅ Registro exitoso / Success.")
    else:
        # Respuesta ante fallos de validación o datos redundantes.
        print("❌ Error: Placa duplicada o inválida.")


# =================================================================
# EJECUCIÓN DEL SISTEMA (FLUJO OPERATIVO)
# =================================================================

# 1. Estado inicial del inventario
mostrar_inventario()

# 2. Interacción con el usuario para nueva persistencia de datos
registrar_placa()

# 3. Estado final para verificar la actualización de la lista en RAM
mostrar_inventario()