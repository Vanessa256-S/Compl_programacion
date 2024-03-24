#Hecho por: Brayan David Marcelo Espitia y Laura Vanessa Santana Nova
import tkinter as tk

trabajadores = []

def registrar_trabajador():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    cargo = entry_cargo.get()
        
    if nombre and apellido and edad and cargo:  
        trabajadores.append({
            "Nombre": nombre,
            "Apellido": apellido,
            "Edad": edad,
            "Cargo": cargo
        })

        entry_nombre.delete(0, tk.END)
        entry_apellido.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_cargo.delete(0, tk.END)
        
        actualizar_lista_trabajadores()
        

def actualizar_lista_trabajadores():
    
    lista_trabajadores.delete(0, tk.END)
    
    for trabajador in trabajadores:
        lista_trabajadores.insert(tk.END, f"{trabajador['Nombre']} {trabajador['Apellido']} - {trabajador['Cargo']}")

root = tk.Tk()
root.title("Registro de Trabajadores")

label_nombre = tk.Label(root, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

label_apellido = tk.Label(root, text="Apellido:")
label_apellido.pack()
entry_apellido = tk.Entry(root)
entry_apellido.pack()

label_edad = tk.Label(root, text="Edad:")
label_edad.pack()
entry_edad = tk.Entry(root)
entry_edad.pack()

label_cargo = tk.Label(root, text="Cargo:")
label_cargo.pack()
entry_cargo = tk.Entry(root)
entry_cargo.pack()


boton_registrar = tk.Button(root, text="Registrar Trabajador", command=registrar_trabajador)
boton_registrar.pack()


label_lista = tk.Label(root, text="Lista de Trabajadores:")
label_lista.pack()

lista_trabajadores = tk.Listbox(root, width=50, height=10)
lista_trabajadores.pack()

actualizar_lista_trabajadores()

root.mainloop()
