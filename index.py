import tkinter as tk
from tkinter import messagebox, filedialog

def turing_abb(cadena):
    estado = 'q0'
    i = 0 
    while i < len(cadena):
        if estado == 'q0':
            if cadena[i] == 'a':
                estado = 'q1'
                i += 1
            else:
                return False
        elif estado == 'q1':
            if cadena[i] == 'b':
                estado = 'q2'
                i += 1
            else:
                return False    
        elif estado == 'q2':
            if cadena[i] == 'b':
                estado = 'q3'
                i += 1
            else:
                return False  
        elif estado == 'q3':
            if i < len(cadena) and cadena[i] == 'a':
                estado = 'q1'
                i += 1
            elif i == len(cadena):
                return True
            else:
                return False
    return estado == 'q3'                            

def validar_cadena():
    cadena = entry.get()
    if turing_abb(cadena):
        messagebox.showinfo("Resultado", f"La cadena '{cadena}' es válida.\n")
    else:
        messagebox.showerror("Resultado", f"La cadena '{cadena}' es inválida.\n")

def cargar_archivo():
    archivo_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if archivo_path:
        with open(archivo_path, 'r') as archivo:
            lineas = archivo.readlines()
            resultados = []
            for linea in lineas:
                cadena = linea.strip() 
                if turing_abb(cadena):
                    resultados.append(f"La cadena '{cadena}' es válida.\n")
                    resultados.append(f"*************************************\n")
                else:
                    resultados.append(f"La cadena '{cadena}' es inválida.\n")
            

            messagebox.showinfo("Resultados", "".join(resultados))

root = tk.Tk()
root.title("Validador de cadenas - Máquina de Turing")

label = tk.Label(root, text="Ingrese una cadena o cargue un archivo:", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

button_validar = tk.Button(root, text="Validar", command=validar_cadena, font=("Arial", 14))
button_validar.pack(pady=10)

button_archivo = tk.Button(root, text="Cargar archivo", command=cargar_archivo, font=("Arial", 14))
button_archivo.pack(pady=10)

root.mainloop()
