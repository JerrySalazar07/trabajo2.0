import tkinter as tk
from tkinter import *
from random import randint as r
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np
window = tk.Tk()
window.geometry("300x350")
window.config(bg="#181446")
aEntrada = tk.StringVar()
nEntrada = tk.StringVar()
var = tk.StringVar()
#imagen = tk.PhotoImage(file="descarga.png")
#fondo = ttk.Label(window, image=imagen).place(x=20,y=0)
titulo = ttk.Label(window, text="Países participantes", width=15,font=("Arial",20,"bold"),background="#181446").place(x=25,y=140)
Pas = tk.Label(window, text="Ingrese cantidad de Países participantes: ",font=("Comic Sans MS",10, "bold"),bg="#181446",fg="white").place(x=20, y=170)
nPaises = tk.IntVar()
Pais = tk.Entry(window,textvariable=nPaises).place(x=80, y=190)
nomPais= tk.StringVar()
d = tk.getint()
mPaises=[]
def pRegistro():
    if nPaises.get()>=10:
       window4 = tk.Toplevel(window)       
       window4.geometry("300x250")
       tk.Label(window4, text="Registro").place(x=50,y=0)
       tk.Entry(window4,textvariable=nomPais, width=20).place(x=50,y=50)
       tk.Button(window4,text="Ingresar",width=10, command=RegistrarPais,bg="red").place(x=70,y=80)
       tk.Button(window4,text="Continuar",width=10, command=vRegistro,bg="red").place(x=70,y=110)
       
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
      nomPais.set("")
    else:  
      messagebox.showinfo("Error","No puede ingresar más países")  
      print(opciones)
       
def vRegistro():
    c=0
    for i in opciones:
       c=c+1
    if c==nPaises.get():
       var.set("Elegir pais")
       window2 = tk.Toplevel()
       window2.geometry("350x400")
       #imagen = PhotoImage(file="javelinfinal.pgm")
       #fondo = Label(window2, image=imagen).place(x=0, y=0)
       titulo = tk.Label(window2, text="Datos del Deportista",font=("Arial",20,"bold")).place(x=40,y=100)
       nombre = tk.Label(window2, text="Nombres",font=("Arial",10,),background="grey").place(x=40,y=150)
       apellidos = tk.Label(window2, text="Apellidos",font=("Arial",10,),background="grey").place(x=40, y=180)
       paises = tk.Label(window2, text="Paises   ",font=("Arial",10),background="grey").place(x=40,y=210)
       tk.Entry(window2, textvariable=nEntrada).place(x=120,y=150)
       tk.Entry(window2, textvariable=aEntrada).place(x=120,y=180)
       
       opcion = tk.OptionMenu(window2 ,var,*opciones).place(x=120, y=210)
      
       login = tk.Button(window2, text="  Ingresar  ", background="red", command=bLogin).place(x=60, y=300)
       resultado = tk.Button(window2, text="Resultado", background="red", command=vResultado).place(x=80, y=350)
       quit = tk.Button(window2, text="     Salir     ", background="red", command=window2.destroy).place(x=130, y=300)
       for i in range(nPaises.get()):
           mPaises.append([0]*3)
       window2.mainloop() 
       var.set("Elegir país")
    else:
       messagebox.showinfo("Error","Ingresar más países")    
    
Button(window, text="Aceptar",bg="red", command=pRegistro, width=10).place(x=100,y=220)
Button(window, text="Salir",bg="red",command=window.destroy,width=10).place(x=100,y=250)
nombreC = []

     
def bLogin():
    nombre = nEntrada.get()+" "+aEntrada.get()
    nombreC.append(nombre)  
    pais = var.get()
    if nEntrada.get() != "" or aEntrada.get() != ""  :
      messagebox.showinfo("Registro con exito","Bienvenido "+nombre)
      for i in range(nPaises.get()):
        if opciones[i]==pais:
           a=r(0,2)   
           bronce=1
           plata=1
           oro=1
           if a==0:
              mPaises[i][a]+=bronce
              break
           elif a==1:
              mPaises[i][a]+=plata
              break
           elif a==2:
              mPaises[i][a]+=oro  
              break
    elif pais=="Elegir país":
        messagebox.showinfo("Error","Ingrese un país")                              
    else:
        messagebox.showinfo("Error","Ingrese sus datos")

    nEntrada.set("")
    aEntrada.set("")
    var.set("Elegir país")
    print(mPaises)    
def vResultado():
    window3 = tk.Toplevel()
    window3.geometry("500x350")
    sumaT=[]
    a=0
    c=0
    for i in range(nPaises.get()):
        suma=0
        for j in range(3):
            suma = suma + mPaises[i][j]
        sumaT.append(suma)     
    for i in range(nPaises.get()):
        c=c+30
        tk.Label(window3, text=i+1).place(x=0, y=c)

    print("Pais\t\tMedallas\t\tTotal")
    for i in range(len(mPaises)):
        for j in range(len(mPaises)-1):
            if sumaT[j]>sumaT[j+1]:
                
                itemSum=sumaT[j]
                sumaT[j]=sumaT[j+1]
                sumaT[j+1]=itemSum
                
                medallas=mPaises[j]
                mPaises[j]=mPaises[j+1]
                mPaises[j+1]=medallas
                 
                opcion=opciones[j]
                opciones[j]=opciones[j+1]
                opciones[j+1]=opcion   
    opciones.reverse()
    mPaises.reverse()
    sumaT.reverse()            
    #iPeru = PhotoImage(file="peru1.pgm")
    #Peru = Label(window3, image=iPeru, text="Perú").place(x=100,y=150)
    tk.Label(window3, text="Posición").place(x=0,y=0)
    tk.Label(window3, text="País").place(x=80,y=0)
    tk.Label(window3, text="   ",background="#CD7F32").place(x=180,y=0)
    tk.Label(window3, text="   ",background="silver").place(x=200,y=0)
    tk.Label(window3, text="   ",background="gold").place(x=220,y=0)
    tk.Label(window3,text="Total").place(x=300,y=0)
    tk.Button(window3, text="Cerrar",background="red",command=window3.destroy).place(x=200,y=300)
    for i in range(len(mPaises)):
        f=160
        a=a+30
        tk.Label(window3, text=opciones[i]).place(x=80,y=a)
        tk.Label(window3,text=sumaT[i]).place(x=300,y=a)
        for j in range(3):
            f=f+20
            tk.Label(window3, text=mPaises[i][j]).place(x=f,y=a)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    paises = opciones
    datos = sumaT
    xx = range(1,len(datos)+1)

    ax.bar(xx, datos)
    ax.set_xticks(xx)
    ax.set_xticklabels(paises)
    ax.set_ylabel("N° de Medallas")

    plt.show()        
    window3.mainloop()
window.mainloop()
