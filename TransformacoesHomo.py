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
homogenea = np.array([1,1,1,1,1])           #criando coordenadas homogeneas 
matrizIdentidade = [[1,0,0],[0,1,0],[0,0,1]] # matriz identidade para facilitar o uso das coordenadas homogeneas
matrizObjeto =np.full((3,5), 0)             #criando uma matriz para a forma geometrica


for i in range(5):                          # preenchendo a matriz da forma geometrica
    matrizObjeto[0][i] = xpoints[i]
for i in range(5):
    matrizObjeto[1][i] = ypoints[i]
for i in range(5):
    matrizObjeto[2][i] = homogenea[i]


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
    matrizIdentidade = [[1,0,0],[0,1,0],[0,0,1]] #resetando a matrizIdentidade para que não fique salvo os resultados usados nos metodos anteriores
    # Pontos
    xpoints = np.array([1,4,4,1,1])
    ypoints = np.array([1,1,4,4,1])
    plot1 = fig.add_subplot(111)
    plot1.plot(xpoints,ypoints)      #metodo para plotar o grafico depois de aplicar os valores no array 
    matrizObjeto.fill(0)
    for i in range(5):                          # preenchendo a matriz do objeto
        matrizObjeto[0][i] = xpoints[i]
    for i in range(5):
        matrizObjeto[1][i] = ypoints[i]
    for i in range(5):
        matrizObjeto[2][i] = homogenea[i]

   
    plot1.axis([0,10,0,10])
        
   
    fig.canvas.draw()                   #atualizar grafico
    fig.canvas.flush_events()
    
def escalar():                              #Metodo para escalar o objeto fazendo multiplicação de array
    matrizIdentidade = [[1,0,0],[0,1,0],[0,0,1]]
    fig.clf()
    result=0
    Sx =2           #valores para alterar o escalonamento
    Sy =2
    k = 0
    j = 0
    matrizIdentidade[0][0] = Sx  #posicionando os valores do escalonamento na matriz Identidade
    matrizIdentidade[1][1] = Sy
    # Pontos
    xpoints = np.array([1,4,4,1,1])
    ypoints = np.array([1,1,4,4,1])

    plot1 = fig.add_subplot(111)  
    plot1.plot(xpoints,ypoints)

    for i in range(15):         #laço para efetuar a aplicação do escalonamento e salvar os valores obtidos no vetor X e depois no vetor Y para plotar

        if k == 3:
            xpoints[j] = result
            k=0
            j+=1
            result=0
        result = (matrizIdentidade[0][k]*matrizObjeto[k][j])+result
        if i == 14:
            xpoints[4] = result
        k += 1
    result = 0
    k = 0
    j = 0
    for i in range(15):

        if k == 3:
            ypoints[j] = result
            k=0
            j+=1
            result=0
        result = (matrizIdentidade[1][k]*matrizObjeto[k][j])+result
        if i == 14:
            ypoints[4] = result
        k += 1


       
    plot1.axis([0,10,0,10])
    plot1.plot(xpoints,ypoints) 
 
    fig.canvas.draw()
    fig.canvas.flush_events()

def translacao():                       # Metodo para fazer a translação da forma na diagonal superior direita fazendo a soma dos arrays 
   
    matrizIdentidade = [[1,0,0],[0,1,0],[0,0,1]]  #metodo para resetar a matriz identidade
    fig.clf()

    result=0
    tx =3
    ty =3
    matrizIdentidade[0][2] = tx 
    matrizIdentidade[1][2] = ty
    
    # Pontos
    xpoints = np.array([1,4,4,1,1])
    ypoints = np.array([1,1,4,4,1])
    k = 0
    j = 0
    
    plot1 = fig.add_subplot(111)  
    plot1.axis([0,10,0,10])
    plot1.plot(xpoints,ypoints)
    for i in range(15):

        if k == 3:
            xpoints[j] = result
            k=0
            j+=1
            result=0
        result = (matrizIdentidade[0][k]*matrizObjeto[k][j])+result
        if i == 14:
            xpoints[4] = result
        k += 1
    result = 0
    k = 0
    j = 0
    for i in range(15):

        if k == 3:
            ypoints[j] = result
            k=0
            j+=1
            result=0
        result = (matrizIdentidade[1][k]*matrizObjeto[k][j])+result
        if i == 14:
            ypoints[4] = result
        k += 1

    
    plot1.plot(xpoints,ypoints)
    fig.canvas.draw()
    fig.canvas.flush_events()
    
def reflexao():                 #Metodo para fazer a reflexão da forma invertendo os sinais do eixo X
    matrizIdentidade = [[1,0,0],[0,1,0],[0,0,1]]   
    fig.clf()
    result=0
    Rx =-1          # -1 significa que vou fazer a reflexão em relação ao eixo X 
    Ry =1
    matrizIdentidade[0][0] = Rx
    matrizIdentidade[1][1] = Ry
    # Pontos
    xpoints = np.array([1,4,4,1,1])
    ypoints = np.array([1,1,4,4,1])

    plot1 = fig.add_subplot(111)  
    plot1.plot(xpoints,ypoints)

    k = 0
    j = 0
      

    for i in range(15):

        if k == 3:
            xpoints[j] = result
            k=0
            j+=1
            result=0
        result = (matrizIdentidade[0][k]*matrizObjeto[k][j])+result     #
        if i == 14:
            xpoints[4] = result
        k += 1
    result = 0
    k = 0
    j = 0
    for i in range(15):

        if k == 3:
            ypoints[j] = result
            k=0
            j+=1
            result=0
        result = (matrizIdentidade[1][k]*matrizObjeto[k][j])+result
        if i == 14:
            ypoints[4] = result
        k += 1

    plot1.axis([-5,10,-5,10])
    plot1.plot(xpoints,ypoints)

    fig.canvas.draw()
    fig.canvas.flush_events()

def rotacao():              #Metodo para fazer a rotação da forma de acordo com a formula passada em sala de aula 
    matrizIdentidade = [[1,0,0],[0,1,0],[0,0,1]]
    fig.clf()
    ang = 30                            #Angulo definido foi 30 Graus               
    seno = math.sin(math.radians(ang))  #encontrando o valor do seno de 10 graus 
    cos = math.cos(math.radians(ang))   #encontrando o valor do Cosseno de 10 graus
    result=0
    matrizIdentidade[0][0] = cos
    matrizIdentidade[0][1] = seno*-1
    matrizIdentidade[1][0] = seno
    matrizIdentidade[1][1] = cos
    # Pontos
    xpoints = np.array([1,4,4,1,1])
    ypoints = np.array([1,1,4,4,1])
    plot1 = fig.add_subplot(111)   
    plot1.axis([-2,10,-2,10])
    plot1.plot(xpoints,ypoints)

    k = 0
    j = 0


    for i in range(15):

        if k == 3:
            xpoints[j] = result
            k=0
            j+=1
            result=0
        result = (matrizIdentidade[0][k]*matrizObjeto[k][j])+result
        if i == 14:
            xpoints[4] = result
        k += 1
    result = 0
    k = 0
    j = 0
    for i in range(15):

        if k == 3:
            ypoints[j] = result
            k=0
            j+=1
            result=0
        result = (matrizIdentidade[1][k]*matrizObjeto[k][j])+result
        if i == 14:
            ypoints[4] = result
        k += 1

    plot1.plot(xpoints,ypoints)

    fig.canvas.draw()
    fig.canvas.flush_events() 

def cisalhamento():                 #Metodo pra fazer o cisalhamento de acordo com a formula passada em sala de aula no eixo X 
    matrizIdentidade = [[1,0,0],[0,1,0],[0,0,1]]    
    fig.clf()
    Chx = 1     # Aplicando o cisalhamento no eixo X
    result=0
    matrizIdentidade[0][1] = Chx        
    # Pontos
    xpoints = np.array([1,4,4,1,1])
    ypoints = np.array([1,1,4,4,1])
    plot1 = fig.add_subplot(111)                
    plot1.axis([-1,10,0,10])
    plot1.plot(xpoints,ypoints)
    k = 0
    j = 0


    for i in range(15):

        if k == 3:
            xpoints[j] = result
            k=0
            j+=1
            result=0
        result = (matrizIdentidade[0][k]*matrizObjeto[k][j])+result
        if i == 14:
            xpoints[4] = result
        k += 1
    result = 0
    k = 0
    j = 0
    for i in range(15):

        if k == 3:
            ypoints[j] = result
            k=0
            j+=1
            result=0
        result = (matrizIdentidade[1][k]*matrizObjeto[k][j])+result
        if i == 14:
            ypoints[4] = result
        k += 1

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