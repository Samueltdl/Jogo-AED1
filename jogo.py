import graphics as gf
from time import sleep

win = gf.GraphWin('navezinha piu piu', 700, 800, autoflush=False)

background = gf.Image(gf.Point(350, 400), 'img/background.png')
background.draw(win)

nave = gf.Image(gf.Point(350, 745), 'img/nave.png')
hitbox= gf.Circle(gf.Point(350, 750), 40)
nave.draw(win)
hitbox.draw(win)

while True:
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


    print(hitbox.getCenter())




win.getMouse()
win.close()