# 🦷 Sistema de Gestión de Citas Odontológicas  

Este proyecto es un programa en **Python** que permite administrar y priorizar citas en un consultorio odontológico. Incluye el manejo de **colas de urgencias**, pensadas para atender prioritariamente a pacientes con extracciones urgentes.  

---

## ✨ Características principales  

- 📌 **Gestión de citas**  
  - Registrar citas con datos del cliente (cédula, nombre, teléfono).  
  - Selección de tipo de cliente: **Particular, EPS, Prepagada**.  
  - Selección de atención: **Limpieza, Calzas, Extracción, Diagnóstico**.  
  - Definir prioridad: **Normal o Urgente**.  
  - Registro de fecha de la cita.  
  - Cálculo automático del valor según cliente y tipo de atención.  

- 📊 **Resumen de citas**  
  - Total de clientes registrados.  
  - Ingresos totales generados.  
  - Número de clientes con extracción.  

- 🔍 **Gestión avanzada**  
  - Mostrar clientes ordenados por valor de la cita.  
  - Buscar citas por cédula.  
  - Cancelar citas específicas de un cliente.  

- 🚨 **Cola de urgencias**  
  - Generación automática de una **cola prioritaria** con pacientes de **Extracción + Urgente**.  
  - Ordenada cronológicamente (fecha más cercana primero).  
  - Informe de la cola para que la clínica pueda llamar a los pacientes.  
  - Atención en estricto orden mediante estructura **FIFO (cola con deque)**.  

---

## 🛠️ Tecnologías utilizadas  

- Python **3.10+**  
- Módulos estándar: `datetime`, `collections`  

---

---

## 🚀 Instalación y uso  

1. Clonar el repositorio:  
   ```bash
   https://github.com/LuzSotoBermon/consultorio-odontologico-II-.git
