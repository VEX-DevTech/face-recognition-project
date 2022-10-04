# LOGGER BASE SERÁ UTILIZADA PARA TENER UN REGISTRO DE QUIEN INGRESO A LA BIBLIOTECA #

####################################################################################
# LIBRERIAS A UTILIZAR #
import logging as log
import os
import sys

####################################################################################
app_path = os.path.dirname(sys.executable)
log.basicConfig(level = log.DEBUG,
                format = "%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s",
                datefmt = "%I:%M:%S %p",
                handlers = [
                    log.FileHandler("files/Data/registro_actividad.log"),
                    log.StreamHandler()
                ])