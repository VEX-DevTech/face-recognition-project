# CLASE PARA EL RECONOCIMIENTO FACIAL CON EIGEN FACES #
# (EJECUTAR UNICAMENTE CUANDO YA SE HAYA ENTRENADO LOS ROSTROS) #

######################################################################################
# LIBRERIAS A UTILIZAR #
import cv2
import os
from tkinter import messagebox
from logger_base import log

#######################################################################################
# CLASE PRINCIPAL DEL RECONOCIMIENTO #
class EigenRecognition:
    # MÉTODO CONSTRUCTOR DE LA CLASE #
    def __init__(self, nombre, apellido):
        self.nombre_persona = nombre
        self.apellido_persona = apellido

        # Ruta donde se almacenaron las 300 fotos
        self.path_data = "files/faceCaptions"
        self.path_imagenes = os.listdir(self.path_data)

        # Llamado al sistema de reconocimiento y al archivo de entrenamiento
        self.sistema = cv2.face.EigenFaceRecognizer_create()
        self.sistema.read("files/Data/entrenamiento.xml")

        # Captura de video vía streaming
        self.cap_video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        # Llamado al archivo de cv2 para clasificar los rostros (haarcascade_frontalface_default.xml)
        self.clasificacion_rostros = cv2.CascadeClassifier(f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml")
        
        # Llamado al método reconocer para comenzar el proceso
        self.reconocer()


    # RECONOCER EL ROSTRO VÍA WEBCAM STREAMING #
    def reconocer(self):
        # Bucle Principal
        reconocido = 0
        while reconocido != 30:
            # Validaciones principales y Bandera
            ret, frame = self.cap_video.read()
            if ret == False: break
            
            # Pasamos el frame actual a gris para poder reconocer
            frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Realizamos una copia del frame gris para luego compararlo
            frame_aux = frame_gris.copy()

            # Almacenamos todos los rostros entrenados en escala de grises
            rostros = self.clasificacion_rostros.detectMultiScale(frame_gris, 1.3, 5)

            # Ciclo for comparativo con cada uno de los rostros entrenados
            for(x, y, w, h) in rostros:
                rostro = frame_aux[y:y+h, x:x+w]
                rostro = cv2.resize(rostro, (150, 150), interpolation= cv2.INTER_CUBIC)
                # Le pedimos al sistema de reconocimiento que analice el rostro actual
                resultado = self.sistema.predict(rostro)

                #cv2.putText(frame,f"{resultado}" ,(x,y-5) ,1 ,1.3 ,(255,255,0) ,1 ,cv2.LINE_AA)

                # Comparativa de resultados, si son menos a 5700 el rostro es conocido
                if resultado[1] < 5400:
                    cv2.putText(frame,"Reconocido permaneza unos segundos",(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                    reconocido += 1
                else:
                    cv2.putText(frame,"Desconocido ubiquese bien",(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)

            cv2.imshow("Ventana de Verificacion de Identidad - Para cancelar presione ESC", frame)
            k = cv2.waitKey(1)
            if k == 27: break
        
        if reconocido >= 30:
            messagebox.showinfo("Reconocimiento Exitoso", "Bienvenido, puedes ingresar a la biblioteca.")
            log.debug(f"LOGIN: El alumno {self.nombre_persona} {self.apellido_persona} ingreso a la biblioteca.")
        else:
            messagebox.showerror("Reconocimiento Inválido", "No se ha reconocido el rostro, por lo tanto no puede ingresar")

        self.cap_video.release()
        cv2.destroyAllWindows()