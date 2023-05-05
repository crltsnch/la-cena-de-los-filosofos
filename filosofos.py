import time
import threading
import random

N=5  #numero de filosofos que se sentarán en la  mesa
tiempo_total = 3 #tiempo que durara la cena, por tanto el tiempo que durara la ejecucion del programa

class filosofo(threading.Thread):
