import requests
import time
import psycopg2
import threading
#importc 

try:
    conexion = psycopg2.connect(database='concurrente', user='postgres', password='steven')
    cursor1=conexion.cursor()
    cursor1.execute('select version()')
    version=cursor1.fetchone()
except Exception as err:
    print('Error al conecta a la base de datos')


def service():
    get_service()

def get_service():
    url = "https://jsonplaceholder.typicode.com/photos"
    r = requests.get(url)
    data = r.json()
    photos = data
    return photos
    

def connect_db():
    pass

def close_conexion():
    conexion.close()

def write_db(photos):
    for photo in photos:
        try:
            cursor1.execute("insert into pokemons (name) values ('"+photo["title"]+"')")
        except Exception as err:
            print('Error en la inserción: '+ err)
        else:
            conexion.commit()


tread = threading.Thread(target=get_service, args=())
twrite = threading.Thread(target=write_db, args=(data))

tread.start()
twrite.start()

if __name__ == "__main__":
    init_time = time.time()
    service()
    end_time = time.time() - init_time
    print(end_time)
    