import tkinter as tk
from tkinter import *
from random import randint as r
from tkinter import ttk, messagebox
window = Tk()
window.geometry("300x350")
aEntrada = tk.StringVar()
nEntrada = tk.StringVar()
var = tk.StringVar()
#imagen = PhotoImage(file="pana.pgm")
#fondo = Label(window, image=imagen).place(x=20,y=0)
titulo = Label(window, text="Países participantes", width=15,font=("Arial",20,"bold")).place(x=20,y=140)
Pas = Label(window, text="Ingrese cantidad de Países participantes: ",font=("Arial",10, "bold")).place(x=20, y=170)
nPaises = IntVar()
Pais = Entry(window,textvariable=nPaises).place(x=80, y=190)
nomPais= tk.StringVar()
def pRegistro():
    if nPaises.get()>=10:
       window4 = Toplevel(window)
       window4.geometry("400x300")
       Label(window4, text="Registro").place(x=50,y=0)
       
       Entry(window4,textvariable=nomPais, width=20).place(x=50,y=50)
       Button(window4,text="Ingresar", command=RegistrarPais).place(x=70,y=70)
       Button(window4,text="Continuar", command=vRegistro).place(x=70,y=100)
    else:
        messagebox.showinfo("Error","El número de participante debe ser mayor o igual a 10")
var.set("Elegir País")
opciones = []  
c=0
def RegistrarPais():
      opcion=nomPais.get()
      opciones.append(opcion)   
      print(opciones)
def vRegistro():
       window2 = Toplevel()
       # La imagen es de prueba (para ver como quedaría en la interfaz
       #imagen = PhotoImage(file="javelinfinal.pgm")
       #fondo = Label(window2, image=imagen).place(x=0, y=0)
       titulo = Label(window2, text="Datos del Deportista",font=("Arial",20,"bold")).place(x=100,y=100)
       nombre = Label(window2, text="Nombres",font=("Arial",10,),background="grey").place(x=100,y=150)
       apellidos = Label(window2, text="Apellidos",font=("Arial",10,),background="grey").place(x=100, y=180)
       paises = Label(window2, text="Paises   ",font=("Arial",10),background="grey").place(x=100,y=210)
       tk.Entry(window2, textvariable=nEntrada).place(x=170,y=150)
       tk.Entry(window2, textvariable=aEntrada).place(x=170,y=180)
       
       opcion = tk.OptionMenu(window2 ,var,*opciones).place(x=170, y=210)
       login = Button(window2, text="  Ingresar  ", background="red", command=bLogin).place(x=150, y=300)
       resultado = Button(window2, text="Resultado", background="red", command=vResultado).place(x=200, y=350)
       quit = Button(window2, text="     Salir     ", background="red", command=window.destroy).place(x=250, y=300)
       window2.mainloop()
    
Button(window, text="Aceptar",bg="red", command=pRegistro, width=10).place(x=100,y=220)
Button(window, text="Salir",bg="red",command=window.destroy,width=10).place(x=100,y=250)
nombres = []
apellidos = []
#No se me ocurre otra manera de almacenar
for i in range(nPaises.get()):
    opciones[i]=[]
def bLogin():
    nMayor=10
    nombre = nEntrada.get()
    apellido = aEntrada.get()
    if nEntrada.get() != "" or aEntrada.get() != "":
       messagebox.showinfo("Registro con exito","Bienvenido "+nombre+" "+apellido)
       bronce = r(1,5)
       plata = r(1,5)
       oro = r(1,5)
       nombres.append(nombre)
       apellidos.append(apellido)
       if var.get()=="Peru" or var.get()=="peru":
        Peru[0]+=bronce
        Peru[1]+=plata
        peru[2]+=oro
       elif var.get()=="Brasil" or var.get()=="brasil":
        Brasil[0]+=bronce
        Brasil[1]+=plata
        Brasil[2]+=oro
       elif var.get()=="Chile" or var.get()=="chile":
        Chile[0]+=bronce
        Chile[1]+=plata
        Chile[2]+=oro
       elif var.get()=="Argentina" or var.get()=="argentina":
        Argentina[0]+=bronce
        Argentina[1]+=plata
        Argentina[2]+=oro
       elif var.get()=="Uruguay" or var.get()=="uruguay":
        Uruguay[0]+=bronce
        Uruguay[1]+=plata
        Uruguay[2]+=oro
    else:
        messagebox.showinfo("Error","Ingrese sus datos")
def vResultado():
    window3 = Toplevel()
    window3.geometry("500x350")
    sumaP=0
    sumaB=0
    sumaA=0
    sumaU=0
    sumaC=0
    c=0
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
    for i in range(nPaises.get()):
        c=c+30
        Label(window3, text=i+1).place(x=0, y=c)
    #iPeru = PhotoImage(file="peru1.pgm")
    #Peru = Label(window3, image=iPeru, text="Perú").place(x=100,y=150)
    Label(window3, text="Posición").place(x=0,y=0)
    Label(window3, text="País").place(x=80,y=0)
    Label(window3, text="  ",background="brown").place(x=180,y=0)
    Label(window3, text="  ",background="silver").place(x=200,y=0)
    Label(window3, text="  ",background="gold").place(x=220,y=0)
    Label(window3,text="Total").place(x=300,y=0)
    Button(window3, text="Cerrar",background="red",command=window3.destroy).place(x=200,y=300)
    window3.mainloop()
  


window.mainloop()