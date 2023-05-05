from classPlanAhorro import PlanAhorro
from gestor import actualizarValor,mostrarPorValor,dadoUnValor,modifCuotasLicit
import csv

if __name__=='__main__':
  
  planes= []
  with open("planes.csv") as archivo:
    reader= csv.reader(archivo, delimiter=';')
    for fila in reader:
        codigo= int(fila[0])
        modelo=fila[1]
        version=fila[2]
        valor= float(fila[3])
        cantCuotasPlan= int(fila[4])
        cantCuotasLicita= int(fila[5])

        plan= PlanAhorro(codigo, modelo, version,valor,cantCuotasPlan,cantCuotasLicita)
        planes.append(plan)         
               
    print(f"--- MENU: ---")
    print(f"[1]. Actualizar el valor del vehículo de cada plan.")
    print(f"[2]. Mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior a cierto valor.")
    print(f"[3]. Mostrar el monto que se debe haber pagado para licitar el vehículo.")
    print(f"[4]. Modificar la cantidad cuotas que debe tener pagas para licitar.")
    print(f"[0]. Salir")
    opcion= int(input("Ingrese el numero de opción que desea realizar: "))
    while opcion != 0:
        if opcion == 1:
            actualizarValor(planes)
        elif opcion == 2: 
            dadoUnValor(planes)
        elif opcion == 3: 
            mostrarPorValor(planes)
        elif opcion == 4:
            modifCuotasLicit(planes)
        else:
            print('Opcion invalida')
        opcion= int(input("Ingrese el numero de opción que desea realizar: "))
