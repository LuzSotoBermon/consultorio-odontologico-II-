from funciones.globales import citas, cola_urgencias
from datetime import datetime
from collections import deque

def generar_cola():
    global cola_urgencias
    if "data_citas" not in citas:
        print("\n⚠️ No hay citas registradas.")
        return

    # Filtrar solo extracciones urgentes
    urgencias = [
        c for cliente in citas["data_citas"].values() for c in cliente
        if c["tipoAtencion"].lower() == "extracción" and c["prioridad"].lower() == "urgente"
    ]

    # Ordenar por fecha más cercana
    urgencias.sort(key=lambda x: datetime.strptime(x["fechaCita"], "%d-%m-%Y"))

    # Crear la cola con deque
    cola_urgencias = deque(urgencias)
    print("\n✅ Cola de urgencias generada correctamente.")


def mostrar_cola():
    if not cola_urgencias:
        print("\n⚠️ No hay clientes en la cola de urgencias.")
        return
    print("\n📋 Informe de cola de urgencias:")
    for i, c in enumerate(cola_urgencias, start=1):
        print(f"{i}. {c['nombre']} | Cédula: {c['cedula']} | Fecha: {c['fechaCita']} | Tel: {c['telefono']}")


def atender_cliente():
    if not cola_urgencias:
        print("\n⚠️ No hay clientes por atender.")
        return
    cliente = cola_urgencias.popleft()
    print(f"\n✅ Atendido cliente: {cliente['nombre']} (Cédula: {cliente['cedula']})")
