import csv
import os

def generar_reporte():
    if not os.path.exists("registro_callcenter.csv"):
        print("No hay datos para analizar")
        return

    total_llamadas = 0
    consultas = 0
    reclamos = 0
    por_agente = {}

    with open("registro_callcenter.csv", "r", newline="") as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Encabezados

        for cliente, caso, fecha, hora, agente in lector:
            total_llamadas += 1

            if caso == "consulta":
                consultas += 1
            elif caso == "reclamo":
                reclamos += 1

            if agente not in por_agente:
                por_agente[agente] = 1
            else:
                por_agente[agente] += 1

    print("\n📊 REPORTE AUTOMÁTICO")
    print(f"Total llamadas: {total_llamadas}")
    print(f"Consultas: {consultas}")
    print(f"Reclamos: {reclamos}")

    print("\n📞 Llamadas por agente:")
    for agente, cantidad in por_agente.items():
        print(f"{agente}: {cantidad}")

generar_reporte()