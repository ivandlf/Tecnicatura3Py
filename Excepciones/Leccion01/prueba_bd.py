conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
cursor= conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)  # De esta manera ejecutamos la sentencia
registros = cursor.fetchall()  # Recuperamos los registros que seran una lista
print(registros)

#cursor.close()
#conexion.close()  # Clase 24 abril lunes-lECCION04-  NO CONECTA CON MI BASE DE DATOS PREGUNTAR???
