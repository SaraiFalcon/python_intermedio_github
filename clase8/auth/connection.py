import psycopg2

def get_connection(): 
    conn = None
    cur = None
    try:
        conn = psycopg2.connect("dbname=python_intermedio_db user=postgres password=root") #Si se conecta nos regresa la conexión: return conn, cur
        cur = conn.cursor()
    except Exception as e:
        print(e) #si no se conecta va a mandar una excepción y conn y cur como None
    
    return conn, cur