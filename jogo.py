import graphics as gf
from time import sleep

win = gf.GraphWin('navezinha piu piu', 700, 800, autoflush=False)

background = gf.Image(gf.Point(350, 400), 'img/background.png')
background.draw(win)

nave = gf.Image(gf.Point(350, 750), 'img/nave.png')
nave.draw(win)

while True:
    direcao = win.checkKey()
    lado= win.checkKey()
    if direcao == 'a':
        nave.move(-5, 0)
    if direcao == 'd':
        nave.move(5, 0)
    if lado == 'a':
        nave.move(-5,0)
    if lado == 'd':
        nave.move(5,0)



win.getMouse()
win.close()