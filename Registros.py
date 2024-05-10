import pyodbc
import tkinter 
from tkinter import messagebox
from tkinter import ttk


# Crear la Ventana principal
Ventana = tkinter.Tk()
Ventana.geometry("600x500")
Ventana.title("rentabilidad de la granja")

#creaciòn de los paneles
panel=ttk.Notebook(Ventana)
panel.pack(fill="both",expand="yes")

#creacion del panel del crud de la granja
tab1= ttk.Frame(panel)
panel.add(tab1,text="crud ganadero")


# Función para conectar a la base de datos
def conectar():
    try:
        conexion = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=ASUS\SQLEXPRESS;'
            'DATABASE=Granja;'
            'Trusted_Connection=yes;'
        )
        return conexion
    except pyodbc.Error as e:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")
        return None

# Función para insertar un nuevo registro en la base de datos del ganado
def insertar_registro(id,Especie,Raza,Edad,Peso,ValorKilo,ValorTotal ):
    try:
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            consulta = "INSERT INTO GANADO (id,Especie,Raza,Edad,Peso,ValorKilo,ValorTotal ) VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(consulta, (id,Especie,Raza,Edad,Peso,ValorKilo,ValorTotal ))
            conexion.commit()
            messagebox.showinfo("Registro Insertado", "El nuevo registro se ha insertado correctamente.")
            cursor.close()
            conexion.close()
    except pyodbc.Error as e:
        messagebox.showerror("Error al insertar", f"No se pudo insertar el registro: {e}")

# Función para actualizar un registro en la base de datos del ganado
def actualizar_registro(id,Especie,Raza,Edad,Peso,ValorKilo,ValorTotal ):
    try:
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            consulta = "UPDATE GANADO SET Especie=?, Raza=?, Edad=?, Peso=?, ValorKilo=?, ValorTotal=? WHERE ID=?"
            cursor.execute(consulta, (Especie,Raza,Edad,Peso,ValorKilo,ValorTotal,id ))
            conexion.commit()
            messagebox.showinfo("Registro Actualizado", "El registro se ha actualizado correctamente.")
            cursor.close()
            conexion.close()
    except pyodbc.Error as e:
        messagebox.showerror("Error al actualizar", f"No se pudo actualizar el registro: {e}")

# Función para eliminar un registro de la base de datos del ganado
def eliminar_registro(id):
    try:
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            consulta = "DELETE FROM GANADO WHERE ID=?"
            cursor.execute(consulta, (id,))
            conexion.commit()
            messagebox.showinfo("Registro Eliminado", "El registro se ha eliminado correctamente.")
            cursor.close()
            conexion.close()
    except pyodbc.Error as e:
        messagebox.showerror("Error al eliminar", f"No se pudo eliminar el registro: {e}")

# Función para mostrar todos los registros de la tabla del ganado
def mostrar_registros():
    try:
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM GANADO")
            registros = cursor.fetchall()
            cursor.close()
            conexion.close()
            return registros
    except pyodbc.Error as e:
        messagebox.showerror("Error al leer", f"No se pudieron obtener los registros: {e}")
        return []

# Función para manejar el evento de botón "Insertar ganado"
def insertar_registro_interfaz():
    # Obtener valores de las entradas del ganado
    id= Id.get()
    Especie = especie.get()
    Raza = raza.get()
    Edad = edad.get()
    Peso = peso.get()
    ValorKilo = valorkilo.get()
    ValorTotal=int(Peso)*int(ValorKilo)

    # Insertar el nuevo registro del ganado
    insertar_registro(id,Especie,Raza,Edad,Peso,ValorKilo,ValorTotal )

# Función para manejar el evento de botón "Actualizar ganado"
def actualizar_registro_interfaz():
    # Obtener valores de las entradas del ganado
    id= Id.get()
    Especie = especie.get()
    Raza = raza.get()
    Edad = edad.get()
    Peso = peso.get()
    ValorKilo = valorkilo.get()
    ValorTotal=int(Peso)*int(ValorKilo)

    # Actualizar la tabla ganado gracias al id
    actualizar_registro(id,Especie,Raza,Edad,Peso,ValorKilo,ValorTotal )
# Función para manejar el evento de botón "Eliminar ganado" 
def eliminar_registro_interfaz():
    # Obtener el id del registro a eliminar
    id = Id.get()

    # Eliminar el registro con el id especificado
    eliminar_registro(id)

# Función para mostrar todos los registros del ganado en la consola
def mostrar_registros_interfaz():
    registros = mostrar_registros()
    print("estos son los datos de la tabla ganado")
    if registros:
        for registro in registros:
            print(registro)
    else:
        print("No se encontraron registros.")



# Crear campos de entrada ganado
tkinter.Label(tab1, text="ID:").place(x=5, y=15) 
Id = tkinter.Entry(tab1)
Id.place(x=60, y=15)  

tkinter.Label(tab1, text="Especie:").place(x=5, y=50)  
especie = tkinter.Entry(tab1)
especie.place(x=60, y=50)  

tkinter.Label(tab1, text="Raza:").place(x=5, y=85) 
raza = tkinter.Entry(tab1)
raza.place(x=60, y=85) 

tkinter.Label(tab1, text="Edad:").place(x=5, y=120) 
edad = tkinter.Entry(tab1)
edad.place(x=60, y=120) 

tkinter.Label(tab1, text="Peso kg:").place(x=5, y=155) 
peso = tkinter.Entry(tab1)
peso.place(x=60, y=155) 

tkinter.Label(tab1, text="Valor Kg:").place(x=5, y=190) 
valorkilo = tkinter.Entry(tab1)
valorkilo.place(x=60, y=190) 


# Botones para realizar operaciones CRUD ganado
tkinter.Button(tab1, text="Insertar ganado", command=insertar_registro_interfaz).place(x=30, y=290) 
tkinter.Button(tab1, text="Actualizar ganado", command=actualizar_registro_interfaz).place(x=30, y=320)
tkinter.Button(tab1, text="Eliminar ganado", command=eliminar_registro_interfaz).place(x=30, y=350)
tkinter.Button(tab1, text="Mostrar ganado", command=mostrar_registros_interfaz).place(x=30, y=380)

#insertar un nuevo cultivo 
def insertar_Cultivo(Identificador,Nombre,Tipo,Area,Rendimiento,ValorKilo1,ValorTotal ):
    try:
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            consulta = "INSERT INTO Cultivos (id,Nombre,Tipo,Area,Rendimiento,ValorKilo ) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(consulta, (Identificador,Nombre,Tipo,Area,Rendimiento,ValorKilo1,ValorTotal ))
            conexion.commit()
            messagebox.showinfo("Registro Insertado", "El nuevo registro se ha insertado correctamente.")
            cursor.close()
            conexion.close()
    except pyodbc.Error as e:
        messagebox.showerror("Error al insertar", f"No se pudo insertar el registro: {e}")


# Función para actualizar un registro en la base de datos del cultivo
def actualizar_Cultivo(Identificador,Nombre,Tipo,Area,Rendimiento,ValorKilo1,ValorTotal ):
    try:
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            consulta = "UPDATE Cultivos SET Nombre=?, Tipo=?, Area=?, Rendimiento=?, ValorKilo=? WHERE ID=?"
            cursor.execute(consulta, (Nombre,Tipo,Area,Rendimiento,ValorKilo1,ValorTotal ,Identificador ))
            conexion.commit()
            messagebox.showinfo("Registro Actualizado", "El registro se ha actualizado correctamente.")
            cursor.close()
            conexion.close()
    except pyodbc.Error as e:
        messagebox.showerror("Error al actualizar", f"No se pudo actualizar el registro: {e}")


# Función para eliminar un registro de la base de datos de los cultivos
def eliminar_registro_Cultivo(Identificador):
    try:
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            consulta = "DELETE FROM Cultivos WHERE ID=?"
            cursor.execute(consulta, (Identificador,))
            conexion.commit()
            messagebox.showinfo("Registro Eliminado", "El registro se ha eliminado correctamente.")
            cursor.close()
            conexion.close()
    except pyodbc.Error as e:
        messagebox.showerror("Error al eliminar", f"No se pudo eliminar el registro: {e}")

        
# Función para mostrar todos los registros de la tabla de los cultivos

def mostrar_registros_Cultivo():
    try:
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            print("los datos de la tabla cultivos son: ")
            cursor.execute("select * from Cultivos")
            registros = cursor.fetchall()
            cursor.close()
            conexion.close()
            if registros:
                for registro in registros:
                    print(registro)
            else:
                print("No se encontraron registros en la tabla de Cultivos.")
            return registros
    except pyodbc.Error as e:
        messagebox.showerror("Error al leer", "No se pudieron obtener los registros: {e}")
        return []

# Función para manejar el evento de botón "Insertar ganado"
def insertar_registro_Cultivo():
    # Obtener valores de las entradas del ganado
    Identificador= identificador.get()
    Nombre = nombre.get()
    Tipo = tipo.get()
    Area = area.get()
    Rendimiento = rendimiento.get()
    ValorKilo1 = valorkilo1.get()
    ValorTotal=int(Area)*int(Rendimiento)

    insertar_Cultivo(Identificador,Nombre,Tipo,Area,Rendimiento,ValorKilo1,ValorTotal )
# Función para manejar el evento de botón "Actualizar ganado"
def actualizar_registro_Cultivo():
    # Obtener valores de las entradas del ganado
    Identificador= identificador.get()
    Nombre = nombre.get()
    Tipo = tipo.get()
    Area = area.get()
    Rendimiento = rendimiento.get()
    ValorKilo1 = valorkilo1.get()
    ValorTotal=int(Area)*int(Rendimiento)
    # Actualizar la tabla ganado gracias al id
    actualizar_Cultivo(Identificador,Nombre,Tipo,Area,Rendimiento,ValorKilo1,ValorTotal )

# Crear campos de entrada Cultivos
tkinter.Label(tab1, text="ID:").place(x=320, y=15) 
identificador = tkinter.Entry(tab1)
identificador.place(x=400, y=15)  

tkinter.Label(tab1, text="Nombre:").place(x=320, y=50)  
nombre = tkinter.Entry(tab1)
nombre.place(x=400, y=50)  

tkinter.Label(tab1, text="tipo:").place(x=320, y=85) 
tipo = tkinter.Entry(tab1)
tipo.place(x=400, y=85) 

tkinter.Label(tab1, text="Area:").place(x=320, y=120) 
area = tkinter.Entry(tab1)
area.place(x=400, y=120) 

tkinter.Label(tab1, text="Rendimiento:").place(x=320, y=155) 
rendimiento = tkinter.Entry(tab1)
rendimiento.place(x=400, y=155) 

tkinter.Label(tab1, text="Valor KG:").place(x=320, y=190) 
valorkilo1 = tkinter.Entry(tab1)
valorkilo1.place(x=400, y=190) 

# Botones para realizar operaciones CRUD de los cultivos
tkinter.Button(tab1, text="Insertar Cultivos", command=insertar_registro_Cultivo).place(x=400, y=290) 
tkinter.Button(tab1, text="Actualizar Cultivos", command=actualizar_registro_Cultivo).place(x=400, y=320)
tkinter.Button(tab1, text="Eliminar Cultivos", command=eliminar_registro_Cultivo).place(x=400, y=350)
tkinter.Button(tab1, text="Mostrar Cultivos", command=mostrar_registros_Cultivo).place(x=400, y=380)





# Ejecutar el bucle principal de la interfaz gráfica
tab1.mainloop()