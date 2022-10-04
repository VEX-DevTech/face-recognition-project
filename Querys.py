from connection_db import ConexionDB

class Querys:
    # CONSULTAS REQUERIDAS #
    _SELECT = "SELECT * FROM alumnos ORDER BY cedula_alumno"
    _INSERT = "INSERT INTO alumnos(cedula_alumno, nombre_alumno, apellido_alumno) VALUES(?, ?, ?)"
    _UPDATE = "UPDATE alumnos SET nombre_alumno = ?, apellido_alumno = ? WHERE cedula_alumno = ?"
    _DELETE = "DELETE FROM alumnos WHERE cedula_alumno = ?"
    _SEARCH = "SELECT * FROM alumnos WHERE cedula_alumno = ?"


    # SELECCIONAR #
    @classmethod
    def seleccionar(cls):
        with ConexionDB() as cursor:
            print("Seleccionando los Usuarios...")
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            return registros


    # INSERTAR #
    @classmethod
    def insertar(cls, cedula, nombre, apellido):
        with ConexionDB() as cursor:
            print(f"Insertando un Alumno: {nombre}")
            valores = (cedula, nombre, apellido)
            cursor.execute(cls._INSERT, valores)
            print(f"Usuarios Insertados: {cursor.rowcount}")


    # ACTUALIZAR #
    @classmethod
    def actualizar(cls, nombre, apellido, cedula):
        with ConexionDB() as cursor:
            print(f"Actualizando un Usuario: {nombre}")
            valores = (nombre, apellido, cedula)
            cursor.execute(cls._UPDATE, valores)
            print(f"Usuario Actualizados: {cursor.rowcount}")


    # ELIMINAR #
    @classmethod
    def eliminar(cls, cedula):
        with ConexionDB() as cursor:
            print(f"Eliminando un Usuario con CI: {cedula}")
            valores = (cedula,)
            cursor.execute(cls._DELETE, valores)
            print(f"Usuarios Eliminados: {cursor.rowcount}")

    # BUSCAR #
    @classmethod
    def buscar(cls, cedula):
        with ConexionDB() as cursor:
            print(f"Buscando un Usuario con CI: {cedula}")
            valores = (cedula,)
            cursor.execute(cls._SEARCH, valores)
            registros = cursor.fetchall()
            return registros