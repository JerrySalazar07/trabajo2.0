__author__="Jean Borja, Alexia Menendez, Jerry Salazar"
__version__="v1.0"
__credits__="BMS-C-2019"
__license__="C"
__maintainer__="BMS"
__status__="estudiante"
import tkinter as tk
from tkinter import *
from random import randint as r
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np
window = Tk()
window.geometry("300x350")
window.config(bg="#181446")
aEntrada = tk.StringVar()
nEntrada = tk.StringVar()
var = tk.StringVar()
imagen = PhotoImage(file="lima2019.png")
fondo = Label(window, image=imagen).place(x=5,y=20)
titulo = Label(window, text="Países participantes", width=15,font=("Comic Sans MS",20,"bold"),bg="#181446",fg="white").place(x=25,y=170)
Pas = Label(window, text="Ingrese cantidad de Países participantes: ",font=("Comic Sans MS",10, "bold"),bg="#181446",fg="white").place(x=20, y=210)
nPaises = IntVar()
Pais = Entry(window,textvariable=nPaises).place(x=80, y=240)
nomPais= tk.StringVar()
d = tk.getint()
mPaises=[]

def pRegistro():
    if nPaises.get()>=10:
       window4 = Toplevel(window)
       window4.geometry("400x300")
       window4.config(bg="#181446")
       #ipais=PhotoImage(file="paises1.png")
       #Label(window4,image=ipais).place(x=0,y=0)
       Label(window4, text="Registrar países",font=("Comic Sans MS",15,"bold"),bg="#181446",fg="white").place(x=220,y=0)
       
       Entry(window4,textvariable=nomPais, width=20).place(x=220,y=60)
       
       Button(window4,text="Ingresar", command=RegistrarPais).place(x=220,y=90)
       Button(window4,text="Continuar", command=vRegistro).place(x=220,y=130)
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
    if len(opciones)==nPaises.get():
       window2 = Toplevel()
       window2.geometry("500x350")
       window2.config(bg="#181446")
       #imagen = PhotoImage(file="javelinfinal.pgm")
       #fondo = Label(window2, image=imagen).place(x=0, y=0)
       Label(window2, text="Datos del Deportista",font=("Comic Sans MS",20,"bold"),bg="#181446",fg="white").place(x=20,y=100)
       Label(window2, text="Nombres",font=("Comic Sans MS",10,"bold"),bg="#181446",fg="white").place(x=20,y=150)
       Label(window2, text="Apellidos",font=("Comic Sans MS",10,"bold"),bg="#181446",fg="white").place(x=20, y=180)
       Label(window2, text="Paises   ",font=("Comic Sans MS",10,"bold"),bg="#181446",fg="white").place(x=20,y=210)
       tk.Entry(window2, textvariable=nEntrada).place(x=100,y=150)
       tk.Entry(window2, textvariable=aEntrada).place(x=100,y=180)
       opcion = tk.OptionMenu(window2 ,var,*opciones).place(x=100, y=210)
      
       Button(window2, text="  Ingresar  ", background="red", command=bLogin).place(x=20, y=300)
       Button(window2, text="Resultado", background="red", command=vResultado).place(x=90, y=300)
       Button(window2, text="     Salir     ", background="red", command=window2.destroy).place(x=160, y=300)
       for i in range(nPaises.get()):
           mPaises.append([0]*3)
       window2.mainloop() 
    else:
       messagebox.showinfo("Error","Ingresar más países")    
    
Button(window, text="Aceptar",bg="red", command=pRegistro, width=10).place(x=100,y=270)
Button(window, text="Salir",bg="red",command=window.destroy,width=10).place(x=100,y=300)
nombreC = []

     
def bLogin():
    nombre = nEntrada.get()+" "+aEntrada.get()
    nombreC.append(nombre)  
    pais = var.get()
    if nEntrada.get() != "" or aEntrada.get() != "":
      messagebox.showinfo("Registro con exito","Bienvenido "+nombre)
      nEntrada.set("")
      aEntrada.set("")
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
      var.set("Elegir País")                 
    else:
        messagebox.showinfo("Error","Ingrese sus datos")  
    print(mPaises)    
def vResultado():
    window3 = Toplevel()
    window3.geometry("500x350")
    sumaT=[]
    a=0
    c=0
    
    for i in range(nPaises.get()):
        suma=0
        for j in range(3):
            suma = suma + mPaises[i][j]
        sumaT.append(suma)   
    print(sumaT)    
    for i in range(nPaises.get()):
        c=c+30
        Label(window3, text=i+1).place(x=0, y=c)
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
    
    Label(window3, text="Posición").place(x=0,y=0)
    Label(window3, text="País").place(x=80,y=0)
    Label(window3, text="   ",background="#CD7F32").place(x=180,y=0)
    Label(window3, text="   ",background="silver").place(x=200,y=0)
    Label(window3, text="   ",background="gold").place(x=220,y=0)
    Label(window3,text="Total").place(x=300,y=0)
    Button(window3, text="Cerrar",background="red",command=window3.destroy).place(x=200,y=300)
    for i in range(len(mPaises)):
        f=160
        a=a+30
        Label(window3, text=opciones[i]).place(x=80,y=a)
        Label(window3,text=sumaT[i]).place(x=300,y=a)
        for j in range(3):
            f=f+20
            Label(window3, text=mPaises[i][j]).place(x=f,y=a)
    window3.mainloop()        
    
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
   
window.mainloop()
