import modules.citas as mc
import modules.cola as cola

def menu():
    while True:
        print("""
        ----------------------------
          CONSULTORIO ODONTOLÓGICO
        ----------------------------
        1. Registrar cita
        2. Mostrar resumen
        3. Mostrar clientes ordenados por valor
        4. Buscar cliente por cédula
        5. Cancelar cita
        6. Generar cola de urgencias
        7. Mostrar cola de urgencias
        8. Atender cliente de urgencia
        9. Salir
        """)
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mc.registrar_cita()
        
        elif opcion == "2":
            mc.mostrar_resumen()
        
        elif opcion == "3":
            citas = mc.ordenar_por_valor()
            if citas:
                for c in citas:
                    print(f"{c['cedula']} - {c['nombre']} - {c['tipoCliente']} - "
                          f"{c['tipoAtencion']} - Valor: ${c['valor']:,}")
            else:
                print("\n⚠️ No hay citas registradas.\n")
        
        elif opcion == "4":
            cedula = input("Ingrese la cédula a buscar: ")
            cliente = mc.buscar_por_cedula(cedula)
            if cliente:
                print("\n✅ Cliente encontrado:\n")
                for c in cliente:
                    print(f" Cédula: {c['cedula']}")
                    print(f" Nombre: {c['nombre']}")
                    print(f" Teléfono: {c['telefono']}")
                    print(f" Tipo de cliente: {c['tipoCliente']}")
                    print(f" Tipo de atención: {c['tipoAtencion']}")
                    print(f" Prioridad: {c['prioridad']}")
                    print(f" Fecha de cita: {c['fechaCita']}")
                    print(f" Valor: ${c['valor']:,}\n")
            else:
                print("\n⚠️ Cliente no encontrado.\n")

        elif opcion == "5":
            mc.cancelar_cita()  

        elif opcion == "6":
            cola.generar_cola()
        elif opcion == "7":
            cola.mostrar_cola()
        elif opcion == "8":
            cola.atender_cliente()

        elif opcion == "9":
            print("👋 Saliendo del sistema...")
            break
        
        else:
            print("⚠️ Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
