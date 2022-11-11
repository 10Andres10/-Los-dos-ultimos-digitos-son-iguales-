from tkinter import *

# -----------------
# Ventana principal
# -----------------
aplicacion = Tk()

# Título de la ventana
aplicacion.title("¿Los dos ultimos dígitos son iguales?")

# Tamaño de la ventana
aplicacion.geometry("400x400")

# Deshabilitar maximixar
aplicacion.resizable(0,0)

# Color de fondo de la ventana
aplicacion.config(bg="Pale turquoise3")

# Texto de indicación
Label1 = Label(text="Ingrese el número:")
Label1.place(x=50,y=40)
Label1.config(fg="dark blue", font=("Comic Sans MS", 22), bg="dodger blue")

# Entrada de números
Entry1 = Entry()
Entry1.place(x=50,y=120,width=260,height=40)
Entry1.config(bg="White", fg="steel blue", font=("Comic Sans MS",22))

# Botón para accionar el mecanismo
Button = Button(text="Probar")
Button.config(bg="cornflower blue", fg="black", font=("Comic Sans MS",16))
Button.place(x=150,y=320)

# Texto para indicar el separador de resultado
Label2 = Label(text="El resultado es")
Label2.place(x=70,y=180)
Label2.config(fg="dark blue", font=("Comic Sans MS", 22), bg="dodger blue")

# Sección que muestra el resultado
resultado = Text()
resultado.place(x=50, y=250,width=260,height=40)
resultado.config(bg="White", fg="steel blue", font=("Comic Sans MS",22))

#Bucle infinito
aplicacion.mainloop()