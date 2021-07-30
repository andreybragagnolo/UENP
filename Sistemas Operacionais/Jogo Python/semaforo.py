import time, random
import threading
from threading import Thread

garfo = list()
for i in range(5):
   garfo.append(threading.Semaphore(1))

def filosofo(f):
   f = int(f)
   while True:
      # garfo da esquerda
      garfo[f].acquire()
      # garfo da direita
      garfo[(f + 1) % 5].acquire()
      print ("Filósofo %i comendo..." %f)
      time.sleep(random.randint(1, 5))
      garfo[f].release()
      garfo[(f + 1) % 5].release()
      print ("Filósofo %i pensando..." %f)
      time.sleep(random.randint(1, 10))

for i in range(5):
   print ("Filósofo", i)
   tarefa = Thread(target = filosofo, args = [i])
   tarefa.start()
   
while 1: pass