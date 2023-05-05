
class PlanAhorro:
    __codigo: int
    __modelo:str
    __version:str
    __valor:float
    __cantCuotasPlan:int=0
    __cantCuotasLicita:int=0 
    def __init__(self, codigo, modelo, version,valor,cantCuotasPlan,cantCuotasLicita):
        self.__codigo= codigo
        self.__modelo= modelo
        self.__version=version
        self.__valor=valor
        self.__cantCuotasPlan= cantCuotasPlan
        self.__cantCuotasLicita=cantCuotasLicita

    def get_codigo(self):
        return self.__codigo
    def get_modelo(self):
        return self.__modelo
    def get_version(self):
        return self.__version
    def get_valor(self):
        return self.__valor
    def set_valor(self,valorActual):
        self.__valor = valorActual
    @classmethod
    def get_cantCuotasPlan(cls):
        return cls.__cantCuotasPlan
    @classmethod
    def get_cantCuotasLicita(cls):
        return cls.__cantCuotasLicita
    @classmethod
    def set_cantCuotasLicita(cls,cantnueva):
        cls.__cantCuotasLicita = cantnueva
   
       
