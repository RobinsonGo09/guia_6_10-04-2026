import time


def diagnostico_memoria_isp():
    print("====================================================")
    print("   LABORATORIO DE MEMORIA RAM - INGENIERÍA FESC     ")
    print("====================================================")
    time.sleep(1)

    # 1. EL MOMENTO DE LA RESERVA (MEMORIA ESTÁTICA VS DINÁMICA)
    # Imaginemos que 'nodos' es un local en el Ventura Plaza.
    nodos = ["CENTRO", "NORTE"]
    id_inicial = id(nodos)

    print("\n[PASO 1] Inmueble construido en la RAM:")
    print(f" > Contenido: {nodos}")
    print(f" > Dirección (ID): {id_inicial}")
    print(f" > EXPLICACIÓN: Python reservó la 'habitación' {id_inicial}.")
    print("   En este momento, la lista tiene solo 2 elementos.")
    time.sleep(2)

    # 2. LA MUTACIÓN (EL CAMBIO SIN MUDANZA)
    print("\n[PASO 2] Realizando expansión de red en Cúcuta...")
    print(" > Ejecutando: nodos.append('ATALAYA')")
    nodos.append("ATALAYA")
    print(" > Ejecutando: nodos.insert(0, 'SUR')")
    nodos.insert(0, "SUR")
    time.sleep(2)

    # 3. VERIFICACIÓN DE LA 'PLACA DE INVENTARIO'
    id_final = id(nodos)

    print("\n[PASO 3] Verificación de ubicación post-expansión:")
    print(f" > Nuevo Contenido: {nodos}")
    print(f" > Dirección Final (ID): {id_final}")
    time.sleep(1)

    # 4. LA CONCLUSIÓN TÉCNICA (EL 'PORQUÉ' PARA EL INGENIERO)
    print("\n" + "=" * 52)
    print("         INFORME TÉCNICO DE MUTABILIDAD")
    print("=" * 52)

    if id_inicial == id_final:
        print(" RESULTADO: EL ID ES IDÉNTICO ✅")
        print("-" * 52)
        print(" ¿QUÉ SIGNIFICA ESTO PARA UN INGENIERO?")
        print(" 1. No hubo 'Mudanza': Los datos crecieron pero")
        print("    se quedaron en la misma dirección de memoria.")
        print(" 2. Eficiencia: Python no gastó recursos creando")
        print("    una lista nueva; recicló la que ya existía.")
        print(" 3. Mutabilidad: Las listas son como un tablero")
        print("    acrílico; puedes borrar y escribir sin tener")
        print("    que cambiar el tablero físico.")
    else:
        print(" RESULTADO: EL ID CAMBIÓ ❌")

    print("=" * 52)


if __name__ == "__main__":
    diagnostico_memoria_isp()