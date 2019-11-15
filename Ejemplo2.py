import tkinter as tk
from tkinter import *
from random import randint as r
from tkinter import ttk, messagebox
from tkinter import PhotoImage
window = Tk()
window.geometry("300x350")
window.config(bg="#181446")
miFrame = Frame()
miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width="150",height="150")
miFrame.config(bd="30")
miFrame.config(relief="sunken")
aEntrada = tk.StringVar()
nEntrada = tk.StringVar()
var = tk.StringVar()
#imagen = PhotoImage(file="pana.pgm")
#fondo = Label(window, image=imagen).place(x=20,y=0)
titulo = Label(window, text="Países participantes", width=15,font=("Comic Sans MS",20,"bold"),bg="#181446",fg="white").place(x=20,y=140)
Pas = Label(window, text="Ingrese cantidad de Países participantes: ",font=("Comic Sans MS",10, "bold"),bg="#181446",fg="white").place(x=20, y=180)
nPaises = IntVar()
Pais = Entry(window,textvariable=nPaises).place(x=80, y=210)
nomPais= tk.StringVar()
d = tk.getint()
mPaises=[]
def pRegistro():
    if nPaises.get()>=10:
       window4 = Toplevel(window)
       window4.geometry("400x300")
       Label(window4, text="Registro").place(x=50,y=20)
       
       Entry(window4,textvariable=nomPais, width=20).place(x=50,y=50)
       Button(window4,text="Ingresar", command=RegistrarPais).place(x=70,y=70)
       Button(window4,text="Continuar", command=vRegistro).place(x=70,y=100)
    else:
        messagebox.showinfo("Error","El número de participante debe ser mayor o igual a 10")
var.set("Elegir País")
opciones = []  

def RegistrarPais():
    if nomPais.get()=="" :    
      messagebox.showinfo("Error","Ingrese un país")
    elif len(opciones)<=nPaises.get()-1:
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
       window2.geometry("500x350")
       #imagen = PhotoImage(file="javelinfinal.pgm")
       #fondo = Label(window2, image=imagen).place(x=0, y=0)
       titulo = Label(window2, text="Datos del Deportista",font=("Arial",20,"bold")).place(x=20,y=100)
       nombre = Label(window2, text="Nombres",font=("Arial",10,),background="grey").place(x=20,y=150)
       apellidos = Label(window2, text="Apellidos",font=("Arial",10,),background="grey").place(x=20, y=180)
       paises = Label(window2, text="Paises   ",font=("Arial",10),background="grey").place(x=20,y=210)
       tk.Entry(window2, textvariable=nEntrada).place(x=100,y=150)
       tk.Entry(window2, textvariable=aEntrada).place(x=100,y=180)
       
       opcion = tk.OptionMenu(window2 ,var,*opciones).place(x=100, y=210)
      
       login = Button(window2, text="  Ingresar  ", background="red", command=bLogin).place(x=20, y=300)
       resultado = Button(window2, text="Resultado", background="red", command=vResultado).place(x=100, y=300)
       quit = Button(window2, text="     Salir     ", background="red", command=window2.destroy).place(x=180, y=300)
       for i in range(nPaises.get()):
           mPaises.append([0]*3)
       window2.mainloop() 
    else:
       messagebox.showinfo("Error","Ingresar más países")    
    
Button(window, text="Aceptar",bg="red", command=pRegistro, width=10).place(x=100,y=240)
Button(window, text="Salir",bg="red",command=window.destroy,width=10).place(x=100,y=270)
nombreC = []

     
def bLogin():
    nMayor=10
    nombre = nEntrada.get()+" "+aEntrada.get()
    nombreC.append(nombre)  
    pais = var.get()
    if nEntrada.get() != "" or aEntrada.get() != "":
      messagebox.showinfo("Registro con exito","Bienvenido "+nombre)
      for i in range(nPaises.get()):
        if opciones[i]==pais:
           a=r(0,2)   
           bronce=0
           plata=0
           oro=0
    #Con esto está sumando, la matriz se crea más arriba :S
           if a==0:
        #el cero será cambiado por la opción que se elige en el registro, solo es una prueba
              bronce = r(1,3)
              mPaises[i][a]+=bronce
              break
           elif a==1:
        #el cero será cambiado por la opción que se elige en el registro, solo es una prueba
              plata = r(1,3)
              mPaises[i][a]+=plata
              break
           elif a==2:
        #el cero será cambiado por la opción que se elige en el registro, solo es una prueba 
              oro = r(1,3)
              mPaises[i][a]+=oro  
              break              
         
     #if c==0:   
     #     for i in range(nPaises.get()):
     #       oPais = [0]*3
     #       c=c+1
    else:
        messagebox.showinfo("Error","Ingrese sus datos")  
    print(mPaises)    
def vResultado():
    window3 = Toplevel()
    window3.geometry("500x350")
    suma=0
    sumaT=[]
     #a=0
    c=0
    for i in range(nPaises.get()):
        for j in range(3):
            suma = suma + mPaises[i][j]
        sumaT.append(suma)   
     #for i in range(len(opciones)):
     #   a=a+30
     #   Label(window3, text=opciones[i]).place(x=60,y=a)    
    for i in range(nPaises.get()):
        c=c+30
        Label(window3, text=i+1).place(x=0, y=c)
    #iPeru = PhotoImage(file="peru1.pgm")
    #Peru = Label(window3, image=iPeru, text="Perú").place(x=100,y=150)
    l1 = Label(window3, text="Posición").place(x=0,y=0)
    l2 = Label(window3, text="País").place(x=80,y=0)
    l3 = Label(window3, text="   ",background="#CD7F32").place(x=180,y=0)
    l4 = Label(window3, text="   ",background="silver").place(x=200,y=0)
    l5 = Label(window3, text="   ",background="gold").place(x=220,y=0)
    l6 = Label(window3,text="Total").place(x=300,y=0)
    Button(window3, text="Cerrar",background="red",command=window3.destroy).place(x=200,y=300)
    
   
    window3.mainloop()
window.mainloop()