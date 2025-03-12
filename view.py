import tkinter as tk
from tkinter import messagebox

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title("Aplicación de Banco")

        self.label_titular = tk.Label(self.ventana, text="Titular:")
        self.label_titular.pack()

        self.entry_titular = tk.Entry(self.ventana)
        self.entry_titular.pack()

        self.label_cantidad = tk.Label(self.ventana, text="Cantidad:")
        self.label_cantidad.pack()

        self.entry_cantidad = tk.Entry(self.ventana)
        self.entry_cantidad.pack()

        self.boton_depositar = tk.Button(self.ventana, text="Depositar", command=self.depositar)
        self.boton_depositar.pack()

        self.boton_retirar = tk.Button(self.ventana, text="Retirar", command=self.retirar)
        self.boton_retirar.pack()

        self.boton_saldo = tk.Button(self.ventana, text="Obtener Saldo", command=self.mostrar_saldo)
        self.boton_saldo.pack()

    def depositar(self):
        titular = self.entry_titular.get()
        cantidad = float(self.entry_cantidad.get())
        if self.controlador.depositar(titular, cantidad):
            messagebox.showinfo("Éxito", "Depósito realizado con éxito.")
        else:
            messagebox.showerror("Error", "Error al realizar el depósito.")

    def retirar(self):
        titular = self.entry_titular.get()
        cantidad = float(self.entry_cantidad.get())
        if self.controlador.retirar(titular, cantidad):
            messagebox.showinfo("Éxito", "Retiro realizado con éxito.")
        else:
            messagebox.showerror("Error", "Error al realizar el retiro.")

    def mostrar_saldo(self):
        titular = self.entry_titular.get()
        saldo = self.controlador.obtener_saldo(titular)
        messagebox.showinfo("Saldo", f"El saldo de {titular} es: {saldo}")

    def ejecutar(self):
        self.ventana.mainloop()