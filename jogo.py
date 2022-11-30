import graphics as gf
from time import sleep

win = gf.GraphWin('navezinha piu piu', 700, 800, autoflush=False)



def nave():   
    nave = gf.Image(gf.Point(350, 500), 'img/nave.png')
    return nave

x = nave()
x.draw(win)

while True:
    direcao = win.getKey()
    if direcao == 'a':
        x.move(-15, 0)
    
    dif direcao == 'd':
        x.move(15, 0)




win.getMouse()
win.close()