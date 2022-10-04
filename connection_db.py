import sqlite3

class ConexionDB:
    # INFORMACIÓN PARA LA BASE DE DATOS
    _DATABASE = "files/Data/face_recognition.db"
    _CREATE_DB = "CREATE TABLE alumnos(cedula_alumno VARCHAR(10) UNIQUE, nombre_alumno VARCHAR(20), apellido_alumno VARCHAR(20))"
    
    def __init__(self):
        self._conectar = None
        self._cursor = None

    def __enter__(self):
        self._conectar = sqlite3.connect(self._DATABASE)
        self._cursor = self._conectar.cursor()

        try:
            self._cursor.execute(self._CREATE_DB)
        except sqlite3.OperationalError:
            pass

        return self._cursor

    # HACEMOS COMMIT DE LA TRANSACCIÓN DESEADA #
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self._conectar.rollback()
            print(f"Ocurrió una Excepción, se hizo rollback: {exc_val}")
        else:
            self._conectar.commit()
            print("Se hizo commit de la transacción")

        self._conectar.close()