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
    
    def __del__(self):
        print("Filosofo {0} - Se para de la mesa".format(self.id))  #este metodo se llama cuando el objeto de la clase filosofo se elimina de la memoria, es decir, cuando el hilo termina.
    
    def pensar(self):
        time.sleep(random.randint(0, 5))   #el filosofo piensa durante un tiempo aleatorio entre 0 y 5 segundos, esto lo necesitamos para que los filosofos tomen un tiempo antes de intentar coger los tenedores y, por tanto, evitar el bloqueo mutuo.
    
    def derecha(self, i):
        return (i-1)%N   #devuelve el indice del filósofo que se encuentra a la derecha del filósofo 'i' en la mesa. Cuando el filosofo quiera tomar el tenedor de su derecha, necesita saber el filosofo que esta a su derecha para comprobar si este esta comiendo o no y por tanto saber si el fislofo i puede tomar el tenedor.
    
    def izquierda(self, i):
        return (i+1)%N   #lo mismo que la funcion derecha, pero para el tenedor de la izquierda
    
   