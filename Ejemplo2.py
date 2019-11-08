import tkinter as tk
from tkinter import *
from random import randint as r
from tkinter import ttk, messagebox
#La vista de la interfaz no me convence mucho, sería cosa de modificarlo para que quede mejor
window = Tk()
window.geometry("300x350")
aEntrada = tk.StringVar()
nEntrada = tk.StringVar()
var = tk.StringVar()
titulo = Label(window, text="Países participantes", width=15,font=("Arial",20,"bold")).place(x=20,y=0)
Pas = Label(window, text="Ingrese cantidad de Países participantes: ",font=("Arial",10, "bold")).place(x=20, y=30)
nPaises = IntVar()
Pais = Entry(window,textvariable=nPaises).place(x=80, y=50)
def vRegistro():
    if nPaises.get()>=10:
       window2 = Toplevel(window)
       imagen = PhotoImage(file="javelinfinal.pgm")
       # La imagen es de prueba (para ver como quedaría en la interfaz
       fondo = Label(window2, image=imagen).place(x=250, y=0)
       titulo = Label(window2, text="Datos del Deportista",font=("Arial",20,"bold")).place(x=215,y=100)
       nombre = Label(window2, text="Nombres",font=("Arial",10,),background="grey").place(x=230,y=150)
       apellidos = Label(window2, text="Apellidos",font=("Arial",10,),background="grey").place(x=230, y=180)
       paises = Label(window2, text="Paises   ",font=("Arial",10),background="grey").place(x=230,y=210)
       tk.Entry(window2, textvariable=nEntrada).place(x=310,y=150)
       tk.Entry(window2, textvariable=aEntrada).place(x=310,y=180)
       var.set("Elegir País")
       opciones = ["Perú", "Brasil", "Chile", "Argentina", "Uruguay", "EEUU"]
       opcion = tk.OptionMenu(window2 ,var,*opciones).place(x=310, y=210)
       login = Button(window2, text="  Ingresar  ", background="red", command=bLogin).place(x=210, y=300)
       resultado = Button(window2, text="Resultado", background="red", command=vResultado).place(x=305, y=350)
       quit = Button(window2, text="     Salir     ", background="red", command=window.destroy).place(x=400, y=300)
    else:
        messagebox.showinfo("Error","El número de participante debe ser mayor o igual a 10")
Button(window, text="Aceptar",bg="red", command=vRegistro).place(x=120,y=80)
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
#def window2():


def vResultado():
    window3 = Toplevel()
    window3.geometry("500x350")
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
    Label(window3, text="Posición").place(x=0,y=0)
    Label(window3, text="País").place(x=80,y=0)
    Label(window3, text="  ",background="brown").place(x=180,y=0)
    Label(window3, text="  ",background="silver").place(x=200,y=0)
    Label(window3, text="  ",background="gold").place(x=220,y=0)
    Label(window3,text="Total").place(x=300,y=0)
    Button(window3, text="Cerrar",background="red",command=window3.destroy).place(x=200,y=300)
window.mainloop()