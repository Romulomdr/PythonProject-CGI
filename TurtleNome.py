from tkinter import*
import turtle
import time
screen = turtle.Screen()
screen.bgcolor("dark grey")
screen.title("Turtle")
janela = Tk()
janela.geometry("200x300+100+100")
janela.title("Comandos")

pincel = turtle.Turtle()

def limpar():
    pincel.clear()
    pincel.reset()

limpar1 = Button(janela, text='Limpar',font='bold', command= limpar ,bd=3,bg='#FFA500')
limpar1.place(x=20,y=190)

def primeiroNome ():
    pincel.right(90)
    pincel.forward(150)
    pincel.left(180)
    pincel.forward(150)
    pincel.forward(150)
    pincel.right(45)
    pincel.forward(150)
    pincel.right(45)
    pincel.forward(150)
    pincel.right(45)
    pincel.forward(150)
    pincel.right(90)
    pincel.forward(150)
    pincel.right(45)
    pincel.forward(150)
    pincel.left(135)
    pincel.forward(150)
    pincel.forward(150)
    limpar1.configure(bg='#ff0000')
    pincel.left(180)
    limpar1.configure(bg='#FFA500')

def segundoNome():
    pincel.right(90)
    pincel.forward(150)
    pincel.left(180)
    pincel.forward(150)
    pincel.forward(150)
    pincel.right(157.5)                 #90 dividido em 4 partes deu 22.5
    pincel.forward(150) 
    pincel.forward(170)
    pincel.left(135)
    pincel.forward(150)
    pincel.forward(170)
    pincel.right(157.5)
    pincel.forward(150)
    pincel.forward(150)
    limpar1.configure(bg='#ff0000')
    pincel.left(180)
    limpar1.configure(bg='#FFA500')

def terceiroNome ():
    pincel.right(180)
    pincel.forward(75)
    pincel.left(180)
    pincel.forward(75)
    pincel.forward(75)
    pincel.left(45)
    pincel.forward(75)
    pincel.left(45)
    pincel.forward(75)
    pincel.left(45)
    pincel.forward(75)
    pincel.left(45)
    pincel.forward(75)
    pincel.forward(75)
    pincel.right(45)
    pincel.forward(75)
    pincel.right(45)
    pincel.forward(75)
    pincel.right(45)
    pincel.forward(75)
    pincel.right(45)
    pincel.forward(75)
    pincel.forward(75)
    limpar1.configure(bg='#ff0000')
    pincel.left(180)
    limpar1.configure(bg='#FFA500')




def quartoNome():
    pincel.forward(75)
    pincel.forward(75)
    pincel.left(45)
    pincel.forward(75)
    pincel.left(45)
    pincel.forward(75)
    pincel.forward(75)
    pincel.left(45)
    pincel.forward(75)
    pincel.left(45)
    pincel.forward(75)
    pincel.forward(75)
    pincel.left(90)
    pincel.forward(260)
    limpar1.configure(bg='#ff0000')
    pincel.left(180)
    limpar1.configure(bg='#FFA500')

enviar = Button(janela, text='Primeiro Nome',font='bold', command= primeiroNome ,bd=3,bg='#FFA500')
enviar.place(x=20,y=30)

enviar2 = Button(janela, text='Segundo Nome',font='bold', command= segundoNome ,bd=3,bg='#FFA500')
enviar2.place(x=20,y=70)

enviar3 = Button(janela, text='Terceiro Nome',font='bold', command= terceiroNome ,bd=3,bg='#FFA500')
enviar3.place(x=20,y=110)

enviar4 = Button(janela, text='Quarto Nome',font='bold', command= quartoNome ,bd=3,bg='#FFA500')
enviar4.place(x=20,y=150)





janela.mainloop()
screen.mainloop()
