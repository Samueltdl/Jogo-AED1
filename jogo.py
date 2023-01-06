import graphics as gf
from time import sleep
import random

win = gf.GraphWin('navezinha piu piu', 700, 800, autoflush=False)

background = gf.Image(gf.Point(350, 400), 'img/background.png')
nave = gf.Image(gf.Point(350, 745), 'img/nave.png')
hitbox= gf.Circle(gf.Point(350, 750), 40)
hitbox.setOutline('black')
pontuacao= gf.Text(gf.Point(55,20), "Pontuação:")
pontuacao.setTextColor('white')
pontuacao.setSize(15)


background.draw(win)
pontuacao.draw(win)
hitbox.draw(win)
nave.draw(win)

'''def atira(point):
    print('foi')
    cont=0
    while cont<72:
        tiro = gf.Rectangle(gf.Point(point, 700-cont*10), gf.Point(point,720-cont*10))
        tiro.setOutline('red')
        tiro.draw(win)
        gf.update(3000)
        tiro.undraw()
        cont+=1
        print(tiro.getCenter())

def geraInimigo():
    X= random.randint(0,690)
    cont=0
    while cont<169:
        inimigo = gf.Circle(gf.Point(X, -20+cont*5), 20)
        inimigo.setOutline('red')
        inimigo.setFill('red')
        inimigo.draw(win)
        gf.update(30)
        inimigo.undraw()
        cont+=1
        print(inimigo.getCenter())'''

lista_inimigos=[]
lista_tiros=[]
cont=0
seg=0
ms=0
parametro=60

while True:
    temporizador=gf.Text(gf.Point(50,50), str(seg))
    temporizador.setSize(15)
    temporizador.setTextColor('white')
    temporizador.draw(win)
    if ms==parametro:
        parametro+=60
        seg+=1
        print(seg)
    if cont ==200:
        X= random.randint(5,680)
        inimigo = gf.Circle(gf.Point(X,-20), 20)
        inimigo.setOutline('red')
        inimigo.setFill('red')
        lista_inimigos.append(inimigo)
        inimigo.draw(win)
        cont=0
    
    for elem in lista_inimigos:
        elem.move(0,1)
        if elem.getCenter().getY()== 820:
            elem.undraw()
            lista_inimigos.remove(elem)
        
    #bordaesq = gf.Point(50, 750)
    direcao = win.checkKey()
    if direcao == 'a':
        hitbox.move(-5,0)
        nave.move(-5, 0)
    if direcao == 'd':
        hitbox.move(5,0)
        nave.move(5, 0)
    if win.checkMouse():
        tiro = gf.Rectangle(gf.Point(hitbox.getCenter().getX(), 700), gf.Point(hitbox.getCenter().getX(),720))
        tiro.setOutline('red')
        lista_tiros.append(tiro)
        tiro.draw(win)
    for elem in lista_tiros:
        elem.move(0,-10)

    cont+=1
    ms+=1
    gf.update(65)
    temporizador.undraw()
        
    #print(hitbox.getP2())
    #print(tiro.getP2())
    #print(tiro.getCenter())

win.getMouse()
win.close()

'''Proximos passos:
1- Aumentar a dificuldade conforme o contador de pontuação
2- Estabelecer a colisão dos objetos.
3- Melhorar a estética do game.
4- Talvez implementar um menu.
'''