#Logica de Sitemas
#1er Semestre
#Danilo José Portillo Portillo
#0907-19-12800

#Importe de librerias
from tkinter import Tk
import tkinter as tk
from tkinter import*
from tkinter import ttk


#Creacion de ventana
alto = 1080
ancho=1920
ventana = Tk()
ventana.geometry(str(ancho)+'x'+str(alto))
ventana.title("EXAMEN FINAL")


texto=tk.StringVar(value='')
resultado=Label( textvariable = texto,fg="blue",bg="white",font="Helvetica 40")

texto2=tk.StringVar(value='')
res=Label( textvariable = texto2,fg="blue",bg="white",font="Helvetica 20")

def func1():
    texto2.set("")
    resultado.place(x=650,y=500)
    valor_1=int(campo_1.get())
    valor_2=int(campo_2.get())
    valor_3=int(campo_3.get())    
    if(valor_1>valor_3 and valor_2!=0):
        operacion=valor_1*valor_2*valor_3
        texto.set(str(operacion))
        texto2.set("Multiplicacion =")
    elif(valor_1==valor_2 and valor_2==valor_3):
        operacion=valor_1+valor_2+valor_3
        texto.set(str(operacion))
        texto2.set("Suma =")
    elif(valor_2==0):
        if(valor_1>valor_3):
            operacion=valor_1-valor_3
            texto.set(str(operacion))
            texto2.set("Resta")
        else:
            operacion=valor_3-valor_1
            texto.set(str(operacion))
            texto2.set("Resta")    



def func2():
    valor_1=int(campo_1.get())
    valor_2=int(campo_2.get())
    valor_3=int(campo_3.get())
    unido= ""
    auxiliar=(valor_1*valor_2)+valor_3
    for numero in range(auxiliar):
        unido=unido+str(valor_1)+str(valor_2)+str(valor_3)+"-"
        texto2.set(unido)
        resultado.place_forget()
        



campo_1 = tk.Entry(ventana,width="30")
campo_1.place(x=300,y=300)


campo_2 = tk.Entry(ventana,width="30")
campo_2.place(x=650,y=300)



campo_3 = tk.Entry(ventana,width="30")
campo_3.place(x=1000,y=300)


btn_1 = Button(ventana, text="Funcion 1", bg="red",width="25",fg="white", command=func1)
btn_1.place(x=450,y=400)

btn_2 = Button(ventana, text="Funcion 2", bg="blue",width="25",fg="white", command=func2)
btn_2.place(x=850,y=400)

resultado.place(x=650,y=500)
res.place(x=450,y=500)

ventana.mainloop()
