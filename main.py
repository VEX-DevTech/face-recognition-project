# SISTEMA DE RECONOCIMIENTO FACIAL CON EIGEN FACES #
# ALUMNO: ERICK VINUEZA #
# MATERIAS: PROGRAMACIÓN VISUAL I, PROYECTOS INFORMÁTICOS, LABORATORIOS #

#######################################################################################
# LIBRERIAS A UTILIZAR #
import tkinter as tk
from tkinter import PhotoImage, ttk, messagebox
import shutil
# CLASES A UTILIZAR #
from Querys import Querys
from face_captions import FaceCaptions
from face_training import FaceTraining
from eigen_recognition import EigenRecognition
from logger_base import log

#######################################################################################
# CLASE PARA LA CARATULA DEL PROGRAMA #
class VentanaCaratula(tk.Tk):
    # MÉTODO CONSTRUCTOR DE LA CLASE #
    def __init__(self):
        super().__init__()
        # Configuración de la Ventana
        self.title("DESARROLLADO POR VED - 2022")
        self.iconbitmap("files/images/icono_intesud.ico")
        
        ancho_ventana = 700
        alto_ventana = 650
        x_ventana = self.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}"

        self.geometry(posicion)
        self.resizable(0, 0)

        # Creación de los widgets
        self.crear_caratula()

    
    # CREAR LA CARATULA DE INGRESO AL PROGRAMA #
    def crear_caratula(self):
        # Imagen del Instituto para la caratula
        self.caratula_intesud = PhotoImage(file="files/images/logo_intesud.png")
        label_caratula = ttk.Label(self, image=self.caratula_intesud)
        label_caratula.grid(column=0, row=0, padx= 50, pady=15, columnspan=2)

        # Titulo, nombre, materias, etc...
        label_nombre_proyecto = ttk.Label(self, text="SISTEMA DE RECONOCIMIENTO FACIAL PARA LA BIBLIOTECA DEL INTESUD", font=("Arial", 13, "bold"))
        label_materia = ttk.Label(self, text="PROGRAMACIÓN VISUAL - ADMINISTRACIÓN DE REDES", font=("Arial", 13, "bold"))
        label_nombre_alumno = ttk.Label(self, text="ALUMNO: ERICK VINUEZA", font=("Arial", 13, "bold"))
        label_nombre_profesores = ttk.Label(self, text="PROFESORES: ING. FABRIZIO VILLASIS - TNLGO. CRISTIAN MOROCHO", font=("Arial", 13, "bold"))
        
        label_nombre_proyecto.grid(column=0, row=1, padx= 50, columnspan=2)
        label_materia.grid(column=0, row=2, padx= 50, pady=15, columnspan=2)
        label_nombre_alumno.grid(column=0, row=3, padx= 50, columnspan=2)
        label_nombre_profesores.grid(column=0, row=4, padx= 50, pady=15, columnspan=2)

        # Imagen de Presentación...
        self.coding_image = PhotoImage(file="files/images/coding.png")
        label_coding_image = ttk.Label(self, image=self.coding_image)
        label_coding_image.grid(column=0, row=5, padx= 70, columnspan=2, sticky="e")

        # Boton de Ingreso
        boton_ingreso = ttk.Button(self, text="Iniciar el Programa", command=self.entrar_login)
        boton_ingreso.grid(column=0, row=6, padx=50, columnspan=2, sticky="n")


    # ENTRAR AL LOGIN PRINCIPAL #
    def entrar_login(self):
        self.destroy()
        ventana_login = VentanaIdentificacion()
        ventana_login.mainloop()

#####################################################################################
# CLASE PARA LA VENTANA DE LOGIN #
class VentanaIdentificacion(tk.Tk):
    # MÉTODO CONSTRUCTOR DE LA CLASE #
    def __init__(self):
        super().__init__()
        # Configuración de la Ventana
        self.title("Librería INTESUD")
        self.iconbitmap("files/images/icono_intesud.ico")
        
        ancho_ventana = 315
        alto_ventana = 320
        x_ventana = self.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}"

        self.geometry(posicion)
        self.resizable(0, 0)

        # Creación de los widgets
        self.crear_tabuladores_login()
        

    # CREAR TABULADORES (PESTAÑAS) PARA EL LOGIN Y REGISTRO #
    def crear_tabuladores_login(self):
        # Control de los tabuladores
        control_tabulador = ttk.Notebook(self)
        
        # Imagen Instituto
        self.imagen_intesud = PhotoImage(file="files/images/logo_intesud.png")

        # Login
        tabulador_login = ttk.Frame(control_tabulador)
        control_tabulador.add(tabulador_login, text="  Reconocimiento  ")
        control_tabulador.pack(fill="both")
        self.crear_componentes_login(tabulador_login, self.imagen_intesud)

        # Registro
        tabulador_registro = ttk.Frame(control_tabulador)
        control_tabulador.add(tabulador_registro, text="   Registrate   ")
        control_tabulador.pack(fill="both")
        self.crear_componentes_registro(tabulador_registro, self.imagen_intesud)

        # Administración
        tabulador_admin = ttk.Frame(control_tabulador)
        control_tabulador.add(tabulador_admin, text="  Panel Administrativo  ")
        control_tabulador.pack(fill="both")
        self.crear_componentes_admin(tabulador_admin, self.imagen_intesud)


    # CREAR LOS COMPONENTES DEL LOGIN #
    def crear_componentes_login(self, tabulador, imagen):
        # Etiquetas de Logo, Nombre, Apellido, Texto de Ayuda
        label_imagen = ttk.Label(tabulador, image=imagen)
        label_texto_ayuda = ttk.Label(tabulador, text="Para acceder al reconocimiento\nIngrese los datos solicitados.")
        label_nombre = ttk.Label(tabulador, text="Nombre:", justify=tk.RIGHT)
        label_apellido = ttk.Label(tabulador, text="Apellido:", justify=tk.RIGHT)
        
        label_imagen.grid(column=0, row=0, pady=3, columnspan=2)
        label_texto_ayuda.grid(column=0, row=1, pady=8, columnspan=2)
        label_nombre.grid(column=0, row=2, pady=8, ipadx=5, sticky="e")
        label_apellido.grid(column=0, row=3, ipadx=5, sticky="e")

        # Entrada de Texto para Nombre y Apellido
        self.entrada_nombre_login = ttk.Entry(tabulador, width=40)
        self.entrada_apellido_login = ttk.Entry(tabulador, width=40)

        self.entrada_nombre_login.grid(column=1, row=2,sticky="w")
        self.entrada_apellido_login.grid(column=1, row=3, sticky="w")

        # Boton Comprobación
        boton_comprobar = ttk.Button(tabulador, text="Comprobar Identidad", command=self.comprobar_identidad)
        boton_comprobar.grid(column=0, row=4, columnspan=2, pady=20)


    # CREAR COMPONENTES DEL REGISTRO #
    def crear_componentes_registro(self, tabulador, imagen):
        # Etiquetas de Logo, Nombre, Apellido, Texto de Ayuda
        label_imagen = ttk.Label(tabulador, image=imagen)
        label_texto_ayuda = ttk.Label(tabulador, text="¿Aún no se encuentra registrado?\nIngrese sus datos a continuación:")
        label_nombre = ttk.Label(tabulador, text="Nombre:", justify=tk.RIGHT)
        label_apellido = ttk.Label(tabulador, text="Apellido:", justify=tk.RIGHT)
        label_cedula = ttk.Label(tabulador, text="Cédula:", justify=tk.RIGHT)
        label_pin = ttk.Label(tabulador, text="PIN:", justify=tk.RIGHT)
        label_ayuda_pin = ttk.Label(tabulador, text="Solicitar en Administración.", font=("Arial Rounded MT Negrita", 9))

        label_imagen.grid(column=0, row=0, pady=3, columnspan=2)
        label_texto_ayuda.grid(column=0, row=1, pady=8, columnspan=2)
        label_nombre.grid(column=0, row=2, ipadx=5, sticky="e")
        label_apellido.grid(column=0, row=3, pady=8, ipadx=5, sticky="e")
        label_cedula.grid(column=0, row=4, ipadx=5, sticky="e")
        label_pin.grid(column=0, row=5, pady=8, ipadx=5, sticky="e")
        label_ayuda_pin.grid(column=1, row=6, sticky="w")

        # Entrada de Texto para Nombre, Apellido y Cédula
        self.entrada_nombre_registro = ttk.Entry(tabulador, width=40)
        self.entrada_apellido_registro = ttk.Entry(tabulador, width=40)
        self.entrada_cedula_registro = ttk.Entry(tabulador, width=40)
        self.entrada_pin_registro = ttk.Entry(tabulador, width=23, show="*")

        self.entrada_nombre_registro.grid(column=1, row=2, sticky="w")
        self.entrada_apellido_registro.grid(column=1, row=3, sticky="w")
        self.entrada_cedula_registro.grid(column=1, row=4, sticky="w")
        self.entrada_pin_registro.grid(column=1, row=5, sticky="w")

        # Boton de Carga Imagen y Registro
        boton_registro = ttk.Button(tabulador, text="Registrarse", command=self.registrar_nuevo_alumno)
        boton_registro.grid(column=0, row=7, columnspan=2, pady=15)


    # CREAR COMPONENTES DEL LOGIN DE ADMINISTRACIÓN #
    def crear_componentes_admin(self, tabulador, imagen):
        # Etiquetas de Logo, Usuario, Password y Texto de Ayuda
        label_imagen = ttk.Label(tabulador, image=imagen)
        label_texto_ayuda = ttk.Label(tabulador, text="Solo personal autorizado.", justify=tk.RIGHT)
        label_usuario = ttk.Label(tabulador, text="Usuario:", justify=tk.RIGHT)
        label_password = ttk.Label(tabulador, text="Clave:", justify=tk.RIGHT)
        
        label_imagen.grid(column=0, row=0, pady=3, columnspan=2)
        label_texto_ayuda.grid(column=0, row=1, pady=8, columnspan=2)
        label_usuario.grid(column=0, row=2, pady=8, ipadx=5, sticky="e")
        label_password.grid(column=0, row=3, ipadx=5, sticky="e")

        # Entrada de Texto para Usuario y Password
        self.entrada_usuario_admin = ttk.Entry(tabulador, width=40)
        self.entrada_password_admin = ttk.Entry(tabulador, width=40, show="*")

        self.entrada_usuario_admin.grid(column=1, row=2,sticky="w")
        self.entrada_password_admin.grid(column=1, row=3, sticky="w")

        # Boton de Ingreso
        boton_ingreso = ttk.Button(tabulador, text="Ingresar", command=self.verificar_panel_admin)
        boton_ingreso.grid(column=0, row=4, columnspan=2, pady=20)
    

    # COMPROBAR EL NOMBRE Y APELLIDO INGRESADO EN EL LOGIN #
    def comprobar_identidad(self):
        # Crear una conexión a base de datos
        registros =  Querys.seleccionar()

        nombre_usuario = self.entrada_nombre_login.get()
        apellido_usuario = self.entrada_apellido_login.get()
        
        nombres = []
        apellidos = []
        bandera = False

        for registro in registros:
            nombres.append(registro[1])
            apellidos.append(registro[2])

        for nombre in nombres:
            if nombre_usuario == nombre:
                for apellido in apellidos:
                    if apellido_usuario == apellido:
                        bandera = True
                        messagebox.showinfo("Proceso de Reconocimiento Facial", 
                        f"{nombre_usuario} {apellido_usuario}, porfavor identifiquese en la camara.")
                        self.borrar_entradas(self.entrada_nombre_login, self.entrada_apellido_login)
                        EigenRecognition(nombre_usuario, apellido_usuario)
                        break
                        
        if bandera == False:
            messagebox.showerror("Acceso NO Concedido",
            "Los datos ingresados no coinciden en la base de datos, revise e intentelo de nuevo.")


    # REGISTRAR A UN NUEVO ALUMNO EN LA BASE DE DATOS #
    def registrar_nuevo_alumno(self):
        nombre_usuario = self.entrada_nombre_registro.get()
        apellido_usuario = self.entrada_apellido_registro.get()
        cedula_usuario = self.entrada_cedula_registro.get()
        pin_ingresado = self.entrada_pin_registro.get()
        pin_registro = "admin"

        if pin_ingresado == pin_registro:
            if nombre_usuario and apellido_usuario and cedula_usuario != "":
                # Proceso de base de datos y captura de los rostros
                FaceCaptions(nombre_usuario, apellido_usuario, cedula_usuario)
                # Finalización del proceso
                self.borrar_entradas(self.entrada_nombre_registro, self.entrada_apellido_registro, self.entrada_cedula_registro, self.entrada_pin_registro)
            else:
                messagebox.showerror("Registro Inválido",
                "Al parecer ha dejado uno de los campos vacíos, revise e intentelo nuevamente.")
        else:
            messagebox.showerror("PIN Inválido",
            "No podemos realizar el registro porque el PIN ingresado no es el correcto.")

    
    # VERIFICAR EL USUARIO Y PASSWORD INGRESADO EN EL LOGIN DE ADMINISTRACIÓN #
    def verificar_panel_admin(self):
        usuario_ingresado = self.entrada_usuario_admin.get()
        password_ingresado = self.entrada_password_admin.get()
        usuario_admin = "root"
        password_admin = "cisco"

        if usuario_ingresado == usuario_admin and password_ingresado == password_admin:
            messagebox.showinfo("Notificación de Seguridad", "El acceso de personal no autorizado será penalizado.")
            self.destroy()
            ventana_admin = VentanaAdmin()
            ventana_admin.mainloop()
        else:
            messagebox.showerror("Datos Inválidos",
            "Entradas Incorrectas.")
        
    
    # BORRAR LAS ENTRADAS INGRESADAS #
    def borrar_entradas(self, entrada_nombre, entrada_apellido, entrada_cedula=None, entrada_pin_registro=None):    
        entrada_nombre.delete(0, tk.END)
        entrada_apellido.delete(0, tk.END)
        if entrada_cedula is not None:
            entrada_cedula.delete(0, tk.END)
            entrada_pin_registro.delete(0, tk.END)


####################################################################################
# CLASE PARA LA VENTANA ADMINISTRATIVA #
class VentanaAdmin(tk.Tk):
    # MÉTODO CONSTRUCTOR DE LA CLASE #
    def __init__(self):
        super().__init__()
        # Configuración de la Ventana
        self.title("Panel Administrativo")
        self.iconbitmap("files/images/icono_intesud.ico")
        
        ancho_ventana = 500
        alto_ventana = 310
        x_ventana = self.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}"

        self.geometry(posicion)
        self.resizable(0, 0)

        # Creación de los widgets
        self.crear_panel_administracion()


    # CREAR LOS COMPONENTES PARA EL PANEL DE ADMINISTRACIÓN #
    def crear_panel_administracion(self):
        self.imagen = PhotoImage(file="files/images/logo_intesud.png")
        label_caratula = ttk.Label(self, image=self.imagen)
        label_caratula.grid(column=0, row=0, pady=10, padx=100, columnspan=4)

        # Label y Entrada para buscar registro por cédula
        label_guia = ttk.Label(self, text="Para actualizar o eliminar un registro primero busquelo y asegurese de que existe.")
        label_cedula = ttk.Label(self, text="Número de Cédula:", font=("Arial", 10, "bold"))

        label_guia.grid(column=0, row=2, columnspan=4, padx=10, sticky="w")
        label_cedula.grid(column=0, row=3, padx=10, sticky="w")
        
        self.entrada_buscar = ttk.Entry(self, width=25)
        self.entrada_buscar.grid(column=1, row=3, sticky="w")

        # Boton Buscar
        boton_buscar = ttk.Button(self, text="Buscar", command=self.buscar)
        boton_buscar.grid(column=2, row=3)

        # Boton Actualizar
        boton_actualizar = ttk.Button(self, text="Actualizar Registro", command=self.actualizar)
        boton_actualizar.grid(column=3, row=3)

        # Tabla de busqueda
        self.tabla_cedula = ttk.Entry(self, width=20)
        self.tabla_nombre = ttk.Entry(self, width=20)
        self.tabla_apellido = ttk.Entry(self, width=20)

        self.tabla_cedula.grid(column=0, row=4, padx=10, pady=10)
        self.tabla_cedula.configure(state="disabled")
        self.tabla_nombre.grid(column=1, row=4)
        self.tabla_nombre.configure(state="disabled")
        self.tabla_apellido.grid(column=2, row=4, pady=10, columnspan=2, sticky="w")
        self.tabla_apellido.configure(state="disabled")

        # Boton Seleccionar
        boton_seleccionar = ttk.Button(self, text="Visualizar Registros", command=self.seleccionar)
        boton_seleccionar.grid(column=0, row=5, padx=10, pady=10, columnspan=4, sticky="w")

        # Boton Eliminar
        boton_eliminar = ttk.Button(self, text="Eliminar Registro", command=self.eliminar)
        boton_eliminar.grid(column=0, row=6, padx=10, columnspan=4, sticky="w")

        # Boton Entrenar
        boton_entrenar = ttk.Button(self, text="Entrenar Rostros Registrados", command=self.entrenar)
        boton_entrenar.grid(column=0, row=7, padx=10, pady=10, columnspan=4, sticky="w")

        # Boton Regresar al Login
        boton_regresar_login = ttk.Button(self, text="REGRESAR AL LOGIN", command=self.regresar_login)
        boton_regresar_login.grid(column=0, row=8, padx=10, columnspan=4, sticky="w")


    # BUSCAR UN REGISTRO EN LA BASE DE DATOS POR CÉDULA #
    def buscar(self):
        try:
            # Habilitamos las casillas para poder colocar el contenido
            self.tabla_cedula.configure(state="enabled")
            self.tabla_nombre.configure(state="enabled")
            self.tabla_apellido.configure(state="enabled")
            # Primero se vacían las casillas por si acaso
            self.tabla_cedula.delete(0, tk.END)
            self.tabla_nombre.delete(0, tk.END)
            self.tabla_apellido.delete(0, tk.END)
            # Cogemos el contenido de la caja de busqueda y hacemos la consulta
            self.cedula_buscada = self.entrada_buscar.get()
            self.registro =  Querys.buscar(self.cedula_buscada)
            # Insertamos el contenido en las casillas
            self.tabla_cedula.insert(tk.END, f"{self.registro[0][0]}")
            self.tabla_nombre.insert(tk.END, f"{self.registro[0][1]}")
            self.tabla_apellido.insert(tk.END, f"{self.registro[0][2]}")
            # Deshabilitamos nuevamente las casillas
            self.tabla_cedula.configure(state="disabled")
            self.tabla_nombre.configure(state="disabled")
            self.tabla_apellido.configure(state="disabled")
        except Exception as e:
            messagebox.showwarning("", "No se han encontrado registros que coincidan")
            # Deshabilitamos nuevamente las casillas
            self.tabla_cedula.configure(state="disabled")
            self.tabla_nombre.configure(state="disabled")
            self.tabla_apellido.configure(state="disabled")


    # LLAMADO A LA VENTANA DE ACTUALIZAR REGISTROS #
    def actualizar(self):
            cedula = self.entrada_buscar.get()
            if cedula != "":
                self.destroy()
                ventana_actualizar = VentanaActualizar(cedula)
                ventana_actualizar.mainloop()
            else:
                messagebox.showerror("", "No se ha seleccionado un registro")


    # LLAMADO A LA VENTANA DE SELECCIONAR REGISTROS #    
    def seleccionar(self):
        self.destroy()
        ventana_seleccionar = VentanaSeleccionar()
        ventana_seleccionar.mainloop()


    # ELIMINAR UN REGISTRO EN ESPECIFICO #    
    def eliminar(self):
        try:
            confirmacion = messagebox.askokcancel(message="¿Seguro que desea eliminar?", title="Confirmación")
            if confirmacion == True:
                cedula = self.entrada_buscar.get()
                registro = Querys.buscar(cedula)
                nombre = registro[0][1]
                apellido = registro[0][2]
                path_alumno = f"files/faceCaptions/{nombre}{apellido}"
                shutil.rmtree(path_alumno)
                Querys.eliminar(cedula)
                messagebox.showinfo("Registro Eliminado", f"Con CI: {cedula}")
            else:
                pass
        except Exception as e:
            messagebox.showerror("Error", f"{e}")


    # ENTRENAR ROSTROS QUE ESTEN REGISTRADOS ESE MOMENTO #
    def entrenar(self):
        try:
            messagebox.showinfo("Empezando el Entrenamiento", "El proceso puede demorar algunos minutos...")
            FaceTraining()
            messagebox.showinfo("Todo ha salido bien", "Rostros entrenados, comunique a los alumnos")

        except Exception as e:
            messagebox.showerror("Algo salió mal", f"Comuniquese con el desarrollador: \n{e}")
        
    
    # REGRESAR A LA VENTANA PRINCIPAL DEL RECONOCIMIENTO #
    def regresar_login(self):
        self.destroy()
        ventana_login = VentanaIdentificacion()
        ventana_login.mainloop()


#######################################################################################
# CLASE PARA LA VENTANA DE SELECCIONAR Y VISUALIZAR REGISTROS #
class VentanaSeleccionar(tk.Tk):
    # MÉTODO CONSTRUCTOR DE LA CLASE #
    def __init__(self):
        super().__init__()
        # Configuración de la Ventana
        self.title("REGISTROS DE LA BASE DE DATOS")
        self.iconbitmap("files/images/icono_intesud.ico")
        
        ancho_ventana = 600
        alto_ventana = 400
        x_ventana = self.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}"

        self.geometry(posicion)
        self.resizable(0, 0)

        # Creación de los widgets
        self.crear_panel_seleccionar()


    # CREAR LOS COMPONENTES PARA EL PANEL SELECCIONAR #
    def crear_panel_seleccionar(self):
        self.imagen = PhotoImage(file="files/images/logo_intesud.png")
        label_caratula = ttk.Label(self, image=self.imagen)
        label_caratula.grid(column=0, row=0, padx= 100, pady=10, columnspan=4)

        # Query SELECCIONAR
        label_guia_select = ttk.Label(self, text="Estos son todos los alumnos registrados:", font=("Arial", 11, "bold"))
        label_guia_select.grid(column=0, row=1, pady=10, columnspan=2, sticky="w")
        
        try:
            self.lista_registros = Querys.seleccionar()
            self.total_filas = len(self.lista_registros) 
            self.total_columnas = len(self.lista_registros[0])
            
            for i in range(self.total_filas): 
                for j in range(self.total_columnas): 
                    self.entrada = ttk.Entry(self, width=20, font=('Arial', 10, 'bold')) 
                    self.entrada.grid(row=i+2, column=j, sticky="w") 
                    self.entrada.insert(tk.END, f"{self.lista_registros[i][j]}")
                    self.entrada.configure(state='disabled')
        except Exception:
            messagebox.showwarning("", "No se han encontrado registros") 

        boton_volver_admin = ttk.Button(self, text="VOLVER AL PANEL DE ADMINISTRACIÓN", command=self.volver_panel_admin)
        boton_volver_admin.grid(column=0, row=self.total_filas+2, padx=10, pady=20, columnspan=2, sticky="w")


    # VOLVER A LA VENTANA DEL PANEL ADMINISTRATIVO #
    def volver_panel_admin(self):
        self.destroy()
        ventana_admin = VentanaAdmin()
        ventana_admin.mainloop()


############################################################################################
# CLASE PARA LA VENTANA ACTUALIZAR REGISTRO #
class VentanaActualizar(tk.Tk):
    # MÉTODO CONSTRUCTOR DE LA CLASE #
    def __init__(self, cedula):
        super().__init__()
        # Configuración de la Ventana
        self.title("ACTUALIZAR UN REGISTRO")
        self.iconbitmap("files/images/icono_intesud.ico")

        ancho_ventana = 300
        alto_ventana = 200
        x_ventana = self.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}"

        self.geometry(posicion)
        self.resizable(0, 0)

        # Parametro necesario
        self.cedula_usuario = cedula

        # Creación de los widgets
        self.crear_panel_actualizar()


    # CREAR EL PANEL DE ACTUALIZAR UN REGISTRO #
    def crear_panel_actualizar(self):
        self.imagen = PhotoImage(file="files/images/logo_intesud.png")
        label_caratula = ttk.Label(self, image=self.imagen)
        label_caratula.grid(column=0, row=0, pady=10, padx=15, columnspan=2)

        label_actualizar = ttk.Label(self, text="Ingresa los datos solicitados")
        label_actualizar.grid(column=0, row=1, columnspan=2, sticky="w")

        cedula_label = ttk.Label(self, text="Cédula: ")
        nombre_label = ttk.Label(self, text="Nombre: ")
        apellido_label = ttk.Label(self, text="Apellido: ")

        cedula_label.grid(column=0, row=2)
        nombre_label.grid(column=0, row=3)
        apellido_label.grid(column=0, row=4)

        self.entrada_cedula_a = ttk.Entry(self, width=30)
        self.entrada_cedula_a.insert(tk.END, f"{self.cedula_usuario}")
        self.entrada_cedula_a.configure(state="disable")
        self.entrada_nombre_a = ttk.Entry(self, width=30)
        self.entrada_apellido_a = ttk.Entry(self, width=30)
        
        self.entrada_cedula_a.grid(column=1, row=2)
        self.entrada_nombre_a.grid(column=1, row=3)
        self.entrada_apellido_a.grid(column=1, row=4)

        boton_actualizar = ttk.Button(self, text="ACTUALIZAR", command=self.actualizar)
        boton_volver = ttk.Button(self, text="VOLVER", command=self.volver_panel_admin)
        
        boton_actualizar.grid(column=0, row=5, pady=10)
        boton_volver.grid(column=1, row=5, pady=10)


    # ACTUALIZAR UN REGISTRO #
    def actualizar(self):
        cedula = self.entrada_cedula_a.get()
        nombre_nuevo = self.entrada_nombre_a.get()     
        apellido_nuevo = self.entrada_apellido_a.get()
        try:
            Querys.actualizar(nombre_nuevo, apellido_nuevo, cedula)
            messagebox.showinfo("", "Registro Actualizado Correctamente")
        except Exception:
            messagebox.showerror("", "Ha ocurrido un error verifica que la cédula ingresada sea la correcta")

    # VOLVER AL PANEL DE ADMINISTRACIÓN #
    def volver_panel_admin(self):
        self.destroy()
        ventana_admin = VentanaAdmin()
        ventana_admin.mainloop()

############################################################################################
# TESTING DE LA APLICACIÓN #
if __name__ == "__main__":
    ejecutar = VentanaCaratula()
    ejecutar.mainloop()