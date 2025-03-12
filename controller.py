# controller.py
from model import Cuenta

class Controlador:
    def __init__(self):
        self.cuentas = {}

    def crear_cuenta(self, titular):
        if titular not in self.cuentas:
            self.cuentas[titular] = Cuenta(titular)

    def depositar(self, titular, cantidad):
        self.crear_cuenta(titular)
        return self.cuentas[titular].depositar(cantidad)

    def retirar(self, titular, cantidad):
        self.crear_cuenta(titular)
        return self.cuentas[titular].retirar(cantidad)

    def obtener_saldo(self, titular):
        self.crear_cuenta(titular)
        return self.cuentas[titular].obtener_saldo()