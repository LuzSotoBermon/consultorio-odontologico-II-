import funciones.globales as fg
from modules.tarifas import calcular_valor
from datetime import datetime

def AddData(key, cedula, data):
    """Guarda los datos en memoria, permitiendo múltiples citas por cliente"""
    if key not in fg.citas:
        fg.citas[key] = {}

    if cedula not in fg.citas[key]:
        fg.citas[key][cedula] = []

    # Evitar citas duplicadas
    for cita in fg.citas[key][cedula]:
        if cita["tipoAtencion"].lower() == data["tipoAtencion"].lower() and cita["fechaCita"] == data["fechaCita"]:
            print("Ya existe una cita para este cliente con el mismo procedimiento y fecha.")
            return

    fg.citas[key][cedula].append(data)


def registrar_cita():
    try:
        # --- Cédula ---
        while True:
            cedula = input('Ingrese la cédula del cliente: ').strip()
            if not cedula.isdigit():
                print("La cédula debe contener solo números.")
            elif len(cedula) < 5:
                print("La cédula es demasiado corta.")
            else:
                break

        # --- Nombre ---
        while True:
            nombre = input('Ingrese el nombre del cliente: ').strip().title()
            if not nombre.replace(" ", "").isalpha():
                print("El nombre solo debe contener letras.")
            else:
                break

        # --- Teléfono ---
        while True:
            telefono = input('Ingrese el teléfono del cliente: ').strip()
            if not telefono.isdigit() or len(telefono) < 7:
                print("El teléfono debe ser numérico y de al menos 7 dígitos.")
            else:
                break

        # --- Tipo de cliente ---
        tipos_cliente = ["PARTICULAR", "EPS", "PREPAGADA"]
        while True:
            tipoCliente = input('Tipo de Cliente (Particular/EPS/Prepagada): ').strip().upper()
            if tipoCliente not in tipos_cliente:
                print(f"Tipo de cliente inválido. Debe ser: {', '.join(tipos_cliente)}")
            else:
                break

        # --- Tipo de atención ---
        tipos_atencion = ["Limpieza", "Calzas", "Extracción", "Diagnóstico"]
        while True:
            tipoAtencion = input('Tipo de Atención (Limpieza/Calzas/Extracción/Diagnóstico): ').strip().capitalize()
            if tipoAtencion not in tipos_atencion:
                print(f"Tipo de atención inválida. Debe ser: {', '.join(tipos_atencion)}")
            else:
                break

        # --- Prioridad ---
        prioridades = ["Normal", "Urgente"]
        while True:
            prioridad = input('Prioridad de Atención (Normal/Urgente): ').strip().capitalize()
            if prioridad not in prioridades:
                print(f"Prioridad inválida. Debe ser: {', '.join(prioridades)}")
            else:
                break

        # --- Fecha ---
        while True:
            fechaCita = input('Fecha de la cita (dd-mm-yyyy): ').strip()
            try:
                datetime.strptime(fechaCita, "%d-%m-%Y")
                break
            except ValueError:
                print("Fecha inválida. Use el formato dd-mm-yyyy.")

        # --- Calcular valor ---
        valor_cita = calcular_valor(tipoCliente, tipoAtencion)

        # --- Guardar cita ---
        cita = {
            'cedula': cedula,
            'nombre': nombre,
            'telefono': telefono,
            'tipoCliente': tipoCliente.capitalize(),
            'tipoAtencion': tipoAtencion,
            'prioridad': prioridad,
            'fechaCita': fechaCita,
            'valor': valor_cita
        }

        AddData('data_citas', cedula, cita)
        print(f"\n✅ Cita registrada correctamente. Valor a pagar: ${valor_cita:,}\n")

    except Exception as e:
        print(f'Error inesperado: {e}')


def mostrar_resumen():
    if 'data_citas' not in fg.citas or not fg.citas['data_citas']:
        print("No hay citas registradas.")
        return

    citas = [c for cliente in fg.citas['data_citas'].values() for c in cliente]

    total_clientes = len(set(c['cedula'] for c in citas))
    ingresos_totales = sum(c['valor'] for c in citas)
    extracciones = sum(1 for c in citas if c['tipoAtencion'].lower() == "extracción")

    print("\n📊 RESUMEN DEL CONSULTORIO ")
    print(f"Total de clientes: {total_clientes}")
    print(f"Ingresos totales: ${ingresos_totales:,}")
    print(f"Número de clientes con extracción: {extracciones}")


def ordenar_por_valor():
    if 'data_citas' not in fg.citas or not fg.citas['data_citas']:
        print("No hay citas registradas.")
        return []

    citas = [c for cliente in fg.citas['data_citas'].values() for c in cliente]
    citas.sort(key=lambda x: x['valor'], reverse=True)
    return citas


def buscar_por_cedula(cedula):
    cedula = cedula.strip()
    if 'data_citas' not in fg.citas or cedula not in fg.citas['data_citas']:
        return None
    return fg.citas['data_citas'][cedula]


def cancelar_cita():
    cedula = input("Ingrese la cédula del cliente para eliminar cita: ").strip()
    cliente = buscar_por_cedula(cedula)
    if not cliente:
        print("\n⚠️ Cliente no encontrado.\n")
        return

    print("\nSeleccione la cita a eliminar:")
    for i, c in enumerate(cliente, start=1):
        print(f"{i}. {c['tipoAtencion']} - Fecha: {c['fechaCita']} - Valor: ${c['valor']:,}")

    while True:
        seleccion = input("Ingrese el número de la cita a eliminar: ").strip()
        if not seleccion.isdigit() or int(seleccion) < 1 or int(seleccion) > len(cliente):
            print("Selección inválida, intente de nuevo.")
        else:
            break

    # Eliminar cita seleccionada
    del fg.citas['data_citas'][cedula][int(seleccion)-1]

    # Si no quedan citas del cliente, eliminar la cédula
    if not fg.citas['data_citas'][cedula]:
        del fg.citas['data_citas'][cedula]

    print("\n✅ Cita eliminada correctamente.\n")
