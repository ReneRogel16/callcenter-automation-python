import csv
import os
from datetime import datetime

ARCHIVO = "registro_callcenter.csv"

def clientes_atendidos():
    llamadas = 0
    reclamos = 0
    consultas = 0

    agente = input("Nombre del agente: ").strip().title()

    archivo_existe = os.path.exists(ARCHIVO)

    with open(ARCHIVO, "a", newline="", encoding="latin-1") as archivo:
        escritor = csv.writer(archivo)

        # Encabezados
        if not archivo_existe:
            escritor.writerow(["Cliente", "Caso", "Fecha", "Hora", "Agente"])

        while True:
            accion = input("¿Deseas ingresar datos? (si/no): ").lower()

            if accion == "no":
                break

            if accion == "si":
                cliente = input("Nombre del cliente: ").strip().title()
                caso = input("¿Consulta o Reclamo?: ").lower()

                ahora = datetime.now()
                fecha = ahora.strftime("%Y-%m-%d")
                hora = ahora.strftime("%H:%M:%S")

                if caso == "consulta":
                    consultas += 1
                elif caso == "reclamo":
                    reclamos += 1
                else:
                    print("❌ Caso no válido")
                    continue

                llamadas += 1
                escritor.writerow([cliente, caso, fecha, hora, agente])

    print(f"\nClientes atendidos: {llamadas}")
    print(f"Consultas: {consultas}")
    print(f"Reclamos: {reclamos}")


def menu():
    while True:
        print("\n===== CALL CENTER TOOL =====")
        print("1. Ingreso de datos")
        print("2. Salir")

        opcion = input("Elige una opción (1-2): ")

        if opcion == "1":
            clientes_atendidos()
        elif opcion == "2":
            print("Gracias por usar el programa 👋")
            break
        else:
            print("❌ Opción no válida")

menu()
