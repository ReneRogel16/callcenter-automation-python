import csv
import os

ARCHIVO = "registro_callcenter.csv"

def generar_reporte():
    if not os.path.exists(ARCHIVO):
        print("❌ No existe el archivo de registros.")
        return

    total_llamadas = 0
    consultas = 0
    reclamos = 0
    llamadas_por_agente = {}

    with open(ARCHIVO, "r", newline="", encoding="latin-1") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            total_llamadas += 1

            if fila["Caso"] == "consulta":
                consultas += 1
            elif fila["Caso"] == "reclamo":
                reclamos += 1

            agente = fila["Agente"]
            llamadas_por_agente[agente] = llamadas_por_agente.get(agente, 0) + 1

    print("\n📊 REPORTE AUTOMÁTICO")
    print(f"Total llamadas: {total_llamadas}")
    print(f"Consultas: {consultas}")
    print(f"Reclamos: {reclamos}")

    print("\n📞 Llamadas por agente:")
    for agente, cantidad in llamadas_por_agente.items():
        print(f"{agente}: {cantidad}")

generar_reporte()
