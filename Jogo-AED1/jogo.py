import graphics as gf
from time import sleep
import random

win = gf.GraphWin('navezinha piu piu', 700, 800, autoflush=False)

def drawEstrutura():
    background = gf.Image(gf.Point(350, 400), 'img/background.png')
    pontuacao= gf.Text(gf.Point(55,20), "Pontuação:")
    pontuacao.setTextColor('white')
    pontuacao.setSize(15)
    Abates= gf.Text(gf.Point(200,20), "Abates:")
    Abates.setTextColor('white')
    Abates.setSize(15)

    background.draw(win)
    pontuacao.draw(win)
    Abates.draw(win)

drawEstrutura()

nave = gf.Image(gf.Point(350, 745), 'img/nave.png')
hitbox= gf.Circle(gf.Point(350, 750), 40)
hitbox.setOutline('black')
hitbox.draw(win)
nave.draw(win)

lista_inimigos=[]
lista_tiros=[]
cont=0
seg=0
ms=0
parametro=60
inimigos_mortos = 0
cont_parado = 0
#print(nave.getAnchor())
direcao = ''
cont_d_parado = 0
to_em_d = False
loop_d = False
cont_a_parado = 0
to_em_a = False
loop_a = False 



while True:

    #------------------- TEMPORIZADOR E CONTADOR DE ABATES --------------------------------

    temporizador=gf.Text(gf.Point(50,50), str(seg))
    temporizador.setSize(15)
    temporizador.setTextColor('white')
    temporizador.draw(win)
    contAbates=gf.Text(gf.Point(200,50), str(inimigos_mortos))
    contAbates.setSize(15)
    contAbates.setTextColor('white')
    contAbates.draw(win)
    if ms==parametro:
        parametro+=60
        seg+=1
        print(seg)
    if cont ==100:
        X= random.randint(5,680)
        inimigo = gf.Rectangle(gf.Point(X, -20), gf.Point(X + 40, 20)) # CRIA INIMIGOS DE ACORDO COM O TEMPO, E OS ADICIONA NA LISTA DE INIMIGOS
        inimigo.setOutline('red')
        inimigo.setFill('red')
        lista_inimigos.append(inimigo)
        inimigo.draw(win)
        cont=0
    
    for elem in lista_inimigos:
        elem.move(0,1)
        if elem.getCenter().getY()== 820: # MOVE OS INIMIGOS E TAMBÉM OS ELIMINA EM CASO DE PASSAR DA TELA
            elem.undraw()
            lista_inimigos.remove(elem)
        
    #bordaesq = gf.Point(50, 750)

    #----------------------- MOVIMENTAÇÃO DA NAVE -----------------------------------

    teste = win.checkKey()
    print("                                 >",teste,"<")  

    if teste == 'd':
        cont_d_parado = 0        
        to_em_d = True        
        cont_a_parado = 0        
        to_em_a = False
        loop_d = True        

    if teste == 'a':
        cont_a_parado = 0        
        to_em_a = True        
        cont_d_parado = 0        
        to_em_d = False 
        loop_a = True 


    if teste == '' and to_em_d:        #MOVIMENTAÇÃO LISA DO PRISCO
        if cont_d_parado < 32:
            direcao = 'd'
            cont_d_parado += 1
            loop_d = False
        else:                
            to_em_d = False
            direcao = ''
    elif teste == '' and to_em_a:
        if cont_a_parado < 32:
            direcao = 'a'
            cont_a_parado += 1
        else:   
            to_em_a = False
            direcao = ''
    else:
        direcao = teste
    
    if direcao == 'a':
        hitbox.move(-2,0)
        nave.move(-2, 0)       

    if direcao == 'd':
        hitbox.move(2,0)
        nave.move(2, 0)


     #------------------ TIRO ---------------------------------------
      
        
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

    #------------- COLISÃO DOS TIROS COM INIMIGOS---------------------------------

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
    contAbates.undraw()
        
    #print(hitbox.getP2())
    #print(tiro.getP2())
    #print(tiro.getCenter())

win.getMouse()
win.close()

'''Proximos passos:
1- Aumentar a dificuldade conforme o contador de pontuação
2- Estabelecer a colisão com a nave.
3- Melhorar a estética do game.
4- Talvez implementar um menu.
5- Adicionar sprites, e talvez mudar sprite da nave.
6- Adicionar animação de explosão na colisão dos inimigos.
'''