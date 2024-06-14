import os, time, msvcrt
from funciones1 import *

trabajadores = []

while True:
    print("""
    >MENU TRABAJADORES<
    1) registrar trabajador
    2) listar trabajadores
    3) imprimir plantilla de sueldos
    4) salir""")

    opc = int(input('ingrese opción:'))
    if opc == 1:
        print("registrar trabajador")
        nombre_apellido = input("ingrese nombre y su apellido: ")
        cargo = int(input("ingrese su cargo (1.CEO, 2.DESARROLLADOR, 3:ANALISTA)"))
        sueldo_b = int(input("ingrese sueldo bruto: "))
        desc_salud = round(7/100* sueldo_b)
        desc_afp  = int(12/100*sueldo_b)
        sueldo_liquido = sueldo_b-desc_afp-desc_salud
        trabajador = [nombre_apellido, cargo, sueldo_b, desc_salud, desc_afp,sueldo_liquido]
        trabajadores.append(trabajador)
        print('Trabajador registrado con exito!!')
        esperar_t()
        limpiar_p()
    elif opc == 2:
        pass
        esperar_t()
    elif opc == 3:
        pass
        esperar_t()
    else:
        break