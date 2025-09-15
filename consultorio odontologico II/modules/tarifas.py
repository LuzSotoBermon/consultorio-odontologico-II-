tarifas = {
    "PARTICULAR": {
        "valor_cita": 80000,
        "atencion": {
            "Limpieza": 60000,
            "Calzas": 80000,
            "Extracción": 100000,
            "Diagnóstico": 50000
        }
    },
    "EPS": {
        "valor_cita": 5000,
        "atencion": {
            "Limpieza": 0,
            "Calzas": 40000,
            "Extracción": 40000,
            "Diagnóstico": 0
        }
    },
    "PREPAGADA": {
        "valor_cita": 30000,
        "atencion": {
            "Limpieza": 0,
            "Calzas": 10000,
            "Extracción": 10000,
            "Diagnóstico": 0
        }
    }
}

def calcular_valor(tipoCliente, tipoAtencion):
    """
    Calcula el valor total de la cita: valor base + valor de la atención.
    Funciona sin importar mayúsculas/minúsculas.
    """
    tipoCliente = tipoCliente.strip().upper()
    tipoAtencion = tipoAtencion.strip().capitalize()

    if tipoCliente not in tarifas:
        return 0

    valor_cita = tarifas[tipoCliente]["valor_cita"]
    valor_atencion = tarifas[tipoCliente]["atencion"].get(tipoAtencion, 0)

    return valor_cita + valor_atencion
