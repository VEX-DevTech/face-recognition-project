# CLASE PARA EL ENTRENAMIENTO DE ROSTROS #
# (EJECUTAR DESPUÉS DE CAPTURAR NUEVOS ROSTROS)

###########################################################################################
# LIBRERIAS A UTILIZAR #
import cv2
import os
import numpy as np

###########################################################################################
# CLASE PRINCIPAL PARA EL ENTRENAMIENTO #
class FaceTraining:
    # MÉTODO CONSTRUCTOR DE LA CLASE #
    def __init__(self):
        # LECTURA DE ROSTROS #
        self.path_data = "files/faceCaptions"
        self.lista_personas = os.listdir(self.path_data)

        self.etiquetas = []
        self.data_rostros = []
        contador_etiqueta = 0

        for nombre_persona in self.lista_personas:
            persona_path = f"{self.path_data}/{nombre_persona}"
            print("Leyendo las Imágenes...")

            for archivo_jpg in os.listdir(persona_path):
                print(f"Rostros: {nombre_persona}/{archivo_jpg}")
                self.etiquetas.append(contador_etiqueta)
                self.data_rostros.append(cv2.imread(f"{persona_path}/{archivo_jpg}", 0))
                imagen = cv2.imread(f"{persona_path}/{archivo_jpg}", 0)

            contador_etiqueta += 1

        self.entrenar()

    
    # ENTRENAR LOS ROSTROS #
    def entrenar(self):
        # 
        sistema = cv2.face.EigenFaceRecognizer_create()

        print("Entrenando...")
        sistema.train(self.data_rostros, np.array(self.etiquetas))


        sistema.write("files/Data/entrenamiento.xml")
        print("Modelo almacenado...")