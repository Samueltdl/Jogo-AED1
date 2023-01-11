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

lista_inimigos=[]
lista_tiros=[]
cont=0
seg=0
ms=0
parametro=60

inimigos_mortos = 0

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
        inimigo = gf.Rectangle(gf.Point(X, -20), gf.Point(X + 40, 20))
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
        #print(tiro.getP1())
        
    for elem in lista_tiros:
        elem.move(0,-10)
        #print(tiro.getP1())
        if elem.getCenter().getY()== -20:
            elem.undraw()
            lista_tiros.remove(elem)

    for elem in lista_tiros:
        for a in lista_inimigos:
            if elem.getP1().getY() <= a.getP2().getY():
                if a.getP1().getX() <= elem.getP1().getX() <= a.getP2().getX():
                    print('aaaaaaaaaaaaa')
                    elem.undraw()
                    lista_tiros.remove(elem)
                    a.undraw()
                    lista_inimigos.remove(a)
                    inimigos_mortos += 1
    
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