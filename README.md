# la cena de los filosofos

El link a mi repositorio es: [GitHub](https://github.com/crltsnch/la-cena-de-los-filosofos)

#Archivo `filosofos.py`

```
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
        print("Filosofo {0} - Se para de la mesa".format(self.id))  #este metodo se llama cuando el objeto de la clase filosofo se elimina de la memoria, es decir, cuando el hilo termina
    
    def pensar(self):
        time.sleep(random.randint(0, 5))   #el filosofo piensa durante un tiempo aleatorio entre 0 y 5 segundos, esto lo necesitamos para que los filosofos tomen un tiempo antes de intentar coger los tenedores y, por tanto, evitar el bloqueo mutuo
    
    def derecha(self, i):
        return (i-1)%N   #devuelve el indice del filósofo que se encuentra a la derecha del filósofo 'i' en la mesa. Cuando el filosofo quiera tomar el tenedor de su derecha, necesita saber el filosofo que esta a su derecha para comprobar si este esta comiendo o no y por tanto saber si el fislofo i puede tomar el tenedor
    
    def izquierda(self, i):
        return (i+1)%N   #lo mismo que la funcion derecha, pero para el tenedor de la izquierda
    
    def verificar(self, i):
        if filosofo.estado[i] == 'HAMBRIENTO' and filosofo.estado[self.izquierda(i)] != 'COMIENDO' and filosofo.estado[self.derecha(i)] != 'COMIENDO':   #si el filosofo (el que está ejecutando el hilo) esta hambriento y los filosofos de su izquierda y derecha no estan comiendo, entonces el filosofo puede cambiar de estado a comiendo.
            filosofo.estado[i] = 'COMIENDO'
            filosofo.tenedores[i].release()   #se libera el semaforo del tenedor del filosofo i, es decir, el filosofo i puede tomar los tenedores.
    
    def tomar(self):
        filosofo.semaforo.acquire()  #se adquiere el semaforo binario para asegurar la exclusión mutua entre filósofos al intentar tomar los tenedores. Si el filosofo esta comiendo, otro filosofo que quiera comer tendra que esperar
        filosofo.estado[self.id] = 'HAMBRIENTO'   #el filosofo cambia su estado a hambriento
        self.verificar(self.id)   #se comprueba si el filosofo puede tomar ambos tenedores para comer
        filosofo.semaforo.release()  #si puede comer, el filosofo libera el semáforo, deja de intentar tomar los tenedores y pasa a estar comeindo.
        filosofo.tenedores[self.id].acquire()  #si puede tomarlos, el filósofo asquiere el bloqueo de ambos tenedores, ambos tenedores están disponibles y el filósofo puede comenzar a comer
    
    def soltar(self):
        filosofo.semaforo.acquire()  #infica que el filósofo comenzará a soltar los tenedores y se asegura de que ningun otro filósofo pueda acceder a ellos hasta que el actual termine de soltarlos
        filosofo.estado[self.id] = 'PENSANDO'   #el filosofo cambia su estado a pensando
        self.verificar((self.id + 1) % filosofo.n)  #se comprueba si el filosofo de la derecha puede comer, llamando a la función verificar. Si el id del filosofo de la derecha es n entonces pasamos al indice 0
        self.verificar((self.id - 1 + filosofo.n) % filosofo.n)  #igual que antes pero para el filosofo de la izquierda. Si el id del filosofo de la izquierda es -1 entonces pasamos al indice n-1
        filosofo.semaforo.release()  #el filosofo termina de soltar los tenedores y libera el semaforo para que otro filosofo pueda tomarlos, libera el acceso al recurso compartido
    
    def comer(self):
        print("Filosofo {} comiendo".format(self.id))  #indica que el filósofo está comiendo
        time.sleep(2)   #introduce un retraso enla ejecución simulando el tiempño que el filósofo necesita para comer, en este caso 2 segundos
        print("Filosofo {} termina de comer".format(self.id))  #indica que el filósofo ha terminado de comer

    def run(self):   #cuando se inicia un nuevo hilo
        for i in range(tiempo_total):
            self.pensar()   #el filósofo piensa
            self.tomar()   #el filósofo toma los tenedores
            self.comer()   #el filósofo come
            self.soltar()   #el filósofo suelta los tenedores

def main():
    lista = []  #lista que almacena los filosofos
    for i in range(N):
        lista.append(filosofo())   #añadimos el filosofo a la lista
    
    for f in lista:  #recorremos la lista de filosofos
        f.start()  #se inicia el hilo del filosofo
    
    for f in lista:   
        f.join()   #después de iniciar todos los hilos, esto asegura que todos los filósofos terminen de comer antes de que finalice el programa
    
if __name__ == "__main__":
    main()

```
