import os, msvcrt, time
trabajadores = []
cargos = ("CEO","DESARROLLADOR","ANALISTA")
def limpiar_pantalla():
    time.sleep(3)

def esperar_t():
    print('>>>Presione tecla para continuar<<<')
    msvcrt.getch()

def limpiar_p():
    os.system
    
#################################

def opc_1():
        print("registrar trabajador")
        nombre_apellido = input("ingrese nombre y su apellido: ")
        cargo = int(input("ingrese su cargo (1.CEO, 2.DESARROLLADOR, 3:ANALISTA)"))
        sueldo_b = int(input("ingrese sueldo bruto: "))
        desc_salud = round(7/100* sueldo_b)
        desc_afp  = int(12/100*sueldo_b)
        sueldo_liquido = sueldo_b-desc_afp-desc_salud
        trabajador = [nombre_apellido, cargo[cargos-1], sueldo_b, desc_salud, desc_afp,sueldo_liquido]
        trabajadores.append(trabajador)
        print('Trabajador registrado con exito!!')
        esperar_t()
        limpiar_p()
def opc_2():
    if len(trabajadores) == 0:
        print('ERROR NO EXISTEN REGISTROS')
    else:
        print("\tLISTA TRABAJADORES")
        print("TRABAJADOR\tCARGO\tSUELDO BRUTO\DESC.SALUD\DESC.AFP\tLIQUIDO")
        for t in trabajadores: #t = se convierte en el trabajador ya que recorre la lista en base a
            print(f"{t[0]}\t{t[1]}\t{t[2]}\t\t\t{t[3]}\t\t\t{t[4]}\t{t[5]}")
esperar_t()
def opc_3():
    if len(trabajadores) == 0:
        print('lista vacia')
    else:
        opc2 = int(input("¿Qué cargo desea imprimir?(1:CEO, 2:DESARROLLADOR, 3:ANALISTA 4:TODOS)"))
        if opc2==4:
            with open("todos_trabajadores.txt","w", newline= "\n") as archivo:
                for t in trabajadores:
                    texto = f"{t[0]} {t[1]} {t[2]} {t[3]} {t[4]} {t[5]}\n"
                    archivo.write(texto)
            print('Archivo Creado con exito!')
        else:
            with open("trabajadores_por_cargo", "w") as archivo:
                for t in trabajadores:
                    if cargos[opc2-1]==[1]:
                        texto =  f"{t[0]} {t[1]} {t[2]} {t[3]} {t[4]} {t[5]}\n"
                        archivo.write(texto)
    esperar_t()
def opc_4():
    print("hasta luego!")
    exit()
