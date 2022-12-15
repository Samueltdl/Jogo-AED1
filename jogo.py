import graphics as gf
from time import sleep
import random

win = gf.GraphWin('navezinha piu piu', 700, 800, autoflush=False)

background = gf.Image(gf.Point(350, 400), 'img/background.png')
background.draw(win)

nave = gf.Image(gf.Point(350, 745), 'img/nave.png')
hitbox= gf.Circle(gf.Point(350, 750), 40)
nave.draw(win)
hitbox.draw(win)
def atira(point):
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
        print(inimigo.getCenter())





while True:
    #geraInimigo() Aqui, gera o inimigo... porém essa geração de inimigo para todo o programa.
    x = gf.Point(50, 750)
    direcao = win.checkKey()
    if direcao == 'a':
        if hitbox.getCenter() == x:
            print('foiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
            pass
        hitbox.move(-5,0)
        nave.move(-5, 0)
    if direcao == 'd':
        hitbox.move(5,0)
        nave.move(5, 0)
    if win.checkMouse():
        atira(hitbox.getCenter().getX())
        


    

    #print(hitbox.getP2())
    #print(tiro.getP2())
    #print(tiro.getCenter())




win.getMouse()
win.close()