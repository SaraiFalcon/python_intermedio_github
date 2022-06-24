from .connection import get_connection #importamos la función para conectarnos

def is_authenticated(usuario, password): 
    conn, cur = get_connection()
    consulta = f"SELECT username, password FROM usuarios where username = \'{usuario}\' AND password = \'{password}\';" 

    cur.execute(consulta)
    usuario_encontrado = cur.fetchone()

    result = None #guarda el resultado seteado en none por si no hay nada 
    if usuario_encontrado:
        result = usuario_encontrado

    cur.close()
    conn.close()

    return result