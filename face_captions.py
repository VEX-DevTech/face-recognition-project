# CLASE PARA LA CAPTURA DE ROSTROS NUEVOS #
# (EJECUTAR ANTES DE ENTRENAR LOS ROSTROS) #

##################################################################################
# LIBRERIAS A UTILIZAR #
import cv2
import os
import imutils
from Querys import Querys
from tkinter import messagebox
from logger_base import log

###################################################################################
# CLASE PRINCIPAL DE LA CAPTURA #
class FaceCaptions:
    # MÉTODO CONSTRUCTOR DE LA CLASE #
    def __init__(self, nombre, apellido, cedula):
        # PATHS POR PERSONA DONDE SE GUARDAN LAS IMÁGENES #
        self.nombre_persona = nombre
        self.apellido_persona = apellido
        self.cedula_persona = cedula
        self.path_data = "files/faceCaptions"
        self.persona_path = f"{self.path_data}/{self.nombre_persona}{self.apellido_persona}"
        self.registrado = False
        registros = Querys.seleccionar()
        cedulas = []
        nombres = []
        apellidos = []
        for registro in registros:
            cedulas.append(registro[0])
            nombres.append(registro[1])
            apellidos.append(registro[2])
        for cedula in cedulas:
            if self.cedula_persona == cedula:
                self.registrado = True
        for nombre in nombres:
            if self.nombre_persona == nombre:
                for apellido in apellidos:
                    if self.apellido_persona == apellido:
                        self.registrado = True
        
        if self.registrado is not True:
            messagebox.showinfo("Captura de Rostros", "Para empezar con el registro, coloquese en la cámara hasta recibir un aviso.")
            if not os.path.exists(self.persona_path):
                os.makedirs(self.persona_path)
                print("Carpeta Creada:", self.persona_path)

            self.capturar_rostro()
        else:
            messagebox.showerror("Datos Inválidos", "El alumno ya se encuentra registrado en la base de datos.")


    # CAPTURAR LOS ROSTROS VÍA WEBCAM STREAMING #
    def capturar_rostro(self):
        # 
        cap_video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        clasificacion_rostros = cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml")
        contador = 0

        # CAPTURA DE LAS 300 IMÁGENES #
        while True:
            ret, frame = cap_video.read()
            if ret == False: break

            frame = imutils.resize(frame, width=640)
            frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame_aux = frame.copy()

            rostros = clasificacion_rostros.detectMultiScale(frame_gris, 1.3, 5)

            for (x, y, w, h) in rostros:
                cv2.putText(frame,"Permanezca Aqui",(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, +h), (0,255,0), 2)
                rostro = frame_aux[y:y+h, x:x+w]
                rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(f"{self.persona_path}/rostro_{contador}.jpg", rostro)
                contador += 1
            cv2.imshow("Ventana de Captura de Rostros - Para cancelar presione ESC", frame)

            k = cv2.waitKey(1)
            if k == 27:
                messagebox.showwarning("Advertencia", "Rostros no capturados, se ha cancelado la captura pero puede intentarlo nuevamente cuando desee")
                break
            if contador >= 300:
                Querys.insertar(self.cedula_persona, self.nombre_persona, self.apellido_persona)
                messagebox.showinfo("Todo ha salido bien",
                "Porfavor espere a que el encargado procese sus datos\nTiempo estimado: 12-24 horas")
                log.debug(f"REGISTRO: El alumno {self.nombre_persona} {self.apellido_persona} se ha registrado.")
                break
        
        cap_video.release()
        cv2.destroyAllWindows()