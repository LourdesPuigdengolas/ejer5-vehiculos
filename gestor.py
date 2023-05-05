    #pasar a un gestor las cuentas y para poder hacer las iteraciones
    # ya que no puedo iterar dentro de la misma clase PlanAhorro 
from classPlanAhorro import PlanAhorro

def actualizarValor(planes):
     for i in range(len(planes)):
        print(f'Codigo: {planes[i].get_codigo()} Modelo: {planes[i].get_modelo()}, Version: {planes[i].get_version()}')
        valorActual = float(input('Ingrese valor actual: '))
        planes[i].set_valor(valorActual)
        print(f'Nuevo valor: {planes[i].get_valor()}')

def dadoUnValor(planes):
    valordado = float(input('Ingrese valor'))
    for plan in enumerate(planes):
        valorcuota = ((plan.get_valor()/plan.get_cantCuotasPlan()) + (plan.get_valor() * 0.10))
        montototal = plan.get_cantCuotasLicita() * valorcuota
        print(f'Codigo: {plan.get_codigo()} Modelo: {plan.get_modelo()}, Version: {plan.get_version()} Monto para licitar: {montototal}')    

def mostrarPorValor(planes):
        for plan in enumerate (planes):
                valorcuota = ((plan.get_valor()/plan.get_cantCuotasPlan()) + (plan.get_valor() * 0.10))
                montototal = plan.get_cantCuotasLicita() * valorcuota
                print(f'Codigo: {plan.get_codigo()} Modelo: {plan.get_modelo()}, Version: {plan.get_version()} Monto para licitar: {montototal}')
        
   
'''def montoLicitacion__mul__(cls):
        montoLi= (cls.__cantCuotasLicita * (cls.importeCuota__add__div__mul__()))
        return print(f"Debe tener pagado ${montoLi} para poder licitar.")
    '''
def  modifCuotasLicit(planes):
        codigobuscar = int(input('Ingrese el codigo del plan: '))
        for plan in enumerate(planes):
                if codigobuscar == plan.get_codigo():
                        cantnueva = int(input('Ingrese la nueva cantidad'))
                        plan.set_cantCuotasLicita(cantnueva)
