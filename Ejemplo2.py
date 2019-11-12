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
    if nPaises.get()>=1:
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

def RegistrarPais():
    if len(opciones)<=nPaises.get()-1:    
      opcion=nomPais.get()
      opciones.append(opcion)   
      print(opciones)
    else:  
      messagebox.showinfo("Error","No puede ingresar más países")  
      print(opciones)
       
def vRegistro():
    c=0
    for i in opciones:
        c=c+1
    if c==nPaises.get():
       window2 = Toplevel()
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
       quit = Button(window2, text="     Salir     ", background="red", command=window2.destroy).place(x=250, y=300)
       window2.mainloop() 
    else:
       messagebox.showinfo("Error","Ingresar más países")    
    
Button(window, text="Aceptar",bg="red", command=pRegistro, width=10).place(x=100,y=220)
Button(window, text="Salir",bg="red",command=window.destroy,width=10).place(x=100,y=250)
nombreC = []
oPais = var.get()
def bLogin():
    c=0
    nMayor=10
    nombre = nEntrada.get()+" "+aEntrada.get()
    if nEntrada.get() != "" or aEntrada.get() != "":
       messagebox.showinfo("Registro con exito","Bienvenido "+nombre)
       bronce=0
       plata=0
       oro=0
       if bronce<=0:
          bronce = r(0,2)
       elif plata<=0 and bronce!=1:
          plata = r(0,2)
       elif oro <=0 and plata!=1 and bronce!=1: 
          oro = r(0,2)
       nombreC.append(nombre)
    if c==0:   
       for i in range(nPaises.get()):
           oPais = [0]*3
           c=c+1
    if c>=0:
       for j in range(1):
           oPais[0]+=bronce
           oPais[1]+=plata
           oPais[2]+=oro
    #Nos ahorramos todo esto    
    else:
        messagebox.showinfo("Error","Ingrese sus datos")
    print(oPais)    
def vResultado():
    window3 = Toplevel()
    window3.geometry("500x350")
    suma=0
    sumaP = []
    c=0
    a=0
    #for i in range(3):
    #    suma = suma + oPais[i]
    #    sumaP.append(suma)
    #print(suma)    
    """
    for i in range(3):
        sumaP = sumaP+Peru[i]
    for i in range(3):
        sumaB = sumaB+Brasil[i]
    for i in range(3):
        sumaC = sumaC +Chile[i]
    for i in range(3):
        sumaA = sumaA+Argentina[i]
    for i in range(3):
        sumaU = sumaU+ Uruguay[i]"""
    for i in range(len(opciones)):
        a=a+30
        Label(window3, text=opciones[i]).place(x=60,y=a)    
    for i in range(nPaises.get()):
        c=c+30
        Label(window3, text=i+1).place(x=0, y=c)
    #iPeru = PhotoImage(file="peru1.pgm")
    #Peru = Label(window3, image=iPeru, text="Perú").place(x=100,y=150)
    Label(window3, text="Posición").place(x=0,y=0)
    Label(window3, text="País").place(x=80,y=0)
    Label(window3, text="   ",background="#CD7F32").place(x=180,y=0)
    Label(window3, text="   ",background="silver").place(x=200,y=0)
    Label(window3, text="   ",background="gold").place(x=220,y=0)
    Label(window3,text="Total").place(x=300,y=0)
    Button(window3, text="Cerrar",background="red",command=window3.destroy).place(x=200,y=300)
    window3.mainloop()
window.mainloop()