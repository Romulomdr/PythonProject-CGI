import matplotlib.pyplot as plt
import numpy as np
from tkinter import*
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import math
                        # importando Bibliotecas para calculos matematicos, Plotar o grafico e tkinter para configurar uma janela e botões


tela = Tk() 
tela.title('Plotando no Tkinter') 
tela.geometry("800x800") 
    
    
fig = Figure(figsize = (8, 8),              #para aumentar ou diminuir o tamanho do da figura no tkinter
             dpi = 100) 

xpoints = np.array([1,4,4,1,1])         #criando um array e preenchendo com as coordenadas
ypoints = np.array([1,1,4,4,1]) 
plot1 = fig.add_subplot(111)            #configurando o plot antes de exibi-lo
plot1.plot(xpoints,ypoints) 
plot1.axis([0,10,0,10])
canvas = FigureCanvasTkAgg(fig, 
                           master = tela)
canvas.draw() 
canvas.get_tk_widget().pack()                #mostrando no tkinter as ferramentas do matplotlib
toolbar = NavigationToolbar2Tk(canvas, 
                                tela) 
toolbar.update() 
canvas.get_tk_widget().pack()          

def original():                             #Metodo para voltar para o grafico original
    fig.clf()
    
    # Pontos
    xpoints = np.array([1,4,4,1,1])
    ypoints = np.array([1,1,4,4,1])
    homegenea = np.array([1,1,1,1,1])

    plot1 = fig.add_subplot(111)
    plot1.axis([0,10,0,10])
    plot1.plot(xpoints,ypoints)        
   
    fig.canvas.draw()                   #atualizar grafico
    fig.canvas.flush_events()
    
def escalar():                              #Metodo para escalar o objeto fazendo multiplicação de array

    fig.clf()

    # Pontos
    xpoints = np.array([1,4,4,1,1])
    ypoints = np.array([1,1,4,4,1])

    plot1 = fig.add_subplot(111)  
    plot1.plot(xpoints,ypoints)
    xpoints = np.array([1,4,4,1,1])*2
    ypoints = np.array([1,1,4,4,1])*2
    plot1.axis([0,10,0,10])
    plot1.plot(xpoints,ypoints)         #metodo para plotar o grafico depois de aplicar os valores no array 
    
    fig.canvas.draw()
    fig.canvas.flush_events()

def translacao():                       # Metodo para fazer a translação da forma na diagonal superior direita fazendo a soma dos arrays 

    fig.clf()

    # Pontos
    xpoints = np.array([1,4,4,1,1])
    ypoints = np.array([1,1,4,4,1])

    plot1 = fig.add_subplot(111)  
    plot1.plot(xpoints,ypoints)
    xpoints = np.array([1,4,4,1,1])+4       #Aplicando a transformação
    ypoints = np.array([1,1,4,4,1])+4
    plot1.axis([0,10,0,10])
    plot1.plot(xpoints,ypoints)

    fig.canvas.draw()
    fig.canvas.flush_events()
    
def reflexao():                 #Metodo para fazer a reflexão da forma invertendo os sinais do eixo X
    
    fig.clf()

    # Pontos
    xpoints = np.array([1,4,4,1,1])
    ypoints = np.array([1,1,4,4,1])

    plot1 = fig.add_subplot(111)  
    plot1.plot(xpoints,ypoints)
    xpoints = np.array([1,4,4,1,1])*-1
    ypoints = np.array([1,1,4,4,1])
    plot1.axis([-5,10,-5,10])
    plot1.plot(xpoints,ypoints)

    fig.canvas.draw()
    fig.canvas.flush_events()

def rotacao():              #Metodo para fazer a rotação da forma de acordo com a formula passada em sala de aula 

        fig.clf()

        # Pontos
        xpoints = np.array([1,4,4,1,1])
        ypoints = np.array([1,1,4,4,1])
        plot1 = fig.add_subplot(111)   
        plot1.axis([-2,10,-2,10])
        plot1.plot(xpoints,ypoints)
    

        ang = 10                            #Angulo definido foi 10 Graus               
        seno = math.sin(math.radians(ang))  #encontrando o valor do seno de 10 graus 
        cos = math.cos(math.radians(ang))   #encontrando o valor do Cosseno de 10 graus
        
        for i in range(5):              #fazendo o laço percorrer todo o array e aplicando a formula e salvando os novos valores 

            xpoints[i] = (xpoints[i]*cos) - (ypoints[i]*seno)   #Formula x.cos(0) - y.sen(0)
            ypoints[i] = (ypoints[i]*cos) + (xpoints[i]*seno)   #Formula y.cos(0) + x.sen(0)
                                            #seno 10 = 0,1736
                                            #cos 10 = 0,9848

        plot1.plot(xpoints,ypoints)

        fig.canvas.draw()
        fig.canvas.flush_events() 

def cisalhamento():                 #Metodo pra fazer o cisalhamento de acordo com a formula passada em sala de aula no eixo X 
    fig.clf()
    # Pontos
    xpoints = np.array([1,4,4,1,1])
    ypoints = np.array([1,1,4,4,1])
    plot1 = fig.add_subplot(111)                
    plot1.axis([-1,10,0,10])
    plot1.plot(xpoints,ypoints)

    #X' = x + (Kx.y)            #Formula
    #Y' = y + (Ky.x)
    Kx = 1                  #aplicando no eixo X 
    Ky = 0
    for i in range(5):

        xpoints[i] = xpoints[i] + (Kx*ypoints[i])           #aplicando os novos valores depois da transformação
        ypoints[i] = ypoints[i] + (Ky*xpoints[i])       
    
    plot1.plot(xpoints,ypoints)
   
    fig.canvas.draw()
    fig.canvas.flush_events()   

barraDeMenus = Menu(tela)                                           #Botões de menu que ficam na parte superior com seus respectivos titulos e metodos 
barraDeMenus.add_command(label="Original", command=original)
barraDeMenus.add_command(label="Escalar", command=escalar)
barraDeMenus.add_command(label="Translação", command=translacao)
barraDeMenus.add_command(label="Reflexão", command=reflexao) 
barraDeMenus.add_command(label="Rotação", command=rotacao)
barraDeMenus.add_command(label="Cisalhamento", command=cisalhamento)

tela.config(menu=barraDeMenus)
tela.mainloop()                     #metodo para manter a janela do tkinter aberta 