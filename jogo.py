import graphics as gf
from time import sleep
import random

win = gf.GraphWin('navezinha piu piu', 700, 800, autoflush=False)

def menu():
    background = gf.Image(gf.Point(350, 400), 'img/background.png')
    botaoIniciar = gf.Rectangle(gf.Point(250, 250), gf.Point(450, 330))
    botaoIniciar.setFill('dark green')
    botaoIniciar.setOutline('white')

    botaoSobre = gf.Rectangle(gf.Point(250, 350), gf.Point(450, 430))
    botaoSobre.setFill('dark orange')
    botaoSobre.setOutline('white')

    botaoSair = gf.Rectangle(gf.Point(250, 450), gf.Point(450, 530))
    botaoSair.setFill('dark red')
    botaoSair.setOutline('white')

    return [background, botaoIniciar, botaoSobre, botaoSair]

itensMenu = menu()

def sobreOjogo():
    background = gf.Image(gf.Point(350, 400), 'img/background.png')
    texto1 = gf.Text(gf.Point(345, 250), f'Sprisco Invaders é um jogo de batalha espacial onde o jogador\ntem o objetivo de protejer o planeta Terra de invasores alienígenas.')
    texto1.setTextColor('white')
    texto1.setSize(14)

    texto2 = gf.Text(gf.Point(340, 350), f'O jogador controla uma nave espacial que possui lançadores de laser\naltamente tecnológicos e que são capazes de eliminar os inimigos.')
    texto2.setTextColor('white')
    texto2.setSize(14)

    texto3 = gf.Text(gf.Point(340, 535), f'O jogo conta com uma mecânica simples e de fácil aprendizado.\n\nMapeamento de botões:\n\nAtirar: clique esquerdo do mouse\n\nMover a nave para equerda: tecla "a"\n\nMover a nave para direita: tecla "d"')
    texto3.setTextColor('white')
    texto3.setSize(14)


    return [background, texto1, texto2, texto3]

itensSobre = sobreOjogo()

def drawEstrutura():
    background = gf.Image(gf.Point(350, 400), 'img/background.png')

    pontuacao= gf.Text(gf.Point(55,20), "Pontuação:")
    pontuacao.setTextColor('white')
    pontuacao.setSize(15)

    Abates= gf.Text(gf.Point(200,20), "Abates:")
    Abates.setTextColor('white')
    Abates.setSize(15)

    #retanguloBranco = gf.Rectangle(gf.Point(0, 1), gf.Point(700, 50))
    #retanguloBranco.setFill('white')

    retangulo_vida = gf.Rectangle(gf.Point(375, 5), gf.Point(690, 25))
    retangulo_vida.setWidth(2)
    retangulo_vida.setOutline('white')

    retangulo_vidaNave = gf.Rectangle(gf.Point(500, 28), gf.Point(690, 47))
    retangulo_vidaNave.setWidth(2)
    retangulo_vidaNave.setOutline('white')

    return [background, pontuacao, Abates, retangulo_vida, retangulo_vidaNave]

itensJogo = drawEstrutura()

iniciar = False
sair = False

for elem in itensMenu:
    elem.draw(win)

while iniciar == False and sair == False:
    for elem in itensSobre:
        elem.undraw()

    clique = win.getMouse()
    if 250 < clique.getX() < 450 and 250 < clique.getY() < 330:
        iniciar = True
    
    if 250 < clique.getX() < 450 and 350 < clique.getY() < 430:
        for elem in itensMenu:
            elem.undraw()        
        for elem in itensSobre:
            elem.draw(win)
        win.getMouse()
        for elem in itensMenu:
            elem.draw(win)

    if 250 < clique.getX() < 450 and 450 < clique.getY() < 530:
        sair = True

    if sair == True:
        for elem in itensMenu:
            elem.undraw()
        win.close()

    if iniciar == True:    
        for elem in itensMenu:
            elem.undraw()
        for elem in itensJogo:
            elem.draw(win)
        break

#def retangulo_vida_planeta():

test= gf.Rectangle(gf.Point(377, 7), gf.Point(390, 22))
test.setFill('red')
test.draw(win)

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
direcao = ''
cont_d_parado = 0
to_em_d = False
loop_d = False
cont_a_parado = 0
to_em_a = False
loop_a = False 
velocidadeInimigo = 1

def explosao(x):
    explosoes= [gf.Image(x.getCenter(), 'img/explosao 0.png'),gf.Image(x.getCenter(), 'img/explosao 1.png'),gf.Image(x.getCenter(), 'img/explosao 2.png'),gf.Image(x.getCenter(), 'img/explosao 3.png'),gf.Image(x.getCenter(), 'img/explosao 4.png'),gf.Image(x.getCenter(), 'img/explosao 5.png'),gf.Image(x.getCenter(), 'img/explosao 6.png')]
    return explosoes

ta_explodindo= False
qual_explosao= 0
dificultador_speedinimigo=50
dificultador_qntinimigo=50
timer=100

while True:

    #---------------------------------TEMPORIZADOR------------------------------------
    temporizador = gf.Text(gf.Point(50,50), str(seg))
    temporizador.setSize(15)
    temporizador.setTextColor('white')
    temporizador.draw(win)
    #----------------------------------CONTADOR DE ABATES-----------------------------
    contAbates = gf.Text(gf.Point(200,50), str(inimigos_mortos))
    contAbates.setSize(15)
    contAbates.setTextColor('white')
    contAbates.draw(win)
    
    if ms == parametro:
        parametro += 60
        seg += 1
        #print(seg)

    if cont == timer:
        X = random.randint(5,680)
        inimigo = gf.Rectangle(gf.Point(X, -20), gf.Point(X + 40, 20)) # CRIA INIMIGOS DE ACORDO COM O TEMPO, E OS ADICIONA NA LISTA DE INIMIGOS
        inimigo.setOutline('red')
        inimigo.setFill('red')
        lista_inimigos.append(inimigo)
        inimigo.draw(win)
        cont = 0
    
    for elem in lista_inimigos:
        elem.move(0,velocidadeInimigo)
        if elem.getCenter().getY() == 820: # MOVE OS INIMIGOS E TAMBÉM OS ELIMINA EM CASO DE PASSAR DA TELA
            elem.undraw()
            lista_inimigos.remove(elem)
        
    #bordaesq = gf.Point(50, 750)

    #----------------------- MOVIMENTAÇÃO DA NAVE -----------------------------------
    teste = win.checkKey()
    #print("                                 >",teste,"<")  

    #-------------------------- TECLA PARA PAUSAR O JOGO ----------------------------
    if teste == 'Escape':
        pause = gf.Text(gf.Point(350, 400), f'PAUSE')
        pause.setTextColor('white')
        pause.setSize(36)
        pause.draw(win)

        win.getMouse()
        pause.undraw()

    #---------------------TECLA PARA MOVER A NAVE PARA A DIREITA -----------------------
    if teste == 'd':
        cont_d_parado = 0        
        to_em_d = True        
        cont_a_parado = 0        
        to_em_a = False
        loop_d = True        

    #-------------------TECLA PARA MOVER A NAVE PARA A EQAUERDA--------------------------
    if teste == 'a':
        cont_a_parado = 0        
        to_em_a = True        
        cont_d_parado = 0        
        to_em_d = False 
        loop_a = True 

    #-----------------------MOVIMENTAÇÃO LISA DO PRISCO--------------------------------------
    if teste == '' and to_em_d:
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
        if hitbox.getCenter().getX() > 2:
            hitbox.move(-4,0)
            nave.move(-4, 0)       

    if direcao == 'd':
        if hitbox.getCenter().getX() < 698:
            hitbox.move(4,0)
            nave.move(4, 0)

    #---------------------------------- TIRO ---------------------------------------      
    if len(lista_tiros) < 4:
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

    #--------------------------- COLISÃO DOS TIROS COM INIMIGOS---------------------------------
    for elem in lista_tiros:
        for a in lista_inimigos:
            if elem.getP1().getY() <= a.getP2().getY() <= hitbox.getP1().getY():
                if a.getP1().getX() <= elem.getP1().getX() <= a.getP2().getX():
                    
                    elem.undraw()
                    lista_tiros.remove(elem)
                    a.undraw()      
                    ta_explodindo= True      
                    quem_explodiu= a
                    lista_inimigos.remove(a)
                    inimigos_mortos += 1
                    seg += 2

    if ta_explodindo:
        boom= explosao(quem_explodiu)           
        boom[qual_explosao].draw(win)
        gf.update(100)
        boom[qual_explosao].undraw()
        qual_explosao+=1
        if qual_explosao >= len(boom):
            ta_explodindo= False
            qual_explosao=0

    if seg > dificultador_speedinimigo:
        velocidadeInimigo += 0.5
        dificultador_speedinimigo+=50
    
    if seg > dificultador_qntinimigo:
        if timer > 10:
            dificultador_qntinimigo+=50
            timer-=10
        
    #print(velocidadeInimigo)
    print(timer)
    cont+=1
    ms+=1
    gf.update(60)
    temporizador.undraw()
    contAbates.undraw()
        
    #print(hitbox.getP2())
    #print(tiro.getP2())
    #print(tiro.getCenter())

'''Proximos passos:
1- Aumentar a dificuldade conforme o contador de pontuação
2- Estabelecer a colisão com a nave.
3- Melhorar a estética do game.
4- Talvez implementar um menu.
5- Adicionar sprites, e talvez mudar sprite da nave.
6- Adicionar animação de explosão na colisão dos inimigos.
'''