import tkinter as tk
from tkinter import *
from random import randint as r
from tkinter import ttk, messagebox
#import matplotlib.pyplot  as plt
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
d = tk.getint()
mPaises=[]
def pRegistro():
    if nPaises.get()>=5:
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
       resultado = Button(window2, text="Resultado", background="red", command=vResultado).place(x=60, y=350)
       quit = Button(window2, text="     Salir     ", background="red", command=window2.destroy).place(x=100, y=300)
       for i in range(nPaises.get()):
           mPaises.append([0]*3)
       window2.mainloop() 
    else:
       messagebox.showinfo("Error","Ingresar más países")    
    
Button(window, text="Aceptar",bg="red", command=pRegistro, width=10).place(x=100,y=220)
Button(window, text="Salir",bg="red",command=window.destroy,width=10).place(x=100,y=250)
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
     #Con esto está sumando, la matriz se crea más arriba :S
           if a==0:
        #el cero será cambiado por la opción que se elige en el registro, solo es una prueba
              mPaises[i][a]+=bronce
              break
           elif a==1:
        #el cero será cambiado por la opción que se elige en el registro, solo es una prueba
              mPaises[i][a]+=plata
              break
           elif a==2:
        #el cero será cambiado por la opción que se elige en el registro, solo es una prueba 
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
     #for i in range(len(opciones)):
     #   a=a+30
     #   Label(window3, text=opciones[i]).place(x=60,y=a)   
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
    #asd
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
  #def vOro():
  #def vGraf():
    
window.mainloop()