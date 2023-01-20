import graphics as gf
import random
win = gf.GraphWin('navezinha piu piu', 700, 800, autoflush=False)
lista_inimigos=[]
X = random.randint(5,680)
inimigo = gf.Rectangle(gf.Point(X, 200), gf.Point(X + 40, 240)) # CRIA INIMIGOS DE ACORDO COM O TEMPO, E OS ADICIONA NA LISTA DE INIMIGOS
inimigo.setOutline('red')
alien = gf.Image(gf.Point(X, -20), 'img/alien1.png')
alien.draw(win)
#lista_alien.append(alien)
lista_inimigos.append(inimigo)
inimigo.draw(win)
for elem in lista_inimigos:
    print(lista_inimigos.index(elem))

win.getKey()