import os, time, msvcrt
from funciones1 import *


while True:
    print("""
    >MENU TRABAJADORES<
    1) registrar trabajador
    2) listar trabajadores
    3) imprimir plantilla de sueldos
    4) salir""")

    opc = int(input('ingrese opción:'))
    if opc == 1:
        opc_1()
    elif opc == 2:
        opc_2()
    elif opc == 3:
        opc_3
    else:
        opc_4()
        limpiar_pantalla