def registro_notas(Nnotas):
    if Nnotas <=5:
        print
        notas = []
        Tnotas = 0
        print("\nLa nota ingresada debe ser entre 0 y 10.")
    
        for i in range(Nnotas):
            while True:
                nota = float(input(f"Ingrese la nota {i+1}: "))
                if 0 <= nota <= 10:
                   notas.append(nota)
                   Tnotas += nota
                   break
                else:
                   print("Error: La nota debe ser entre 0 y 10. Intente nuevamente.")
    return notas, Tnotas

def mostrar_resumen(materia, notas, promedio):
    print(f"\nMateria: {materia}")
    print(f"Tus notas son: {notas}")
    print(f"Este es su promedio: {promedio:.2f}")
    
    if promedio >= 7:
        print("\n⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻")
        print(f"                 ¡Felicidades! Has aprobado {materia}.")
        print("⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼")
    else:
        print("\n⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻")
        print(f"                  Lo siento, no has aprobado {materia}.")
        print("⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼\n")

def certificado(materia, promedio):
    import random
    import datetime
    n = random.randint(100, 999)
    hoy = datetime.date.today()
    fecha = hoy.strftime("%d/%m/%Y")
    if promedio >= 7:
        print("")
        certi = input("¿Desea imprimir su certificado de notas? (Si/No): ")
        if certi == "si" or certi == "Si":
            print("\n...............................................................................")
            print("|============================================================================|")
            print("|                    CERTIFICADO DE APROBACION DE MATERIA                    |")
            print("|============================================================================|")
            print("|                      NOMBRE DEL COLEGIO O UNIVERSIDAD                      |")
            print("|                           Departamento Academico                           |")
            print("|                               Quito, Ecuador                               |")
            print("|                                                                            |")
            print(f"|                            Certificado N° {n}                              |")
            print("|                                                                            |")
            print(f"|Fecha: {fecha}                                                           |")
            print("|                                                                            |")
            print("|----------------------------------------------------------------------------|")
            print("|                                                                            |")
            print(f"|Se certifica que el estudiante ha aprobado la materia:                      |\n|Materia: {materia}")
            print(f"|Promedio Final: {promedio:05.2f}                                                       |")
            print("|                                                                            |")
            print("|Por la presente se otorga este certificado al estudiante como reconocimiento|\n|de su desempeño academico.                                                  |")
            print("|                                                                            |")
            print("|¡Felicidades! El estudiante ha aprobado la materia con éxito.               |")
            print("|                                                                            |")
            print("|----------------------------------------------------------------------------|")
            print("|                                                                            |")
            print("|                           ______________________                           |")
            print("|                             Firma del profesor                             |")
            print("|============================================================================|")
            print("")
        elif certi == "no" or certi == "No":
            print("-------------------------------------------------------------------------------")
            print("Ok, no se generara el certificado.\n")
        else:
            print("Respuesta no valida. No se generara el certificado.")

def Promedio_Certificado():
    while True:
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("1.- Proceso de certificado")
        print("2.- Regresar a inicio")
        print("-------------------------------------------------------------------------------")
        op = input("Seleccione una opcion: ")
        if op == "1":
            print("-------------------------------------------------------------------------------")
            materia = input("\nIntroduzca el nombre de la materia: ")
            print("")
            while True:
                Nnotas = int(input(f"¿Cuantas notas desea ingresar para {materia}? (Un maximo hasta 5 notas) "))
                if Nnotas <=5:
                    notas, Tnotas = registro_notas(Nnotas)
                    promedio = Tnotas / Nnotas
                    mostrar_resumen(materia, notas, promedio)
                    certificado(materia, promedio)
                    break
                else:
                    print("Solo puede ingresar 5 notas.")
        elif op == "2":
            print("-------------------------------------------------------------------------------")
            print("\n                              Regresando...\n")
            break
        else:
            print("Opcion no valida. Por favor, elige una opción valida.")
