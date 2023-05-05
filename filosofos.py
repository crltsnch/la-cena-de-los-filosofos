import time
import threading
import random

N=5  #numero de filosofos que se sentarán en la  mesa
tiempo_total = 3 #tiempo que durara la cena, por tanto el tiempo que durara la ejecucion del programa

class filosofo(threading.Thread):
    semaforo = threading.Lock()  #semaforo binario que asegura la exclusión mutua entre filósofos al intentar tomar los tenedores
    estado = []   #lista que almacena el estado de cada filosofo 'PENSANDO', 'HAMBRIENTO' o 'COMIENDO'
    tenedores = []   #lista de semaforos para sincronizar el uso de los tenedores entre los filosofos. Muestra quien esta en cola para uasr el tenedor
    count = 0   #contador que lleva la cuenta del numero de filosofos que se han creado.

    def __init__(self):
        super().__init__()   #herencia, se llama al constructor de la clase padre ('Threand') usando el método super()
        self.id = filosofo.count   #se le asigna un id al filosofo de count
        filosofo.count+=1   #y se incrementa el contador de filosofos
        filosofo.estado.append('PENSANDO')   #se añade el estado del filosofo a la lista de estados, en estado pensando.
        filosofo.tenedores.append(threading.Semaphore(0))   #se crea un semaforo para su tenedor izquierdo y se añade a la lista de tenedores
        print("Filosofo {0} - PENSANDO".format(self.id))   #mensaje en la consolo indicando que el filosofo esta pensando
    
    