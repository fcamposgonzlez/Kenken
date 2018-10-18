import os #Modulo de control de sistema de python
from time import * #Modulo de tiempo python
from tkinter import * # Modulo de GUI de python
import ast #Modulo para "eval" seguro
import random #Modulo seleccion aleatoria
import pygame #Modulo pygame usado para la música
#import numpy as np
import winsound 
from PIL import Image, ImageTk #Manejo imagenes Python
import tempfile #uso de archivos temporales
import win32api #Modulo uso de 
import win32print # Funciones de windows
import tweepy #Modulo API de Twitter
import json #Modulo API
import itertools
#Variables globales
global Timer
Timer = False
global state
state = True
global TimeCounter
TimeCounter = 0
Lista = []
Top10 = []
global Nivel
Nivel = 4
global Mx
Mx = -1
global My
My = -1
global sonido
sonido = True
global multinivel
multinivel = False
#Clase jugar
        
class Jugar:
#Inicio de Juego  
        
    def __init__ (self):
        global Nivel
        if multinivel == True:
            Nivel = 3
        self.Pila1 = []
        self.Pila2 = []
        VentanaPrincipal.iconify()
        self.MatrizPrin = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            ]
        self.juegokenkensolover()
    #Juego de kenken para iniciar el juego 
    def juegokenkensolover (self):
        self.Nombrejug = StringVar()
        self.Vjugar = Toplevel()
        self.Vjugar.title("KenKen:Jugar")
        LabelConfig = Label (self.Vjugar, text = "KENKEN",fg= "Dark Green", font = "Times 40").grid(row=0,column=2,rowspan = 2,columnspan = Nivel)
        self.Matrizsolover()
        BIniJugar = Button (self.Vjugar, bg="Red", activebackground = "Pink", relief = "groove",text = "Iniciar Juego",width = "11", font = "Times 15",command=lambda: self.iniciarkenken()).grid(row=11,column=0,columnspan = 3)
        BValJuego = Button (self.Vjugar, bg="Green", activebackground = "Light Green", relief = "groove",text = "Validar Juego",width = "11", font = "Times 15").grid(row=11,column=3,columnspan = 3)
        BOtrJuego = Button (self.Vjugar, bg="Navy", activebackground = "light blue", relief = "groove",text = "Otro Juego",width = "11", font = "Times 15").grid(row=11,column=6,columnspan = 3)
        BReiniJuego = Button (self.Vjugar, bg="Orange", activebackground = "Light pink", relief = "groove",text = "Reiniciar Juego",width = "11", font = "Times 15").grid(row=11,column=9,columnspan = 3)
        BTerJuego = Button (self.Vjugar, bg="Pink", activebackground = "white", relief = "groove",text = "Terminar Juego",width = "11", font = "Times 15").grid(row=11,column=12,columnspan = 3)
        BTop10 = Button (self.Vjugar, bg="Yellow", activebackground = "light yellow", relief = "groove",text = "Top 10",width = "11", font = "Times 15").grid(row=12,column=12,columnspan = 3)
        LNomjug = Label (self.Vjugar, text = "Digite su nombre",fg= "Purple", font = "Times 20").grid(row=12,column=0,columnspan = 3)  
        ENomjug = Entry(self.Vjugar,textvariable = self.Nombrejug,width=30).grid(row=12,column = 4,columnspan = 3)

#Reiniciar el juego
    def reiniciar(self):
        global  Timer
        self.Pila1 = []
        self.Pila2 = []
        self.MatrizPrin = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            ]
        if Timer == False:
            self.s=0
            self.m=0
            self.h=0
            self.CreaMatrizBot()
        else:
            self.Vconfigtimer = Toplevel ()
            self.Vconfigtimer.title ("Timer")
            self.se = IntVar()
            self.mi = IntVar()
            self.ho = IntVar()
            LabelTimer = Label (self.Vconfigtimer, text = "Timer", fg= "Dark Green", font = "Times 40").grid(row=0,column=0,columnspan = 2)
            Labelhoras = Label (self.Vconfigtimer, text = "Horas", font = "Times 20").grid(row=1,column=0)
            Labelminutos = Label (self.Vconfigtimer, text = "Minutos", font = "Times 20").grid(row=2,column=0)
            Labelsegundos = Label (self.Vconfigtimer, text = "Segundos", font = "Times 20").grid(row=3,column=0)
            Entryhoras = Entry(self.Vconfigtimer, textvariable=self.ho).grid(row=1,column = 1)
            Entryminutos = Entry(self.Vconfigtimer, textvariable=self.mi).grid(row=2,column = 1)
            Entrysegundos = Entry(self.Vconfigtimer, textvariable=self.se).grid(row=3,column = 1)
            BOkTimer = Button (self.Vconfigtimer, bg="Green", command = self.OkTimer, activebackground = "Light Green", relief = "groove",text = "Ok",width = "20", font = "Times 20").grid(row = 4,column = 0, columnspan = 2)
        
#Iniciar el juego de kenken        
    def iniciarkenken (self):
        if len(self.Nombrejug.get()) < 3 or len(self.Nombrejug.get()) >30:
            self.datequiperror = messagebox.showerror("ERROR","Error, cantidad de caracteres admitidos en Nombre es entre 3 hasta 30",parent=self.Vjugar)
        else:
            self.Vjugar.destroy()
            if Timer == False:
                self.s=0
                self.m=0
                self.h=0
                self.Vjugar.after(100,self.Timer)
                self.juegokenken()
            elif Timer == True:
                self.Vconfigtimer = Toplevel ()
                self.Vconfigtimer.title ("Timer")
                self.se = IntVar()
                self.mi = IntVar()
                self.ho = IntVar()
                LabelTimer = Label (self.Vconfigtimer, text = "Timer", fg= "Dark Green", font = "Times 40").grid(row=0,column=0,columnspan = 2)
                Labelhoras = Label (self.Vconfigtimer, text = "Horas", font = "Times 20").grid(row=1,column=0)
                Labelminutos = Label (self.Vconfigtimer, text = "Minutos", font = "Times 20").grid(row=2,column=0)
                Labelsegundos = Label (self.Vconfigtimer, text = "Segundos", font = "Times 20").grid(row=3,column=0)
                Entryhoras = Entry(self.Vconfigtimer, textvariable=self.ho).grid(row=1,column = 1)
                Entryminutos = Entry(self.Vconfigtimer, textvariable=self.mi).grid(row=2,column = 1)
                Entrysegundos = Entry(self.Vconfigtimer, textvariable=self.se).grid(row=3,column = 1)
                BOkTimer = Button (self.Vconfigtimer, bg="Green", command = self.OkTimer, activebackground = "Light Green", relief = "groove",text = "Ok",width = "20", font = "Times 20").grid(row = 4,column = 0, columnspan = 2)
            else:
                self.juegokenken()
#Boton de Aceptar del Timer
    def OkTimer (self):
        self.st = self.se.get() 
        self.mt = self.mi.get()
        self.ht = self.ho.get()
        self.s = self.se.get()
        self.m = self.mi.get()
        self.h = self.ho.get()
        if self.s < 0 or self.s > 60 or self.m < 0 or self.m > 60 or self.h < 0 or self.h > 24:
            self.datequiperror = messagebox.showerror("ERROR","Error, Ingrese una hora valida",parent=self.Vconfigtimer)
        else:
            self.Vconfigtimer.destroy()
            self.Vjugar.after(100,self.Timer)
            self.juegokenken()
        
#Creacion de matriz donde los botones no hacen nada
    def Matrizsolover (self):
        self.opciones = []
        self.Listasjuegonivel = []
        global Nivel
        self.configuracionkenken = {}
        for linea in open("kenken_juegos.dat","r"):
            contador = 0
            self.configuracionkenken = ast.literal_eval(linea)
            contador = 0
            for y in range (len(self.configuracionkenken)):
                for x in range (1,len(self.configuracionkenken[y+1])):
                    contador+=1
            if contador == Nivel*Nivel:
                self.Listasjuegonivel.append(self.configuracionkenken)
        self.diccionario = random.choice(self.Listasjuegonivel)
        self.Listasjuegonivel.remove(self.diccionario)
        self.all_buttons = []
        for x in range(Nivel):
            buttons_row = []
            for y in range(Nivel):
                self.boton = Button(self.Vjugar, highlightcolor = "light blue", width=5, height=3, text = str(self.MatrizPrin[x][y]))
                self.boton.grid(row=x+2, column=y+2,sticky = "WENS")
                buttons_row.append( self.boton )
            self.all_buttons.append( buttons_row )
        contador = 0
        colorestxt = open("colores.txt","r")
        colores = colorestxt.readline()
        colores = ast.literal_eval(colores)
        for p in range(len(self.diccionario)):            
            for t in range (1,len(self.diccionario[p+1])):
                if t == 1:
                    tuplas = self.diccionario[p+1]
                    r=tuplas[t][0]-1+2
                    c=tuplas[t][1]-1+2
                    Labelnumero=Label(self.Vjugar,text=tuplas[0],font = "Times 12") 
                    Labelnumero.grid(row=r,column=c,sticky = "NW")
                f=tuplas[t][0]-1
                g=tuplas[t][1]-1
                self.all_buttons[f][g]["bg"]= colores[contador]
            contador=contador+1
        for x in range (Nivel):
            self.boton = Button(self.Vjugar, width=5, height=3, text = str(x+1),bg="light blue")
            self.boton.grid(row=x+2, column=Nivel + 2)
            self.opciones.append (self.boton)

#Inicio del juego de kenken        
    def juegokenken (self):
        self.Vjugar = Toplevel()
        self.Vjugar.title("KenKen:Jugar")
        LabelConfig = Label (self.Vjugar, text = "KENKEN", fg= "Dark Green", font = "Times 40").grid(row=0,column=2,rowspan = 2,columnspan = Nivel)
        self.Matriz()
        BIniJugar = Button (self.Vjugar, bg="Red", activebackground = "Pink", relief = "groove",text = "Iniciar Juego",width = "11", font = "Times 15").grid(row=11+2,column=0,columnspan = 3)
        BValJuego = Button (self.Vjugar,command = self.ValidarJuego, bg="Green", activebackground = "Light Green", relief = "groove",text = "Validar Juego",width = "11", font = "Times 15").grid(row=11+2,column=3,columnspan = 3)
        BOtrJuego = Button (self.Vjugar,command = self.OtroJuego, bg="Navy", activebackground = "light blue", relief = "groove",text = "Otro Juego",width = "11", font = "Times 15").grid(row=11+2,column=6,columnspan = 3)
        BReiniJuego = Button (self.Vjugar,command = self.reiniciar, bg="Orange", activebackground = "Light pink", relief = "groove",text = "Reiniciar Juego",width = "11", font = "Times 15").grid(row=11+2,column=9,columnspan = 3)
        BTerJuego = Button (self.Vjugar,command = self.TerminarJuego , bg="Pink", activebackground = "white", relief = "groove",text = "Terminar Juego",width = "11", font = "Times 15").grid(row=11+2,column=12,columnspan = 3)
        BTop10 = Button (self.Vjugar,command = self.Top10, bg="Yellow", activebackground = "light yellow", relief = "groove",text = "Top 10",width = "11", font = "Times 15").grid(row=12+2,column=12,columnspan = 3)
        BGuardar = Button (self.Vjugar,command = self.Guardar, bg="Green", activebackground = "Light Green", relief = "groove",text = "Guardar",width = "11", font = "Times 15").grid(row=10+2,column=0,columnspan = 3)
        BCargar = Button (self.Vjugar,command = self.Cargar, bg="Blue", activebackground = "Light Blue", relief = "groove",text = "Cargar",width = "11", font = "Times 15").grid(row=10+2,column=3,columnspan = 3)
        BDeshacer = Button (self.Vjugar,command = self.Deshacer , bg="Brown", activebackground = "white", relief = "groove",text = "Deshacer",width = "11", font = "Times 15").grid(row=10+2,column=6,columnspan = 3)
        BReahacer = Button (self.Vjugar,command = self.Rehacer, bg="Turquoise", activebackground = "light Blue", relief = "groove",text = "Rehacer",width = "11", font = "Times 15").grid(row=10+2,column=9,columnspan = 3)
        BBorrar = Button (self.Vjugar,command = self.Borrar, bg="Red", activebackground = "white", relief = "groove",text = "Borrar",width = "11", font = "Times 15").grid(row=10+2,column=12,columnspan = 3)
        LNomjug = Label (self.Vjugar, text = self.Nombrejug.get(),fg= "turquoise", font = "Times 23").grid(row=12+2,column=0,columnspan = 6)  
        BSolucionar = Button (self.Vjugar,command = self.Solucionar, bg="Green", activebackground = "white", relief = "groove",text = "Solucionar",width = "11", font = "Times 15").grid(row=9+2,column=12,columnspan = 3)
        BPosibles = Button (self.Vjugar,command = self.Pista, bg="Turquoise", activebackground = "white", relief = "groove",text = "Pista",width = "11", font = "Times 15").grid(row=9+2,column=9,columnspan = 3)
        BPausa = Button (self.Vjugar,command = self.BotDeact, bg="Grey", activebackground = "white", relief = "groove",text = "Pausa",width = "9", font = "Times 15").grid(row=2,column=12,columnspan = 3)
        self.LTimer = Label(self.Vjugar,text = "Timer",fg= "turquoise", font = "Times 23")
        self.LTimer.grid(row=0,column=12,columnspan = 2,rowspan = 2)
#Funcion de Guardado
    def Guardar (self):
        global Nivel        
        self.guardado = open ("Guardar.txt","w")
        self.guardado.write(str([self.MatrizPrin,[self.s,self.m,self.h],Nivel,self.Nombrejug.get()]))
        self.guardado.close()
        self.dictio = open ("Dic.txt", "w")
        self.dictio.write(str(self.diccionario))
        self.dictio.close()
#Funcion de cargar
    def Cargar (self):
        self.Vjugar.destroy()
        return self.Cargar_aux()
    
    def Cargar_aux (self):
        global Nivel
        self.Vjugar = Toplevel()
        self.Vjugar.title("KenKen:Jugar")
        LabelConfig = Label (self.Vjugar, text = "KENKEN", fg= "Dark Green", font = "Times 40").grid(row=0,column=2,rowspan = 2,columnspan = Nivel)
        self.guardado = open ("Guardar.txt","r")
        self.Informacion = ast.literal_eval(self.guardado.readline())
        self.MatrizPrin = self.Informacion[0]
        self.s=self.Informacion[1][0]
        self.m=self.Informacion[1][1]
        self.h=self.Informacion[1][2]
        Nivel = self.Informacion[2]
        self.Nombrejug = self.Informacion[3] 
        self.Botones1(0,0)
        self.dictio = open ("Dic.txt", "r")
        self.diccionario =ast.literal_eval(self.dictio.readline())
        contador = 0
        colorestxt = open("colores.txt","r")
        self.colores = colorestxt.readline()
        self.colores = ast.literal_eval(self.colores)
        self.Botones2(0,1,0)
        self.Botones3(0)
        BIniJugar = Button (self.Vjugar, bg="Red", activebackground = "Pink", relief = "groove",text = "Iniciar Juego",width = "11", font = "Times 15").grid(row=11+2,column=0,columnspan = 3)
        BValJuego = Button (self.Vjugar,command = self.ValidarJuego, bg="Green", activebackground = "Light Green", relief = "groove",text = "Validar Juego",width = "11", font = "Times 15").grid(row=11+2,column=3,columnspan = 3)
        BOtrJuego = Button (self.Vjugar,command = self.OtroJuego, bg="Navy", activebackground = "light blue", relief = "groove",text = "Otro Juego",width = "11", font = "Times 15").grid(row=11+2,column=6,columnspan = 3)
        BReiniJuego = Button (self.Vjugar,command = self.reiniciar, bg="Orange", activebackground = "Light pink", relief = "groove",text = "Reiniciar Juego",width = "11", font = "Times 15").grid(row=11+2,column=9,columnspan = 3)
        BTerJuego = Button (self.Vjugar,command = self.TerminarJuego , bg="Pink", activebackground = "white", relief = "groove",text = "Terminar Juego",width = "11", font = "Times 15").grid(row=11+2,column=12,columnspan = 3)
        BTop10 = Button (self.Vjugar,command = self.Top10, bg="Yellow", activebackground = "light yellow", relief = "groove",text = "Top 10",width = "11", font = "Times 15").grid(row=12+2,column=12,columnspan = 3)
        BGuardar = Button (self.Vjugar,command = self.Guardar, bg="Green", activebackground = "Light Green", relief = "groove",text = "Guardar",width = "11", font = "Times 15").grid(row=10+2,column=0,columnspan = 3)
        BCargar = Button (self.Vjugar,command = self.Cargar, bg="Blue", activebackground = "Light Blue", relief = "groove",text = "Cargar",width = "11", font = "Times 15").grid(row=10+2,column=3,columnspan = 3)
        BDeshacer = Button (self.Vjugar,command = self.Deshacer , bg="Brown", activebackground = "white", relief = "groove",text = "Deshacer",width = "11", font = "Times 15").grid(row=10+2,column=6,columnspan = 3)
        BReahacer = Button (self.Vjugar,command = self.Rehacer, bg="Turquoise", activebackground = "light Blue", relief = "groove",text = "Rehacer",width = "11", font = "Times 15").grid(row=10+2,column=9,columnspan = 3)
        BBorrar = Button (self.Vjugar,command = self.Borrar, bg="Red", activebackground = "white", relief = "groove",text = "Borrar",width = "11", font = "Times 15").grid(row=10+2,column=12,columnspan = 3)
        BSolucionar = Button (self.Vjugar,command = self.Solucionar, bg="Green", activebackground = "white", relief = "groove",text = "Solucionar",width = "11", font = "Times 15").grid(row=9+2,column=12,columnspan = 3)
        BPosibles = Button (self.Vjugar,command = self.Pista, bg="Turquoise", activebackground = "white", relief = "groove",text = "Pista",width = "11", font = "Times 15").grid(row=9+2,column=9,columnspan = 3)
        LNomjug = Label (self.Vjugar, text = self.Nombrejug,fg= "turquoise", font = "Times 23").grid(row=12,column=0,columnspan = 6)  
        BPausa = Button (self.Vjugar,command = self.BotDeact, bg="Grey", activebackground = "white", relief = "groove",text = "Pausa",width = "9", font = "Times 15").grid(row=2,column=12,columnspan = 3)
        self.LTimer = Label(self.Vjugar,text = "Timer",fg= "turquoise", font = "Times 23")
        self.LTimer.grid(row=0,column=12,columnspan = 2,rowspan = 2)
        self.Timer()
#Estos Botones son para crear recursivamente los botones 
    def Botones1_aux (self,x,y,buttons_row):
        global Nivel
        if Nivel == x:
            return self.all_buttons
        else:
            if y == 0:
                buttons_row = []
            else:
                pass
            if y == Nivel:
                self.all_buttons.append (buttons_row)
                return self.Botones1_aux(x+1,0,[])
            else:
                boton = Button(self.Vjugar,highlightcolor = "light blue",width=5, height=3, text = str(self.MatrizPrin[x][y]),command=lambda a=x,b=y: self.botonesmatriz(a,b))
                boton.grid(row=x+2, column=y+2,sticky = "WENS")
                buttons_row.append(boton)
                return self.Botones1_aux(x,y+1,buttons_row)
            
    def Botones1 (self,x,y):
        buttons_row = []
        self.all_buttons = []
        return self.Botones1_aux (x,y,buttons_row)
        
    def Botones2 (self,x,y,contador):
        if x == len(self.diccionario):
            return 0
        elif y == len(self.diccionario[x+1]):
            return self.Botones2 (x+1,1,contador+1) 
        elif y == 1:
            self.tuplas = self.diccionario[x+1]
            r=self.tuplas[y][0]-1+2
            c=self.tuplas[y][1]-1+2
            Labelnumero=Label(self.Vjugar,text=self.tuplas[0],font = "Times 12") 
            Labelnumero.grid(row=r,column=c,sticky = "NW")
        f=self.tuplas[y][0]-1
        g=self.tuplas[y][1]-1
        self.all_buttons[f][g]["bg"] = self.colores[contador]
        return self.Botones2 (x,y+1,contador)

    def Botones3 (self,x):
        if x == Nivel:
            return 0
        else:
            self.boton = Button(self.Vjugar, width=6, height=3, text = str(x+1),bg="light blue",command=lambda a=x+1: self.botonesopciones(a))
            self.boton.grid(row=x+2, column=Nivel + 2)
            self.opciones.append (self.boton)
            return self.Botones3 (x+1)
#Deshacer                     
    def Deshacer (self):
        if self.Pila1 == []:
            pass
        else:
            bot = self.Pila1.pop()
            self.Pila2.append(bot)
            print(self.Pila2)
            if self.Pila1 == []:
                self.MatrizPrin = [
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]
                ]
                self.CreaMatrizBot()    
            else:
                self.MatrizPrin = self.Pila1[-1]
                self.CreaMatrizBot()
#Funcion Rehacer                
    def Rehacer (self):
        if self.Pila2 == []:
            pass
        else:
            self.Pila2
            self.MatrizPrin = self.Pila2[-1]
            bot = self.Pila2.pop()
            self.Pila1.append(bot)
            self.CreaMatrizBot()
#Funcion para otro juego
    def OtroJuego (self):
        try:
            global multinivel
            if multinivel == True:
                Nivel = 3
            self.Pila1 = []
            self.Pila2 = []
            self.MatrizPrin = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
            ]
            self.s=0
            self.m=0
            self.h=0
            self.diccionario = random.choice(self.Listasjuegonivel)
            self.Listasjuegonivel.remove(self.diccionario)
            self.all_buttons = []
            for x in range(Nivel):
                buttons_row = []
                for y in range(Nivel):
                    self.boton = Button(self.Vjugar,highlightcolor = "light blue",width=5, height=3, text = str(self.MatrizPrin[x][y]),command=lambda a=x,b=y: self.botonesmatriz(a,b))
                    self.boton.grid(row=x+2, column=y+2,sticky = "WENS")
                    buttons_row.append( self.boton )
                self.all_buttons.append( buttons_row )
            contador = 0
            colorestxt = open("colores.txt","r")
            colores = colorestxt.readline()
            colores = ast.literal_eval(colores)
            for p in range(len(self.diccionario)):            
                for t in range (1,len(self.diccionario[p+1])):
                    if t == 1:
                        tuplas = self.diccionario[p+1]
                        r=tuplas[t][0]-1+2
                        c=tuplas[t][1]-1+2
                        Labelnumero=Label(self.Vjugar,text=tuplas[0],font = "Times 12") 
                        Labelnumero.grid(row=r,column=c,sticky = "NW")
                    f=tuplas[t][0]-1
                    g=tuplas[t][1]-1
                    self.all_buttons[f][g]["bg"]= colores[contador]
                contador=contador+1
            for x in range (Nivel):
                self.boton = Button(self.Vjugar, width=6, height=3, text = str(x+1),bg="light blue",command=lambda a=x+1: self.botonesopciones(a))
                self.boton.grid(row=x+2, column=Nivel + 2)
                self.opciones.append (self.boton)
        except:
            self.datequiperror = messagebox.showerror("Error","Se ha quedado sin juegos para este nivel",parent=self.Vjugar)
#Funcion para terminar el juego        
    def TerminarJuego (self):
        self.Vjugar.destroy()
        VentanaPrincipal.deiconify()
#Funcion para crear la matriz        
    def Matriz (self):
        self.opciones = []
        self.Listasjuegonivel = []
        global Nivel
        self.configuracionkenken = {}
        for linea in open("kenken_juegos.dat","r"):
            contador = 0
            self.configuracionkenken = ast.literal_eval(linea)
            contador = 0
            for y in range (len(self.configuracionkenken)):
                for x in range (1,len(self.configuracionkenken[y+1])):
                    contador+=1
            if contador == Nivel*Nivel:
                self.Listasjuegonivel.append(self.configuracionkenken)
        self.diccionario = random.choice(self.Listasjuegonivel)
        self.Listasjuegonivel.remove(self.diccionario)
        self.CreaMatrizBot()
#Funcion para validar juego y publicar en twitter       
    def ValidarJuego(self):
        global Nivel
        contador = 0
        Validacion = 0
        for x in range (Nivel):
            if Validacion != 0:
                break
            for y in range(Nivel):
                if self.MatrizPrin[x][y] == 0:
                    self.datequiperror = messagebox.showerror("Error","Favor rellene todas las casillas",parent=self.Vjugar)
                    Validacion = 1
                    break
        if Validacion == 0:
            Vale = 0
            for x in range (Nivel):
                for y in range(Nivel):
                    secondM = self.MatrizPrin
                    Matriznumpy = np.array(secondM)
                    Matriznumpy = list(Matriznumpy[:,y])
                    print(Matriznumpy)
                    print(Matriznumpy.count(self.MatrizPrin[x][y]))
                    if self.MatrizPrin[x].count(self.MatrizPrin[x][y]) > 1 or Matriznumpy.count(self.MatrizPrin[x][y]) > 1:
                        self.all_buttons[x][y]['bg'] = "Red"
                        self.all_buttons[x][y].after(100,self.Etiqueta)
                        Vale +=1 
                    else:
                        contador+=1
                    if contador == Nivel*Nivel:
                        for p in range(len(self.diccionario)):
                            listaresta = []
                            listadivision = []
                            Listaaccion = [] 
                            contador = 1
                            for t in range (1,len(self.diccionario[p+1])):
                                if t == 1:
                                    tuplas = self.diccionario[p+1]
                                    numsig= tuplas[0]
                                    sig = numsig[-1]
                                    resultado = int(numsig.replace(sig, ""))
                                    print(resultado)
                                    if sig == "+":
                                        result=0
                                    elif sig == "-":
                                        result=0
                                    elif sig == "/":
                                        result = 1
                                    elif sig == "x":
                                        result=1
                                f=tuplas[t][0]-1
                                g=tuplas[t][1]-1
                                Listaaccion.append(tuplas[t])
                                print(Listaaccion)
                                if sig == "+":
                                    result=result+self.MatrizPrin[f][g]
                                elif sig == "-":
                                    listaresta.append(self.MatrizPrin[f][g])
                                elif sig == "/":
                                    listadivision.append(self.MatrizPrin[f][g])
                                elif sig == "x" or "*":
                                    result=result*self.MatrizPrin[f][g]
                                contador+=1     
                                if contador == len(self.diccionario[p+1]):
                                    if listadivision != []:
                                        listadivision.sort(reverse = True)
                                        print(listadivision)
                                        for s in range(len(listadivision)):
                                            if s == 0:
                                                result = listadivision [s]
                                            else:
                                                result = result/listadivision[s] 
                                    elif listaresta != []:
                                        listaresta.sort(reverse = True)
                                        print (listaresta)
                                        for s in range(len(listaresta)):
                                            if s == 0:
                                                result = listaresta [s]
                                            else:
                                                result = result-listaresta[s]                                            
                                    print(result,resultado)
                                    if result != resultado:
                                        for p in range(len(Listaaccion)):
                                            self.all_buttons[Listaaccion[p][0]-1][Listaaccion[p][1]-1]['bg'] = "Red"
                                            self.all_buttons[Listaaccion[p][0]-1][Listaaccion[p][1]-1].after(100,self.Etiqueta)
                                            Vale +=1
        if Vale == 0:
            global TimeCounter
            TimeCounter+=1
            if TimeCounter == 1:
                global state
                state = False
            with open("Top"+str(Nivel)+".txt", "a") as myfile:
                if Timer == False:
                    myfile.write(str((self.Nombrejug.get(),self.h,self.m,self.s))+"\n")
                elif Timer == True:
                    horatotal = self.ht*3600 + self.mt*60 + self.st
                    horajugada = self.h*3600 + self.m * 60 + self.s
                    Horatotal = horatotal-horajugada
                    self.Conversor (Horatotal)
                    myfile.write(str((self.Nombrejug.get(),self.h,self.m,self.s))+"\n")
            winsound.PlaySound("Tada",winsound.SND_FILENAME)
            if multinivel == False:
                otrojuego = messagebox.askyesno("FELICIDADES", "Desea jugar otra partida?")
                if otrojuego == True:
                    self.OtroJuego()
                else:
                    self.Vjugar.destroy()
            else:
                Nivel += 1
                if Nivel == 10:
                    otrojuego = messagebox.askyesno("FELICIDADES", "Has ganado!, desea jugar otra vez?")
                    if otrojuego == True:
                        self.OtroJuego()
                    else:
                        self.Vjugar.destroy()
                else:
                    self.iniciarkenken()
#Conversor de segundos para el Timer                    
    def Conversor (self,x):
        num=x  
        self.h=(int(num/3600))  
        self.m=int((num-(hor*3600))/60)  
        self.s=num-((self.h*3600)+(self.m*60))
#Funcion para actualizar ventana                    
    def Etiqueta (self):
        LabelVal=Label(self.Vjugar,text = "",fg= "Green", font = "Times 23")
        LabelVal.grid(row=4, column = 8)                         
#Creacion de Botones para las ventanas 
 
    def CreaMatrizBot (self):
        self.all_buttons = []
        for x in range(Nivel):
            buttons_row = []
            for y in range(Nivel):
                self.boton = Button(self.Vjugar,highlightcolor = "light blue",width=5, height=3, text = str(self.MatrizPrin[x][y]),command=lambda a=x,b=y: self.botonesmatriz(a,b))
                self.boton.grid(row=x+2, column=y+2,sticky = "WENS")
                buttons_row.append( self.boton )
            self.all_buttons.append( buttons_row )
        contador = 0    
        colorestxt = open("colores.txt","r")
        colores = colorestxt.readline()
        colores = ast.literal_eval(colores)
        for p in range(len(self.diccionario)):            
            for t in range (1,len(self.diccionario[p+1])):
                if t == 1:
                    tuplas = self.diccionario[p+1]
                    r=tuplas[t][0]-1+2
                    c=tuplas[t][1]-1+2
                    Labelnumero=Label(self.Vjugar,text=tuplas[0],font = "Times 12") 
                    Labelnumero.grid(row=r,column=c,sticky = "NW")
                f=tuplas[t][0]-1
                g=tuplas[t][1]-1
                self.all_buttons[f][g]["bg"]= colores[contador]
            contador=contador+1       
        for x in range (Nivel):
            self.boton = Button(self.Vjugar, width=5, height=3, text = str(x+1),command=lambda a=x+1: self.botonesopciones(a),bg="light blue")
            self.boton.grid(row=x+2, column=Nivel + 2)
            self.opciones.append (self.boton)
#Botones pausa        
            
    def BotDeact (self):
        pygame.mixer.music.pause()
        global TimeCounter
        TimeCounter+=1
        if TimeCounter == 1:
            global state
            state = False
            self.all_buttons = []
            for x in range(Nivel):
                buttons_row = []
                for y in range(Nivel):
                    self.boton = Button(self.Vjugar,state=DISABLED, highlightcolor = "light blue",width=5, height=3, text = str(self.MatrizPrin[x][y]),command=lambda a=x,b=y: self.botonesmatriz(a,b))
                    self.boton.grid(row=x+2, column=y+2,sticky = "WENS")
                    buttons_row.append( self.boton )
                self.all_buttons.append( buttons_row )
            contador = 0    
            colorestxt = open("colores.txt","r")
            colores = colorestxt.readline()
            colores = ast.literal_eval(colores)
            for p in range(len(self.diccionario)):            
                for t in range (1,len(self.diccionario[p+1])):
                    if t == 1:
                        tuplas = self.diccionario[p+1]
                        r=tuplas[t][0]-1+2
                        c=tuplas[t][1]-1+2
                        Labelnumero=Label(self.Vjugar,text=tuplas[0],font = "Times 12") 
                        Labelnumero.grid(row=r,column=c,sticky = "NW")
                    f=tuplas[t][0]-1
                    g=tuplas[t][1]-1
                    self.all_buttons[f][g]["bg"]= colores[contador]
                contador=contador+1
            for x in range (Nivel):
                self.boton = Button(self.Vjugar,state = DISABLED, width=6, height=3, text = str(x+1),bg="light blue")
                self.boton.grid(row=x+2, column=Nivel + 2)
                self.opciones.append (self.boton)    
        else:
            TimeCounter = 0
            state = True
            self.Timer()
            self.CreaMatrizBot()
            pygame.mixer.music.unpause()
#Utilizacion de los botones de accion    
    def botonesopciones (self,z):
        global Mx
        global My
        lol = self.Vjugar.focus_get()
        self.MatrizPrin[Mx][My] = z
        MatrizActual = open("MatrizActual.txt", "w")
        MatrizActual.write(str(self.MatrizPrin))
        MatrizActual.close()
        MatrizActual = open("MatrizActual.txt", "r")
        MatrizActual1 = MatrizActual.read()
        MatrizActual.close()
        MatrizActual = ast.literal_eval(MatrizActual1)
        self.Pila1.append(MatrizActual)
        self.CreaMatrizBot()
         
#Funcion para borrar
    def Borrar(self):
        global Mx
        global My
        lol = self.Vjugar.focus_get()
        self.MatrizPrin[Mx][My] = 0
        MatrizActual = open("MatrizActual.txt", "w")
        MatrizActual.write(str(self.MatrizPrin))
        MatrizActual.close()
        MatrizActual = open("MatrizActual.txt", "r")
        MatrizActual1 = MatrizActual.read()
        MatrizActual.close()
        MatrizActual = ast.literal_eval(MatrizActual1)
        self.Pila1.append(MatrizActual)
        self.CreaMatrizBot()
#Funcion para las funciones de los botones        
    def botonesmatriz (self,x,y):
        global Mx
        global My
        Mx = x
        My = y
        defaultbg = self.Vjugar.cget('bg')
        self.all_buttons[x][y].focus_set()
#Funcion de reloj y timer
    
    def Timer (self):
        global Timer
        if Timer == False:
            if (state):
                self.s += 1
                self.LTimer.configure(text=str(self.h)+":"+str(self.m)+":"+str(self.s))
                if self.s==60:
                    self.m=self.m+1
                    self.s=0
                elif self.m==60:
                    self.s=0
                    self.m=0
                    self.h=h+1
                self.LTimer.after(1000, self.Timer)
        else:
            if (state):
                self.s -= 1
                self.LTimer.configure(text=str(self.h)+":"+str(self.m)+":"+str(self.s))
                if self.s==0 and self.m!=0:
                    self.m=self.m-1
                    self.s=60
                elif self.m==0 and self.s == 0:
                    self.s=60
                    self.m=0
                    self.h=self.h-1
                self.LTimer.after(1000, self.Timer)
                if self.s == 0 and self.m == 0 and self.h == 0:
                    Timeover = messagebox.askyesno("ERROR", "Se acabó el tiempo, desea continuar?")
                    if Timeover == True:
                        Timer = 0
                    else:
                        self.Vjugar.destroy()
#Funcion Top 10 
    def Top10 (self):
        self.VTopten = Toplevel(self.Vjugar) 
        Labeltop = Label (self.VTopten, text = "Top 10",pady = "5", fg= "Dark Blue", font = "Times 60").pack()
        lines = []
        lel = open("Top.txt", 'w')
        with open("Top"+str(Nivel)+".txt", 'r') as infile:
            for line in infile:
                line = ast.literal_eval(line)
                lines.append(line)
        lines.sort(key = lambda x: x[1])
        lines.sort(key = lambda x: x[2])
        lines.sort(key = lambda x: x[3])
        with open("Top"+str(Nivel)+".txt", 'r') as outfile:
            for Line in lines[-10:]:
                with open("Top.txt", "a") as myfile:
                    myfile.write(Line[0]+" = "+str(Line[1])+":"+str(Line[2])+":"+str(Line[3]))
                    LabelConfig = Label (self.VTopten, text =Line[0]+" = "+str(Line[1])+":"+str(Line[2])+":"+str(Line[3]), fg= "Blue", font = "Times 20")
                LabelConfig.pack()
        image = Image.open("impresora.png")
        photo = ImageTk.PhotoImage(image)
        BImprimir = Button (self.VTopten,image=photo, command = self.Imprimir)
        BImprimir.image = photo 
        BImprimir.pack()         
#Funcion imprimir               
    def Imprimir (self):
        os.startfile("Top.txt", "print")


#Funcion Solucionar Kenken
    def Solucionar(self):
        global Nivel
        global listajugadas
        row = 0
        column = 0
        opcion = 1
        listajugadas = []
        self.MatrizPrin = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
            ]
        self.jugadas = list(self.diccionario.values())
        while row != Nivel:
            while True:
                Vali = False
                if Nivel == row:
                    break
                columnsolu = []
                listadenumeros = []
                listaresta = []
                listadivision = []
                rowsolu = self.MatrizPrin[row]
                num = self.jugadas[row][0]
                sig = self.jugadas[row][0][-1]
                numsig = int( num.replace(sig, ""))
                for z in range (Nivel):
                    columnsolu.append(self.MatrizPrin[z][column])
                if opcion > Nivel:
                    try:
                        self.MatrizPrin[row][column] = 0
                        row = listajugadas[-1][0]
                        column = listajugadas [-1][1]
                        opcion = listajugadas [-1][2]+1
                        del listajugadas [-1]
                        break
                    except:
                        self.MatrizPrin[row][column] = 0
                        row = 0
                        column = 0
                        opcion = 1
                        del listajugadas[-1]
                        break
                elif opcion not in rowsolu and opcion not in columnsolu:
                    self.MatrizPrin[row][column] = opcion
                    for x in range (len(self.jugadas)):
                        for y in range (1,len(self.jugadas[x])):
                            if self.jugadas[x][y] == (row+1,column+1):
                                Vali = True
                                for z in range (1,len(self.jugadas[x])):
                                    listadenumeros.append(self.MatrizPrin[self.jugadas[x][z][0]-1][self.jugadas[x][z][1]-1])
                                if 0 in listadenumeros:
                                    listajugadas.append([row,column,opcion])
                                    if column == Nivel-1:
                                        row += 1
                                        column = 0
                                        opcion = 1
                                        break
                                    else:
                                        column += 1
                                        opcion = 1
                                        break
                                else:
                                    num = self.jugadas[x][0]
                                    sig = self.jugadas[x][0][-1]
                                    numsig = int(num.replace(sig, ""))
                                    if sig == "+":
                                        resultado = 0
                                        for n in range (len(listadenumeros)):
                                            resultado += listadenumeros[n]    
                                        if resultado == numsig:
                                            listajugadas.append([row,column,opcion])
                                            if column == Nivel - 1:
                                                row += 1
                                                column = 0
                                                opcion = 1
                                                break
                                            else:
                                                column += 1
                                                opcion = 1
                                                break
                                        elif opcion == Nivel:
                                            try:
                                                self.MatrizPrin[row][column] = 0
                                                row = listajugadas[-1][0]
                                                column = listajugadas [-1][1]
                                                opcion = listajugadas [-1][2]+1
                                                del listajugadas [-1]
                                                break
                                            except:
                                                self.MatrizPrin[row][column] = 0
                                                row = 0
                                                column = 0
                                                opcion = 1
                                                del listajugadas [-1]
                                                break
                                        else:
                                            opcion += 1
                                            break
                                    elif sig == "-":
                                        listadenumeros.sort(reverse = True)
                                        resultado = listadenumeros.pop(0)
                                        for n in range (len(listadenumeros)):
                                            resultado -= listadenumeros[n] 
                                        if resultado == numsig:
                                            listajugadas.append([row,column,opcion])
                                            if column == Nivel - 1:
                                                row += 1
                                                column = 0
                                                opcion = 1
                                                break
                                            else:
                                                column += 1
                                                opcion = 1
                                                break
                                        elif opcion == Nivel:
                                            try:
                                                self.MatrizPrin[row][column] = 0
                                                row = listajugadas[-1][0]
                                                column = listajugadas [-1][1]
                                                opcion = listajugadas [-1][2]+1
                                                del listajugadas [-1]
                                                break
                                            except:
                                                self.MatrizPrin[row][column] = 0
                                                row = 0
                                                column = 0
                                                opcion = 1
                                                del listajugadas [-1]
                                                break
                                        else:
                                            opcion += 1
                                            break
                                    elif sig == "x":
                                        resultado = 1
                                        for n in range (len(listadenumeros)):
                                            resultado *= listadenumeros[n]   
                                        if resultado == numsig:
                                            listajugadas.append([row,column,opcion])
                                            if column == Nivel - 1:
                                                row += 1
                                                column = 0
                                                opcion = 1
                                                break
                                            else:
                                                column += 1
                                                opcion = 1
                                                break
                                        elif opcion == Nivel:
                                            try:
                                                self.MatrizPrin[row][column] = 0
                                                row = listajugadas[-1][0]
                                                column = listajugadas [-1][1]
                                                opcion = listajugadas [-1][2]+1
                                                del listajugadas [-1]
                                                break
                                            except:
                                                self.MatrizPrin[row][column] = 0
                                                row = 0
                                                column = 0
                                                opcion = 1
                                                del listajugadas [-1]
                                                break
                                        else:
                                            opcion += 1
                                            break
                                    elif sig == "/":
                                        listadenumeros.sort(reverse = True)
                                        resultado = listadenumeros.pop(0)
                                        for n in range (len(listadenumeros)):
                                            resultado /= listadenumeros[n]    
                                        if resultado == numsig:
                                            listajugadas.append([row,column,opcion])
                                            if column == Nivel - 1:
                                                row += 1
                                                column = 0
                                                opcion = 1
                                                break
                                            else:
                                                column += 1
                                                opcion = 1
                                                break
                                        elif opcion == Nivel:
                                            try:
                                                self.MatrizPrin[row][column] = 0
                                                row = listajugadas[-1][0]
                                                column = listajugadas [-1][1]
                                                opcion = listajugadas [-1][2]+1
                                                del listajugadas [-1]
                                                break
                                            except:
                                                self.MatrizPrin[row][column] = 0
                                                row = 0
                                                column = 0
                                                opcion = 1
                                                del listajugadas [-1]
                                                break
                                        else:
                                            opcion += 1
                                            break
                        if Vali == True:
                            break
                else:
                    opcion += 1
                    break
            if Nivel == row:
                break
        self.CreaMatrizBot()    
        self.BotDeact()
        if multinivel == False:
            otrojuego = messagebox.askyesno("Solucion", "Desea jugar otra partida?")
            if otrojuego == True:
                self.BotDeact()
                self.OtroJuego()
            else:
                self.BotDeact()
                self.Vjugar.destroy()
        else:
            Nivel += 1
            if Nivel == 10:
                otrojuego = messagebox.askyesno("Solucion", "Has ganado!, desea jugar otra vez?")
                if otrojuego == True:
                    self.BotDeact()
                    self.OtroJuego()
                else:
                    self.BotDeact()
                    self.Vjugar.destroy()
            else:
                self.BotDeact()
                otrojuego = messagebox.askyesno("Solucion", "Desea seguir jugando?")
                if otrojuego == True:
                    self.iniciarkenken()
                else:
                    self.BotDeact()
                    self.Vjugar.destroy()
                
                                    
    def Pista (self):
        global Mx
        global My
        global varsis
        varsis = StringVar()
        listaprin = []
        self.VPista = Toplevel()
        LabelConfig = Label (self.VPista, text = "Jugadas",pady = "5", fg= "Dark Blue", font = "Times 35").pack()
        self.jugadas = list(self.diccionario.values())
        for x in range (len(self.jugadas)):
            for y in range (1,len(self.jugadas[x])):
                if self.jugadas[x][y] == (Mx+1,My+1):
                    for q in range (1,Nivel+1):
                        listaprin.append(q)
                    num = self.jugadas[x][0]
                    sig = self.jugadas[x][0][-1]
                    numsig = int( num.replace(sig, ""))
                    listadenumeros = [list(k) for k in itertools.permutations(listaprin,len(self.jugadas[x])-1)]
                    print (listadenumeros)
                    if sig == "+":
                        for n in range (len(listadenumeros)):
                            resultado = 0
                            for w in range (len(listadenumeros[n])):
                                resultado += listadenumeros[n][w]    
                            if resultado == numsig:
                                varsis.set(listadenumeros[x])
                                Rjugada = Radiobutton(self.VPista, text=str(listadenumeros[n]),command = self.Poner,  variable=varsis, value=listadenumeros[n])
                                Rjugada.pack()
                    elif sig == "-":
                        for n in range (len(listadenumeros)):
                            copylista = listadenumeros[n]
                            copylista.sort(reverse = True)
                            resultado = copylista[0]
                            for w in range (1,len(copylista)):
                                resultado -= copylista[w] 
                            if resultado == numsig:
                                varsis.set(listadenumeros[n])
                                Rjugada = Radiobutton(self.VPista, text=str(listadenumeros[n]),command = self.Poner,  variable=varsis, value=listadenumeros[n])
                                Rjugada.pack()
                    elif sig == "x":
                        for n in range (len(listadenumeros)):
                            resultado = 1
                            for w in range (len(listadenumeros[n])):
                                resultado *= listadenumeros[n][w]   
                            if resultado == numsig:
                                varsis.set(listadenumeros[n])
                                Rjugada = Radiobutton(self.VPista, text=str(listadenumeros[n]),command = self.Poner,  variable=varsis, value=listadenumeros[n])
                                Rjugada.pack()
                    elif sig == "/":                       
                        for n in range (len(listadenumeros)):
                            copylista = listadenumeros[n]
                            copylista.sort(reverse = True)
                            resultado = copylista[0]
                            for w in range (1,len(copylista)):
                                resultado /= copylista[w]                                
                            if resultado == numsig:
                                varsis.set(listadenumeros[n])
                                Rjugada = Radiobutton(self.VPista, text=str(listadenumeros[n]),command = self.Poner, variable=varsis, value=listadenumeros[n])
                                Rjugada.pack()
                        
                        
                    
    def Poner (self):
        global varsis
        self.vari = varsis.get()
        self.vari=self.vari.replace(" ", "")
        self.vari = list(self.vari)
        print(self.vari)
        self.jugadas = list(self.diccionario.values())
        for x in range (len(self.jugadas)):
            for y in range (1,len(self.jugadas[x])):
                if self.jugadas[x][y] == (Mx+1,My+1):
                    for w in range (1, len(self.jugadas[x])):
                        self.MatrizPrin[self.jugadas[x][w][0]-1][self.jugadas[x][w][1]-1] = self.vari[w-1]
                    self.CreaMatrizBot()
                    self.VPista.destroy()
                                                                                                   
        

class Configurar:
    def __init__(self):
        VentanaPrincipal.iconify()
        self.Vconfigurar = Toplevel()
        self.Vconfigurar.title("CONFIGURAR")
        LabelConfig = Label (self.Vconfigurar, text = "Configurar",pady = "5", fg= "Dark Blue", font = "Times 60").pack()
        BNivel = Button (self.Vconfigurar, command = self.Nivel, bg="Purple", activebackground = "Light blue", relief = "groove",text = "NIVEL",width = "20", font = "Times 20").pack()
        BReloj = Button (self.Vconfigurar,command = self.Tiempo, bg="Orange", activebackground = "Pink", relief = "groove",text = "RELOJ",width = "20", font = "Times 20").pack()
        BPospan = Button (self.Vconfigurar, bg="Brown", activebackground = "Grey", relief = "groove",text = "POS. DEL PANEL",width = "20", font = "Times 20").pack()
        BSonido = Button (self.Vconfigurar,command = self.Sonido, bg="Yellow", activebackground = "Light Yellow", relief = "groove",text = "SONIDO",width = "20", font = "Times 20").pack()
        BMultinivel = Button (self.Vconfigurar,command = self.Multinivel, bg="Turquoise", activebackground = "Light Yellow", relief = "groove",text = "MULTINIVEL",width = "20", font = "Times 20").pack()
        BOk = Button (self.Vconfigurar, bg="Green", command = self.Configsalir, activebackground = "Light Green", relief = "groove",text = "Ok",width = "20", font = "Times 20").pack()

    def Configsalir (self):
        VentanaPrincipal.deiconify()
        self.Vconfigurar.destroy()

    def Multinivel (self):
        self.Vconfigurar.iconify()
        self.VconfigurarM = Toplevel()
        self.VconfigurarM.title("Multinivel")
        self.varsi = IntVar()
        LabelConfig = Label (self.VconfigurarM, text = "MULTINIVEL",pady = "5", fg= "Dark Blue", font = "Times 60").pack()
        R3x3 = Radiobutton(self.VconfigurarM, text="Activar", variable=self.varsi, value=True).pack()
        R4x4 = Radiobutton(self.VconfigurarM, text="Desactivar", variable=self.varsi, value=False).pack()
        BJugar = Button (self.VconfigurarM, bg="Green",command = self.AceptarM,pady = "3", activebackground = "Light Green", relief = "groove",text = "Aceptar",width = "20", font = "Times 20").pack()

    def AceptarM (self):
        global multinivel
        multinivel = self.varsi.get()
        self.VconfigurarM.destroy()
            
    
    def Sonido (self):
        global sonido
        self.Vconfigurar.iconify()
        self.VconfigurarN = Toplevel()
        self.VconfigurarN.title("Sonido")
        self.vars = IntVar()
        LabelConfig = Label (self.VconfigurarN, text = "Sonido",pady = "5", fg= "Dark Blue", font = "Times 60").pack()
        R3x3 = Radiobutton(self.VconfigurarN, text="Activar Sonido", variable=self.vars, value=True).pack()
        R4x4 = Radiobutton(self.VconfigurarN, text="Desactivar Sonido", variable=self.vars, value=False).pack()
        BJugar = Button (self.VconfigurarN, bg="Green",command = self.AceptarS,pady = "3", activebackground = "Light Green", relief = "groove",text = "Aceptar",width = "20", font = "Times 20").pack()

    def AceptarS (self):
        global sonido
        sonido = self.vars.get()
        if sonido == False:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.VconfigurarN.destroy()
        self.Vconfigurar.deiconify()
        
    def Tiempo (self):
        self.VTiempo = Toplevel()
        self.VTiempo.title("Tiempo")
        self.vartim = StringVar()
        LabelConfig = Label (self.VTiempo, text = "RELOJ",pady = "5", fg= "Dark Blue", font = "Times 60").pack()
        self.RReloj = Radiobutton(self.VTiempo, text="Activado", variable=self.vartim, value=False).pack()
        self.RTimer = Radiobutton(self.VTiempo, text="Timer", variable=self.vartim, value=True).pack()
        BOk = Button (self.VTiempo, bg="Green", command = self.timerok, activebackground = "Light Green", relief = "groove",text = "Ok",width = "20", font = "Times 20").pack()

    def timerok (self):
        global Timer
        Timer = self.vartim.get()
        self.VTiempo.destroy()
        
        

    def Nivel (self):
        self.Vconfigurar.iconify()
        self.VconfigurarN = Toplevel()
        self.VconfigurarN.title("Nivel")
        self.var = IntVar()
        R3x3 = Radiobutton(self.VconfigurarN, text="3x3", variable=self.var, value=3).pack(side = LEFT)
        R4x4 = Radiobutton(self.VconfigurarN, text="4x4", variable=self.var, value=4).pack(side=LEFT)
        R5x5 = Radiobutton(self.VconfigurarN, text="5x5", variable=self.var, value=5).pack(side = LEFT)
        R6x6 = Radiobutton(self.VconfigurarN, text="6x6", variable=self.var, value=6).pack(side=LEFT)
        R7x7 = Radiobutton(self.VconfigurarN, text="7x7", variable=self.var, value=7).pack(side = LEFT)
        R8x8 = Radiobutton(self.VconfigurarN, text="8x8", variable=self.var, value=8).pack(side=LEFT)
        R9x9 = Radiobutton(self.VconfigurarN, text="9x9", variable=self.var, value=9).pack(side = LEFT)
        BJugar = Button (self.VconfigurarN, bg="Green",command = self.Aceptar,pady = "3", activebackground = "Light Green", relief = "groove",text = "Aceptar",width = "20", font = "Times 20").pack()

    def Aceptar (self):
        global Nivel
        Nivel = self.var.get()
        if Nivel == 0:
            Nivel=6
        self.VconfigurarN.destroy()
        self.Vconfigurar.deiconify()

class Ayuda ():
    def __init__ (self):
        VentanaPrincipal.iconify()
        self.VAyuda = Toplevel()
        self.VAyuda.title("Ayuda")
        BAyuda = Button (self.VAyuda,command = os.startfile("Manual_de_Usuario.pdf"), bg="Green",pady = "3", activebackground = "Light Green", relief = "groove",text = "Ayuda",width = "27", font = "Times 20").pack()
        BAcercade = Button (self.VAyuda, command = self.Acercade, bg="Dark Blue",pady = "3", activebackground = "Light Blue", relief = "groove",text = "Acerca de",width = "27", font = "Times 20").pack()
        BSalir = Button (self.VAyuda, bg="Red",pady = "3", command = self.Salir, activebackground = "Pink", relief = "groove",text = "SALIR",width = "27", font = "Times 20").pack()

    def Acercade (self):
        self.VAcercade = Toplevel()
        self.VAcercade.title ("Acerca de")
        Labelnomap = Label (self.VAcercade, text = "KENKEN",pady = "5", fg= "Dark Blue", font = "Times 60").pack()
        Labelfunc = Label (self.VAcercade, text = "Generador de Juegos de Kenken",pady = "5", fg= "Dark Blue", font = "Times 20").pack()
        Labelaut = Label (self.VAcercade, text = "Fabian Campos González",pady = "5", fg= "Dark Blue", font = "Times 20").pack()
        Labelfech = Label (self.VAcercade, text = "2015",pady = "5", fg= "Dark Blue", font = "Times 20").pack()
        BJugar = Button (self.VAcercade, bg="Green",command = self.VAcercade.destroy,pady = "3", activebackground = "Light Green", relief = "groove",text = "Aceptar",width = "20", font = "Times 20").pack()
        

    def Salir (self):
        VentanaPrincipal.deiconify()
        self.VAyuda.destroy()
    
def doge ():
    Vdoge = Toplevel()
    Vdoge.title("DOGE")
    image = Image.open("doge.jpeg")
    photo = ImageTk.PhotoImage(image)
    label = Label(Vdoge,image=photo)
    label.image = photo 
    label.pack() 
#Funcion de musica 
def MusicaFondo ():
    global sonido
    if sonido == True:
        pygame.mixer.init()
        pygame.mixer.music.load("Professor Layton OST - All Puzzle Themes.mp3")
        pygame.mixer.music.play()
    else:
        pass

#Programa fuente    
VentanaPrincipal = Tk()
VentanaPrincipal.title("KENKEN")
MusicaFondo()
LabelPrin = Label(VentanaPrincipal, text = "KENKEN",pady = "5", fg= "Purple", font = "Times 80").pack()
BJugar = Button (VentanaPrincipal, bg="Green",command = Jugar,pady = "3", activebackground = "Light Green", relief = "groove",text = "JUGAR",width = "27", font = "Times 20").pack()
BConfigurar = Button (VentanaPrincipal, bg="Dark Blue",command = Configurar,pady = "3", activebackground = "Light Blue", relief = "groove",text = "CONFIGURAR",width = "27", font = "Times 20").pack()
BFuncionalidad = Button (VentanaPrincipal,pady = "3",command = doge, bg="Yellow", activebackground = "Light Yellow", relief = "groove",text = "YOU WIN $1 000 000 CLICK IT",width = "27", font = "Times 20").pack()
BAyuda = Button (VentanaPrincipal, bg="Orange",command = Ayuda,pady = "3", activebackground = "Pink", relief = "groove",text = "AYUDA",width = "27", font = "Times 20").pack()
BSalir = Button (VentanaPrincipal, bg="Red",pady = "3", command = VentanaPrincipal.destroy, activebackground = "Pink", relief = "groove",text = "SALIR",width = "27", font = "Times 20").pack()
VentanaPrincipal.mainloop
