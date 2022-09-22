from threading import Thread, Semaphore
from pytube import YouTube

semaforo = Semaphore(1)
videos=[
    'https://www.youtube.com/watch?v=2iVf6CtcasQ',
    'https://www.youtube.com/watch?v=bo9Z_pgByQY',
    'https://www.youtube.com/watch?v=m6jfZa00vkY',
    'https://www.youtube.com/watch?v=xFxMx7DsqP0',
    'https://www.youtube.com/watch?v=xmPtVflvLh0'
]

def critico(id):
    global x;
    x = x + id
    print("Hilo ="+str(id)+"=>"+str(x))
    x=1

class Hilo(Thread):
    def __init__(self,id,link):
        Thread.__init__(self)
        self.id=id
        self.link=link

    def run(self):
        semaforo.acquire()
        critico(self.id)
        yt = YouTube(self.link)
        yt.streams.first().download()
        print(self.link)
        semaforo.release()

threads_semaphore = []
aux=0
for link in videos:
    hilo=Hilo(aux,link)
    threads_semaphore.append(hilo)
    aux=aux+1
x=1;
print(threads_semaphore)
for t in threads_semaphore:
    t.start()