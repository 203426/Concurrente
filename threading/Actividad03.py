#crear 3 subprocesos que vivan dentro de un proceso
    #descargar 5 videos simultaneos
    #registrar en la base de datos, por lo menos 2k registros
    #iterar un servicio 50 veces
import requests
import threading
from pytube import YouTube
import psycopg2

videos=[
    'https://www.youtube.com/watch?v=2iVf6CtcasQ',
    'https://www.youtube.com/watch?v=bo9Z_pgByQY',
    'https://www.youtube.com/watch?v=m6jfZa00vkY',
    'https://www.youtube.com/watch?v=xFxMx7DsqP0',
    'https://www.youtube.com/watch?v=xmPtVflvLh0'
]

def get_api():
    response= requests.get('https://randomuser.me/api/')
    if response.status_code==200:
        #print(f())
        result = response.json().get('results')
        name=  result[0].get('name').get('first')
        return name
    else: 
        return 'Mala obtención del dato'

def insert_in_db(conn,dato):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO pokemons (title) VALUES ('"+dato+"')")
        print (f'Thread DB: Dato ({dato}) insertado en la base de datos')
    except Exception as err:
        print(err)
    else:
        conn.commit()

def connect_db():
    try:
        conn = psycopg2.connect(dbname="concurrente", user="postgres", password="steven", host="localhost", port="5432") #psycopg2.connect("dbname=concurrente user=postgres password=steven@555")
        #cur = conn.cursor()
        print('Base de datos conectada')
    except Exception as err:
        print('Error al conecta a la base de datos')
    return conn

def download_video(dato,link):
    print(f'Descargando video ({dato+1})...')
    yt = YouTube(link)
    yt.streams.first().download()
    print(f'Video descargado ({dato+1})')

def itetar_vid():
    print('~~~Descargando serie de videos~~~')
    for x in range (0,5):
        th1 = threading.Thread(target=download_video, args=[x,videos[x]]) 
        th1.start()
    print('~~~Serie de videos puestos a desargar~~~')

def iterar_db(db):
    print('Hilo para base datos iniciada')
    for x in range (0,2000):
        dato=get_api()
        insert_in_db(db, dato)
    print('hilo para base de datos cerrada')

def iterar_api():
    print('Hilo para Api iniciada')
    for x in range (0,50):
        print ('Thread API: Dato obtenido de la api',get_api())
    print('Hilo para Api cerrada')


if __name__ == '__main__':
    db = connect_db()
    
    th_videos= threading.Thread(target=itetar_vid())
    th_videos.start()
    
    th_db= threading.Thread(target=iterar_db,args=[db])
    th_db.start()

    th_api = threading.Thread(target=iterar_api)
    th_api.start()