##EJERCICIO 7
##definicion de clase abstracta
from abc import ABC, abstractmethod
class Cuenta (ABC):
    ##atributos
    titular = ""
    cantidad = 0.00

    ## MÉTODOS: constructor, getters, setters, mostrar, ingresar, retirar.
    ##constructor
    def __init__self(self, titular, cantidad):
    self.__titular = titular
    self.__cantidad = cantidad
     ##definir setters y getters. atributos privados.
     ## getters
    def get_titular(self):
        return self.__titular

    def get_cantidad(self):
        return self.__cantidad

    ## setter titular
    def set_titular(self, titular):
        self.__titular = titular
    ## setter cantidad
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
 
    ## Método mostrar: muestra los datos de la cuenta. 
    def mostrar(self):
        print ('Estos son los datos de la cuenta:')
        return "Cuenta\n"+"Titular:"+self.titular.mostrar()+" - Cantidad:"+str(self.cantidad)

    ## Método ingresar: se ingresa una cantidad a la cuenta. Si la cantidad introducida es negativa, no se hará nada
    def ingresar(self,cantidad):
        if cantidad >= 0:
            self.__cantidad = self.__cantidad + cantidad
        print ("La cantidad ha sido ingresada correctamente. Total en la cuenta: {}".format(self.__cantidad))
        else
        return ('')

    ## Método retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos. 
    def retirar(self,cantidad):
        if cantidad >= 0:
            self.__cantidad = self.__cantidad - cantidad
        print ("La cantidad ha sido retirada correctamente. Total en la cuenta: {}".format(self.__cantidad))
        else
        return ('')
    ## color rojo en donde? en la cuenta de la resta?? no entendí.


## EJERCICIO 8
## Definir subclase CuentaJoven que deriva de Cuenta
class CuentaJoven (Cuenta):
    ## Bonificación se expresa en porcentaje.
    bonificacion = 0%
    ## MÉTODOS: constructor, setter y getter, es_titular_valido() 
    ## Constructor
    def __init__(self, titular, cantidad, bonificacion):
         super().__init__(self, titular, cantidad)
         self.__bonificacion = bonificacion
    ## Constructor opción 2, con =0 en cantidad y en bonificación
    def __init__(self,titular,cantidad=0,bonificacion=0):
        super().__init__(titular,cantidad)
        self.bonificacion=bonificacion
    ## Getter bonificación
    def get_bonificacion(self):
        return self.__bonificacion

    ## Getter bonificación opción 2, definido como property
    @property
    def bonificacion(self):
        return self.__bonificacion

    ## Setter bonificación
    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    ## Setter bonificación opción 2
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion=bonificacion

    ## Método es_titular_valido()
    def   es_titular_valido():
        if titular >=18 and <25
        self.es_titular_valido
        print ('El titular es válido.')
        else
        print ('El titular no es válido.')

    ##Además, la retirada de dinero sólo se podrá hacer si el titular es válido. //relacionar con retirar. solo retirar si es_titular_valido=true
    def retirar(self,cantidad):
        if not self.es_titular_valido():
            print ("No puedes retirar el dinero. El titular no es válido")
        elif cantidad > 0:
            super().retirar(cantidad)
            print ("La cantidad ha sido retirada correctamente. Total en la cuenta: {}".format(self.__cantidad))
        
   
    ## El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta
    def mostrar(self):
        return "Cuenta Joven\n"+"Titular:"+self.titular.mostrar()+" - Cantidad:"+str(self.cantidad)+ "- Bonificación:"+str(self.bonificacion)+"%"
        
   
  
    
    
