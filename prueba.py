from urllib import response
import requests
import time
import psycopg2
import threading

def service(connection):
    print("Hola Service")
    get_service(connection)
    

def get_service(conn):
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200 :
        data = response.json()
        for dataout in data:
            title = dataout["title"]
            print(title)
            write_db(conn, title)

    else:
        pass

def connect_db():
    conn = psycopg2.connect(dbname="concurrente", user="postgres", password="steven", host="localhost", port="5432") #psycopg2.connect("dbname=concurrente user=postgres password=steven@555")
    #cur = conn.cursor()
    return conn

def write_db(conn, title):
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO pokemons (title) VALUES ('"+title+"')")
    except Exception as err:
        print(err)
    else:
        conn.commit()

if __name__ == "__main__":
    init_time = time.time()
    connection = connect_db()
    service(connection)
    end_time = time.time() - init_time
    print(end_time)

