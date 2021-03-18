# polimorfismo Python

class  Vehiculo: #Clase padre
    def __init__(self,marca): 
        self.marca = marca
    def Avanzar(self): # Metodo avanzar 
        pass

class Carro (Vehiculo): #Clase hija
    rueda=4
    def Avanzar(self): # Metodo avanzar
        print('El Carro avanza en 4 ruedas')

class Moto (Vehiculo): # Clase hija
    rueda=2
    def Avanzar(self): # Metodo avanzar
        print ('La moto avanza en  2 ruedas')

class Camion (Vehiculo): # Clase hija 
    rueda=10
    def Avanzar(self): # Metodo avanzar 
        print ('El camion avanza en  10 ruedas')


objetoUno = Carro('Ford') 
objetoUno.Avanzar() 

objetoDos = Moto('Honda') 
objetoDos.Avanzar() 

objetoTres = Camion('Chevrolet') 
objetoTres.Avanzar() 



