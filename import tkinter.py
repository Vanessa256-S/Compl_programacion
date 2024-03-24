import tkinter

ventana = tkinter.Tk() #Contenedor de graficos
ventana.geometry("400x400")

etiqueta = tkinter.Label(ventana, text="Hola mundo",bg="pink")
etiqueta.pack(fill=tkinter.X)#Colocar el label en pantalla

cajaNumero1 = tkinter.Entry(ventana, font="Helveltica 20")
cajaNumero1.pack()
cajaNumero2 = tkinter.Entry(ventana, font="Helveltica 20")
cajaNumero2.pack()



#def numerosDeLaCaja():
    #numero1 = int(cajaNumero1.get())
    #numero2 = int(cajaNumero2.get())
    #resulMultiplicacion = numero1 * numero2
    #etiquetaResult["text"] = resulMultiplicacion
    #print("El resultado de la multiplicacion es: ", resulMultiplicacion)


#boton = tkinter.Button(ventana, text="Multiplicar", command = numerosDeLaCaja)
#boton.pack()

etiquetaResult = tkinter.Label(ventana, text="",bg="beige", font="Helveltica 20")
etiquetaResult.pack(fill=tkinter.X)#Colocar el label en pantalla

ventana.mainloop()