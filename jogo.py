import graphics as gf
from time import sleep
import random

win = gf.GraphWin('navezinha piu piu', 700, 800, autoflush=False)

#-------------------------------DEF QUE CONTÉM OS ITENS DO MENU---------------------------------------
def menu():
    background = gf.Image(gf.Point(350, 400), 'img/background.png')
    botaoIniciar = gf.Rectangle(gf.Point(250, 250), gf.Point(450, 330))
    botaoIniciar.setFill('dark green')
    botaoIniciar.setOutline('white')
    textoIniciar = gf.Text(gf.Point(350, 290), 'Jogar')
    textoIniciar.setTextColor('white')
    textoIniciar.setSize(34)

    botaoSobre = gf.Rectangle(gf.Point(250, 350), gf.Point(450, 430))
    botaoSobre.setFill('dark orange')
    botaoSobre.setOutline('white')
    textoSobre = gf.Text(gf.Point(350, 390), 'Sobre o Jogo')
    textoSobre.setTextColor('white')
    textoSobre.setSize(24)

    botaoSair = gf.Rectangle(gf.Point(250, 450), gf.Point(450, 530))
    botaoSair.setFill('dark red')
    botaoSair.setOutline('white')
    textoSair = gf.Text(gf.Point(350, 490), 'Sair')
    textoSair.setTextColor('white')
    textoSair.setSize(26)

    return [background, botaoIniciar, botaoSobre, botaoSair, textoIniciar, textoSobre, textoSair]
itensMenu = menu()

#---------------------------DEF QUE CONTÉM OS ITENS DA PARTE "SOBRE O JOGO"----------------------------
def sobreOjogo():
    background = gf.Image(gf.Point(350, 400), 'img/background.png')
    texto1 = gf.Text(gf.Point(345, 120), f'Sprisco Invaders é um jogo de batalha espacial onde o jogador\ntem o objetivo de protejer o planeta Terra de invasores alienígenas.')
    texto1.setTextColor('white')
    texto1.setSize(14)

    texto2 = gf.Text(gf.Point(340, 180), f'O jogador controla uma nave espacial que possui lançadores de laser\naltamente tecnológicos e que são capazes de eliminar os inimigos.')
    texto2.setTextColor('white')
    texto2.setSize(14)

    texto3 = gf.Text(gf.Point(350, 250), f'O jogador deve impedir que a vida da nave ou a do planeta cheguem a zero.\nCaso isso aconteça o jogo será finalizado e o jogador poderá ver sua pontuação.')
    texto3.setTextColor('white')
    texto3.setSize(14)

    texto4 = gf.Text(gf.Point(350, 410), f'Além dos inimigos, também existem as naves aliadas que podem trazer\nmelhorias para a nave do jogador ou até mesmo regenerar sua vida.\n\nTipos de melhorias:\n\nRegeneração de vida\n\nAumento da velocidade de movimento\n\nAumento na quantidade de disparos')
    texto4.setTextColor('white')
    texto4.setSize(14)

    texto5 = gf.Text(gf.Point(340, 660), f'O jogo conta com uma mecânica simples e de fácil aprendizado.\n\nMapeamento de botões:\n\nAtirar: clique esquerdo do mouse\n\nMover a nave para equerda: tecla "a"\n\nMover a nave para direita: tecla "d"\n\nPausar o jogo: "Esc"')
    texto5.setTextColor('white')
    texto5.setSize(14)

    return [background, texto1, texto2, texto3, texto4, texto5]
itensSobre = sobreOjogo()

#-------------------------------DEF QUE CONTÉM OS ITENS QUE COMPÕEM O JOGO-----------------------------
def drawEstrutura():
    background = gf.Image(gf.Point(350, 400), 'img/background.png')

    pontuacao= gf.Text(gf.Point(55,20), "Pontuação:")
    pontuacao.setTextColor('white')
    pontuacao.setSize(15)

    Abates= gf.Text(gf.Point(200,20), "Abates:")
    Abates.setTextColor('white')
    Abates.setSize(15)

    retangulo_vida = gf.Rectangle(gf.Point(502, 5), gf.Point(688, 25))
    retangulo_vida.setWidth(2)
    retangulo_vida.setOutline('white')
    texto_vida = gf.Text(gf.Point(428, 13), f'Vida do planeta:')
    texto_vida.setTextColor('white')
    texto_vida.setSize(14)

    retangulo_vidaNave = gf.Rectangle(gf.Point(593, 28), gf.Point(688, 47))
    retangulo_vidaNave.setWidth(2)
    retangulo_vidaNave.setOutline('white')
    texto_vidaNave = gf.Text(gf.Point(530, 36), f'Vida da nave:')
    texto_vidaNave.setTextColor('white')
    texto_vidaNave.setSize(14)

    return [background, pontuacao, Abates, retangulo_vida, retangulo_vidaNave, texto_vida, texto_vidaNave]
itensJogo = drawEstrutura()

#---------------------------------COORDENADAS DAS BARRINHAS DE VIDA DO PLANETA-------------------------
def retangulo_vida_planeta():

    retangulo1 = gf.Rectangle(gf.Point(507, 7), gf.Point(521, 22))
    retangulo1.setFill('red')
    retangulo2 = gf.Rectangle(gf.Point(525, 7), gf.Point(539, 22))
    retangulo2.setFill('red')
    retangulo3 = gf.Rectangle(gf.Point(543, 7), gf.Point(557, 22))
    retangulo3.setFill('red')
    retangulo4 = gf.Rectangle(gf.Point(561, 7), gf.Point(575, 22))
    retangulo4.setFill('red')
    retangulo5 = gf.Rectangle(gf.Point(579, 7), gf.Point(593, 22))
    retangulo5.setFill('red')
    retangulo6 = gf.Rectangle(gf.Point(597, 7), gf.Point(611, 22))
    retangulo6.setFill('red')
    retangulo7 = gf.Rectangle(gf.Point(615, 7), gf.Point(629, 22))
    retangulo7.setFill('red')
    retangulo8 = gf.Rectangle(gf.Point(633, 7), gf.Point(647, 22))
    retangulo8.setFill('red')
    retangulo9 = gf.Rectangle(gf.Point(651, 7), gf.Point(665, 22))
    retangulo9.setFill('red')
    retangulo10 = gf.Rectangle(gf.Point(669, 7), gf.Point(683, 22))
    retangulo10.setFill('red')

    lista_vida = [retangulo1, retangulo2, retangulo3, retangulo4, retangulo5, retangulo6, retangulo7, retangulo8, retangulo9, retangulo10]
    return lista_vida
barrasVida = retangulo_vida_planeta()

#---------------------------------COORDENADAS DAS BARRINHAS DE VIDA DA NAVE-------------------------------   
def retangulo_vida_nave():
    retangulo1 = gf.Rectangle(gf.Point(597, 30), gf.Point(611, 44))
    retangulo1.setFill('red')
    retangulo2 = gf.Rectangle(gf.Point(615, 30), gf.Point(629, 44))
    retangulo2.setFill('red')
    retangulo3 = gf.Rectangle(gf.Point(633, 30), gf.Point(647, 44))
    retangulo3.setFill('red')
    retangulo4 = gf.Rectangle(gf.Point(651, 30), gf.Point(665, 44))
    retangulo4.setFill('red')
    retangulo5 = gf.Rectangle(gf.Point(669, 30), gf.Point(683, 44))
    retangulo5.setFill('red')

    lista_vida = [retangulo1, retangulo2, retangulo3, retangulo4, retangulo5]
    return lista_vida
barrasVidaNave = retangulo_vida_nave()

#----------------------------DEF QUE CONTÉM OS ITENS QUE APARECEM QUANDO O JOGO É PAUSADO-------------------
def estrutura_pause():
    textoPause = gf.Text(gf.Point(350, 400), f'PAUSE')
    textoPause.setTextColor('white')
    textoPause.setSize(36)

    botaoContinuar = gf.Rectangle(gf.Point(230, 470), gf.Point(470, 530))
    botaoContinuar.setOutline('white')
    botaoContinuar.setFill('dark green')
    textoContinuar = gf.Text(gf.Point(350, 500), 'Continuar')
    textoContinuar.setTextColor('white')
    textoContinuar.setSize(26)

    botaoSair = gf.Rectangle(gf.Point(230, 550), gf.Point(470, 610))
    botaoSair.setOutline('white')
    botaoSair.setFill('dark red')   
    textoSair = gf.Text(gf.Point(350, 580), 'Encerrar Jogo')
    textoSair.setTextColor('white')
    textoSair.setSize(22)


    return [textoPause, botaoContinuar, textoContinuar, botaoSair, textoSair]
pause = estrutura_pause()

#------------------------DEF QUE RETORNA UMA LISTA DOS SPRITES QUE FORMAM A ANIMAÇÃO DE EXPLOSÃO--------------
def explosao(x):
    explosoes = [gf.Image(x.getCenter(), 'img/explosao 0.png'),gf.Image(x.getCenter(), 'img/explosao 1.png'),gf.Image(x.getCenter(), 'img/explosao 2.png'),gf.Image(x.getCenter(), 'img/explosao 3.png'),gf.Image(x.getCenter(), 'img/explosao 4.png'),gf.Image(x.getCenter(), 'img/explosao 5.png'),gf.Image(x.getCenter(), 'img/explosao 6.png')]
    return explosoes

#------------------------------------DEF QUE FAZ O FUNCIONAMENTO DO MENU---------------------------------------
def mostraMenu():
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
            for elem in barrasVida:
                elem.draw(win)
            for elem in barrasVidaNave:
                elem.draw(win)
mostraMenu()

#-------------------------------------------------DEF DO JOGO--------------------------------------------------   
def jogo():
    #GERANDO MOSTRANDO A NAVE NA TELA
    nave = gf.Image(gf.Point(350, 745), 'img/nave.png')
    nave.draw(win)

    #HITBOX CENTRAL DA NAVE
    hitbox= gf.Line(gf.Point(337, 700), gf.Point(363, 700))
    hitbox.setOutline('red')

    #HITBOX DA ASA ESQUERDA DA NAVE
    hitbox_asaEsquerda = gf.Line(gf.Point(305, 760), gf.Point(330, 760))
    hitbox_asaEsquerda.setOutline('red')

    #HITBOX DA ASA DIREITA DA NAVE
    hitbox_asaDireita = gf.Line(gf.Point(371, 760), gf.Point(396, 760))
    hitbox_asaDireita.setOutline('red')

    lista_hitbox = [hitbox, hitbox_asaEsquerda, hitbox_asaDireita]

    #VARIÁVEIS QUE SÃO UTILIZADAS DURANTE O LOOP
    lista_inimigos=[]
    lista_alien=[]
    lista_tiros=[]
    lista_aliado = []
    cont=0
    seg=0
    ms=0
    parametro=60
    inimigos_mortos = 0
    direcao = ''
    cont_d_parado = 0
    to_em_d = False
    cont_a_parado = 0
    to_em_a = False
    velocidadeInimigo = 1
    velocidadeNave = 4
    ta_explodindo = False
    qual_explosao = 0
    dificultador_speedinimigo = 50
    dificultador_qntinimigo = 50
    buff = 100
    timer = 100
    vida = 10
    vidaNave = 5

    while vida > 0 and vidaNave > 0:

        #----------------------------------CONTADOR DE ABATES-----------------------------
        contAbates = gf.Text(gf.Point(200,50), str(inimigos_mortos))
        contAbates.setSize(15)
        contAbates.setTextColor('white')
        contAbates.draw(win)
        
        #---------------------------------TEMPORIZADOR------------------------------------
        temporizador = gf.Text(gf.Point(50,50), str(seg))
        temporizador.setSize(15)
        temporizador.setTextColor('white')
        temporizador.draw(win)
        
        if ms == parametro:
            parametro += 60
            seg += 1
            #print(seg)

        #----------------------------------------------GERADOR DE INIMIGOS------------------------------------------------
        if cont == timer:
            X = random.randint(5,680)
            inimigo = gf.Rectangle(gf.Point(X, -20), gf.Point(X + 40, 15)) # CRIA INIMIGOS DE ACORDO COM O TEMPO, E OS ADICIONA NA LISTA DE INIMIGOS
            alien = gf.Image(inimigo.getCenter(), 'img/alien1.png')
            lista_alien.append(alien)
            #inimigo.setOutline('red')
            lista_inimigos.append(inimigo)
            alien.draw(win)
            #inimigo.draw(win)
            cont = 0

        cont_inimigo=0
        for i in lista_inimigos:
            i.move(0,velocidadeInimigo)
            lista_alien[cont_inimigo].move(0,velocidadeInimigo)                
            cont_inimigo+=1

        cont_inimigo=0
        for i in lista_alien:
            if i.getAnchor().getY() >= 820: # MOVE OS INIMIGOS E TAMBÉM OS ELIMINA EM CASO DE PASSAR DA TELA
                lista_alien.remove(i)
                lista_inimigos.remove(lista_inimigos[cont_inimigo])
                i.undraw()
                lista_inimigos[cont_inimigo].undraw()
                vida -= 1
                barrasVida[vida].undraw()
            cont_inimigo+=1

        #-----------------------------------------------------GERADOR DE ALIADOS------------------------------------------------------
        if seg >= buff and len(lista_aliado) == 0:
            X = random.randint(5,680)
            aliado = gf.Rectangle(gf.Point(X, -20), gf.Point(X + 40, 20)) # CRIA ALIADOS DE ACORDO COM A PONTUAÇÃO, E OS ADICIONA NA LISTA DE ALIADOS
            aliado.setOutline('blue')
            bufff = gf.Image(aliado.getCenter(), 'img/buff.png')
            #aliado.setFill('green')
            lista_aliado.append(aliado)
            #aliado.draw(win)
            bufff.draw(win)
            buff += 100
        
        for elem in lista_aliado:
            elem.move(0, 1.5)
            bufff.move(0, 1.5)                
            
            if elem.getCenter().getY() >= 820: #MOVE O ALIADO E SE CASO ELE PASSAR DA TELA É REMOVIDO DA LISTA
                elem.undraw()
                bufff.undraw()
                lista_aliado.remove(elem)

        #----------------------- MOVIMENTAÇÃO DA NAVE -----------------------------------
        teste = win.checkKey()
        #print("                                 >",teste,"<")  

        #-------------------------- TECLA PARA PAUSAR O JOGO ----------------------------
        if teste == 'Escape':
            for elem in pause:
                elem.draw(win)
            
        #------------------LÓGICA PARA SABER SE O USUÁRIO QUER CONTINUAR OU ENCERRAR O JOGO-----------------
            encerrar = False
            continuar = False
            while encerrar == False and continuar == False:
                clique = win.getMouse()
                if 230 < clique.getX() < 470:
                    if 470 < clique.getY() < 530:
                        continuar = True
            
                    if 550 < clique.getY() < 610:
                        encerrar = True
            
            if continuar:
                for elem in pause:
                    elem.undraw()
            if encerrar:
                vida = 0

        #---------------------------TECLA PARA MOVER A NAVE PARA A DIREITA -----------------------
        if teste == 'd':
            cont_d_parado = 0        
            to_em_d = True        
            cont_a_parado = 0        
            to_em_a = False
            #loop_d = True        

        #-------------------------TECLA PARA MOVER A NAVE PARA A EQAUERDA--------------------------
        if teste == 'a':
            cont_a_parado = 0        
            to_em_a = True        
            cont_d_parado = 0        
            to_em_d = False

        #--------------------------MOVIMENTAÇÃO LISA DO PRISCO--------------------------------------
        if teste == '' and to_em_d:
            if cont_d_parado < 32:
                direcao = 'd'
                cont_d_parado += 1
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
                hitbox.move(-velocidadeNave, 0)
                hitbox_asaEsquerda.move(-velocidadeNave, 0)
                hitbox_asaDireita.move(-velocidadeNave, 0)
                nave.move(-velocidadeNave, 0)      

        if direcao == 'd':
            if hitbox.getCenter().getX() < 698:
                hitbox.move(velocidadeNave, 0)
                hitbox_asaEsquerda.move(velocidadeNave, 0)
                hitbox_asaDireita.move(velocidadeNave, 0)
                nave.move(velocidadeNave, 0)

        #---------------------------------- TIRO ---------------------------------------      
        if len(lista_tiros) < 5:  #LIMITADOR DE TIROS
            if win.checkMouse():
                tiro = gf.Rectangle(gf.Point(hitbox.getCenter().getX(), 700), gf.Point(hitbox.getCenter().getX(),720))
                tiro.setOutline('red')
                lista_tiros.append(tiro)
                tiro.draw(win)
                #print(tiro.getP1())
            
        for elem in lista_tiros:
            elem.move(0,-10)
            #print(tiro.getP1())
            if elem.getCenter().getY() == -20:
                elem.undraw()
                lista_tiros.remove(elem)

        #--------------------------- COLISÃO DOS TIROS COM INIMIGOS---------------------------------
        for elem in lista_tiros:
            cont_inimigo=0
            for a in lista_inimigos:
                if elem.getP1().getY() <= a.getP2().getY() <= hitbox.getP1().getY():
                    if a.getP1().getX() <= elem.getP1().getX() <= a.getP2().getX():
                        ta_explodindo= True      
                        quem_explodiu= a
                        elem.undraw()
                        a.undraw()    
                        lista_alien[cont_inimigo].undraw() 
                        lista_tiros.remove(elem)
                        lista_inimigos.remove(a)
                        lista_alien.remove(lista_alien[cont_inimigo])
                        inimigos_mortos += 1
                        seg += 2
                cont_inimigo+=1
        
        #----------------------------------COLISÃO DOS INIMIGOS COM A NAVE-----------------------------  
        cont_inimigo=0
        for elem in lista_inimigos:
            for a in lista_hitbox:
                if elem.getP2().getY() >= a.getP1().getY():
                    if elem.getP1().getX() <= a.getP1().getX() <= elem.getP2().getX():
                        elem.undraw()
                        lista_alien[cont_inimigo].undraw()
                        lista_inimigos.remove(elem)
                        lista_alien.remove(lista_alien[cont_inimigo])
                        ta_explodindo = True
                        quem_explodiu = elem
                        vidaNave -= 1
                        barrasVidaNave[vidaNave].undraw()
                        #print(vidaNave)

                    elif elem.getP1().getX() <= a.getP2().getX() <= elem.getP2().getX():
                        elem.undraw()
                        lista_alien[cont_inimigo].undraw()
                        lista_inimigos.remove(elem)
                        lista_alien.remove(lista_alien[cont_inimigo])
                        ta_explodindo = True
                        quem_explodiu = elem
                        vidaNave -= 1
                        barrasVidaNave[vidaNave].undraw()
                        #print(vidaNave)

        #----------------------------------COLISÃO DO ALIADO COM A NAVE-----------------------------  
        for elem in lista_aliado:
            for a in lista_hitbox:
                if elem.getP2().getY() >= a.getP1().getY():
                    if elem.getP1().getX() <= a.getP1().getX() <= elem.getP2().getX():
                        lista_aliado.remove(elem)
                        elem.undraw()
                        bufff.undraw()
                        #ta_explodindo = True
                        #quem_explodiu = elem

                        if vidaNave < 5:       #CASO A NAVE JÁ TENHA TOMADO ALGUM DANO ENTÃO O BUFF TEM A CHANCE DE SER UMA RECUPERAÇÃO DE VIDA
                            sorteio = random.randint(0, 1)
                            #print(f'sorteio: {sorteio}')

                            if sorteio == 0:
                                barrasVidaNave[vidaNave].draw(win)
                                vidaNave += 1
                            if sorteio == 1:
                                velocidadeNave += 0.5
                        else:                           #CASO AINDA NÃO TENHA TOMADO DANO O BUFF AUTOMATICAMENTE SERÁ AUMENTO DE VELOCIDADE
                            velocidadeNave += 0.5

                        print(f'velocidade da nave: {velocidadeNave}')
                        print(f'vida da nave: {vidaNave}')

                    elif elem.getP1().getX() <= a.getP2().getX() <= elem.getP2().getX():
                        lista_aliado.remove(elem)
                        elem.undraw()
                        bufff.undraw()
                        #ta_explodindo = True
                        #quem_explodiu = elem
                        velocidadeNave += 1
                        if vidaNave < 5:
                            sorteio = random.randint(0, 1)
                            print(f'sorteio{sorteio}')
                            if sorteio == 0:
                                velocidadeNave += 1
                            if sorteio == 1:
                                barrasVidaNave[vidaNave].draw(win)
                                vidaNave+=1
                        else:
                            velocidadeNave += 1

                        print(f'velocidade{velocidadeNave}')
                        print(f'vida{vidaNave}')

        #----------------------------ANIMAÇÃO DE EXPLOSÃO DOS INIMIGOS--------------------------
        if ta_explodindo:
            boom= explosao(quem_explodiu)           
            boom[qual_explosao].draw(win)
            gf.update(100)
            boom[qual_explosao].undraw()
            qual_explosao+=1
            if qual_explosao >= len(boom):
                ta_explodindo= False
                qual_explosao=0

        #------------------SISTEMA DE AUMENTO DE DIFICULDADE CONFPORME O JOGO AVANÇA---------------
        if seg > dificultador_speedinimigo: #AUMENTO DA VELOCIDADE DOS INIMIGOS
            velocidadeInimigo += 0.5
            dificultador_speedinimigo+=50
            #print('wtffffff')
        
        if seg > dificultador_qntinimigo: #AUMENTO NA VELOCIDADE QUE OS INIMIGOS SÃO GERADOS
            if timer > 60:
                dificultador_qntinimigo+=50
                timer-=10
                #print('wtffffff')

        
        #print(velocidadeInimigo)
        #print(timer)
        cont+=1
        ms+=1
        gf.update(60)
        temporizador.undraw()
        contAbates.undraw()

        #print(hitbox.getP2())
        #print(tiro.getP2())
        #print(tiro.getCenter())
    
    return [seg, inimigos_mortos]

#----------------------DEF QUE CONTÉM OS ELEMENTOS QUE COMPÕEM A TELA DE FIM DE JOGO----------------------------
def fimJogo():
    pontos = jogo()
    background = gf.Image(gf.Point(350, 400), 'img/background.png')
    
    textoFim = gf.Text(gf.Point(350, 300), 'Fim de jogo')
    textoFim.setSize(36)
    textoFim.setTextColor('white')

    pontuacao = gf.Text(gf.Point(350, 500), f'Sua pontuação foi: {pontos[0]}')
    pontuacao.setSize(24)
    pontuacao.setTextColor('white')

    abates = gf.Text(gf.Point(350, 550), f'Inimigos abatidos: {pontos[1]}')
    abates.setSize(24)
    abates.setTextColor('white')

    return [background, textoFim, pontuacao, abates]
    
final = fimJogo()
for elem in final:
    elem.draw(win)
sleep(2)
win.getMouse()
win.close()

'''
Proximos passos (em ordem de prioridade):
1- Adicionar um sprite para quando a nave tomar dano.
2- Talvez adicionar o sprite de explosão se a vida da nave chegar a zero.
3- Talvez dar uma melhorada na tela de fim de jogo.
4- Implementar um sistema para armazenas as pontuações.
'''