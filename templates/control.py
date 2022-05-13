from templates.bd import ob_con

def guardar(evento, dia, mes, year):
    conexion = ob_con()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO evento(evento, dia, mes, year) VALUES (%s, %s, %s, %s)",
                       (evento, dia, mes, year))
        conexion.commit()
        conexion.close()

def obtenerEv():
    conexion = ob_con()
    agendar = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT evento, dia, mes, year FROM evento ")
        agendar = cursor.fetchall()
        conexion.close()
        return agendar