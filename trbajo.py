import tkinter as tk
from tkinter import *
from random import randint as r
from tkinter import ttk, messagebox
#La vista de la interfaz no me convence mucho, sería cosa de modificarlo para que quede mejor
window = Tk()
window.geometry("600x500")
#La imagen es de prueba (para ver como quedaría en la interfaz)
#imagen = PhotoImage(file="javelinfinal.pgm")
#fondo = Label(window, image=imagen).place(x=250, y=0)
titulo = Label(window, text="Datos del Deportista",font=("Arial",20)).place(x=230,y=100)
nombre = Label(window, text="Nombres",font=("Arial",10,),background="grey").place(x=230,y=150)
apellidos = Label(window, text="Apellidos",font=("Arial",10,),background="grey").place(x=230, y=180)
paises = Label(window, text="Paises   ",font=("Arial",10),background="grey").place(x=230,y=210)
nEntrada = tk.StringVar()
tk.Entry(window, textvariable=nEntrada).place(x=310,y=150)
aEntrada = tk.StringVar()
tk.Entry(window, textvariable=aEntrada).place(x=310,y=180)
var = tk.StringVar(window)
var.set("Elegir País")
opciones = ["Perú", "Brasil", "Chile", "Argentina", "Uruguay"]
opcion = tk.OptionMenu(window ,var,*opciones).place(x=310, y=210)
nombres = []
apellidos = []
#No se me ocurre otra manera de almacenar las medallas y luego separarlas :S
peru = [0] * 3
brasil = [0] * 3
chile = [0] * 3
argentina = [0] * 3
uruguay = [0] * 3
def bLogin():
    nMayor=10
    nombre = nEntrada.get()
    apellido = aEntrada.get()
    bronce = r(1,5)
    plata = r(1,5)
    oro = r(1,5)
    nombres.append(nombre)
    apellidos.append(apellido)
    if var.get()=="Perú":
        peru[0]+=bronce
        peru[1]+=plata
        peru[2]+=oro
    elif var.get()=="Brasil":
        brasil[0]+=bronce
        brasil[1]+=plata
        brasil[2]+=oro
    elif var.get()=="Chile":
        chile[0]+=bronce
        chile[1]+=plata
        chile[2]+=oro
    elif var.get()=="Argentina":
        argentina[0]+=bronce
        argentina[1]+=plata
        argentina[2]+=oro
    elif var.get()=="Uruguay":
        uruguay[0]+=bronce
        uruguay[1]+=plata
        uruguay[2]+=oro
    #Esto solo es para ver si los datos están siendo ingresados, no quedarán en la presentación final
    """print(peru)
    print(brasil)
    print(argentina)
    print(uruguay)
    print(chile)
    print(sumaP)
    print(sumaB)
    print(sumaC)
    print(sumaA)
    print(sumaU)
    print(nombres)
    print(apellidos)"""
def vResultado():
    window2 = Toplevel(window)
    window2.geometry("350x250")
    sumaP=0
    sumaB=0
    sumaA=0
    sumaU=0
    sumaC=0
    for i in range(3):
        sumaP = sumaP+peru[i]
    for i in range(3):
        sumaB = sumaB+brasil[i]
    for i in range(3):
        sumaC = sumaC + chile[i]
    for i in range(3):
        sumaA = sumaA+argentina[i]
    for i in range(3):
        sumaU = sumaU+ uruguay[i]
    Label(window2, text=sumaP).place(x=1,y=1) 
    Button(window2, text="Cerrar",background="red",command=window2.destroy).place(x=20,y=20)
login = Button(window, text="  Ingresar  ", background="red",command = bLogin).place(x=210, y=300)
resultado = Button(window, text="Resultado", background="red",command=vResultado).place(x=305,y=350)
quit = Button(window, text="     Salir     ", background="red", command = window.destroy).place(x=400, y=300)
window.mainloop()
