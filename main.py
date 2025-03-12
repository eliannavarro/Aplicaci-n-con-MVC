# main.py
from controller import Controlador
from view import Vista

if __name__ == "__main__":
    controlador = Controlador()
    vista = Vista(controlador)
    
    vista.ejecutar()