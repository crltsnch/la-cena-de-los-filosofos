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