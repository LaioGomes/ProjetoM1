from time import sleep


sleep(5)


def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

def escolher_personagem():
    titulo('       Final da Copinha')

    print('Final da copa de bairro, os jogadores estão anciosos '
          '\ne com medo porque esse time é o vencedor das últimas 3 copas de bairro.'
          '\nVocê deve escolher com qual jogador vai participar desse jogo '
          '\ne tomar as decisões certas para levar o time à vitória nessa copa')

    print('Escolha um jogador:'
          '\n1 - Laio'
          '\n2 - Maycon'
          '\n3 - João')

    opcao = int(input('Escolha um jogador: '))
    if opcao == 1:
        print('Você escolheu Laio o atacante, bom de drible')
        print('O jogo rolou e tocaram a bola pra você,'
              '\nEstá vindo um jogador na sua direção pegar a bola, você é bom de drible mas o lateral tá livre'
              '\nVocê vai \n1 - passar ou \n2 - driblar?')


        opcao = int(input('E aí? '))
        if opcao == 1:
            print('Você passou a bola para o lateral mas ele perdeu a bola para '
                  '\no lateral do outro time, o lateral do outro time passou a bola para o atacante que '
                  '\npassou para o ponta direita e fez um gol'
                  '\nInfelizmente você escolheu errado e seu time perdeu o campeonato')
            exit()



        elif opcao == 2:
            print('Você escolheu driblar o o jogador a sua frente'
                  '\nÓtima escolha, voccê conseguiu avançar com a bola para o meio de campo e agora precisa decidir se'
                  '\n1 - Vai passar a bola para o Maycon ou \n2 - vai tentar continuar levando a bola sozinho até o gol')

            opcao = int(input('O que vai fazer?'))
            if opcao == 1:
                print('Muito bem, você passou a bola para Maycon, ele avançou pela direita até a grande área e agora está '
                      '\nprocurando alguém para passar a bola. Você vai:'
                      '\n1 - correr até lá para receber a bola ou \n2 - vai ficar onde está para descansar e deixar '
                      '\nque ele passe para outro jogador?')

                opcao = int(input('E aí, vai lá ou está cansado demais?'))
                if opcao == 1:
                    print('Você escolheu ficar deixar que Maycon faça o passe para outro jogador porque está cansado'
                          '\nInfelizmente maycon passou para um jogador que chutou a bola na trave'
                          '\no goleiro do time oposto pegou a bola e passou para frente, seu time acabou levando gol'
                          ''
                          '\nFim de jogo')
                    exit()

                elif opcao == 2:
                    print('Você escolheu correr até a grande áre e receber a bola, muito bem'
                          '\nMaycom passou a bola para você e vc ficou livre para chutar ao gol ou passar para João que está livre'
                          '\nE aí?'
                          '\n1 - Chuto pro gol'
                          '\n2 - Passo para João que está livre')

                    opcao = int(input('E aí?'))
                    if opcao == 1:
                        print('Muito bem, você deu um ótimo chute e o goleiro não conseguiu pegar a bola na gaveta'
                              '\nTodo o time comemora porque essa vitória foi linda demais'
                              '\nParabéns pela vitória')

                    elif opcao == 2:
                        print('Muito bem, João recebeu e chutou a bola na gaveta'
                              '\nTodo o time comemora porque essa vitória foi linda demais'
                              '\nParabéns pela vitória')

                    else:
                        while opcao != 1 and opcao != 2:
                            print('Tente outra vez')
                            opcao = int(input('E aí?'))
                            if opcao == 1:
                                print(
                                    'Muito bem, você deu um ótimo chute e o goleiro não conseguiu pegar a bola na gaveta'
                                    '\nTodo o time comemora porque essa vitória foi linda demais'
                                    '\nParabéns pela vitória')

                            elif opcao == 2:
                                print('Muito bem, João recebeu e chutou a bola na gaveta'
                                      '\nTodo o time comemora porque essa vitória foi linda demais'
                                      '\nParabéns pela vitória')





            elif opcao == 2:
                print('Você escolheu continuar levando a bola sozinho, não trabalhou a bola'
                      '\ndeixou de lado o trabalho de equipe e todos os jogadores do outro time foram em cima de vc'
                      '\nacabou perdendo a bola para o time adversário e levou seu time à derrota'
                      ''
                      '\nFim de jogo')
                exit()



            else:
                while opcao != 1 and opcao != 2:
                    print('Tente novamente')
                    opcao = int(input('O que vai fazer?'))
                    if opcao == 1:
                        print(
                            'Muito bem, você passou a bola para Maycon, ele avançou pela direita até a grande área e agora está '
                            '\nprocurando alguém para passar a bola. Você vai:'
                            '\n1 - correr até lá para receber a bola ou \n2 - vai ficar onde está para descansar e deixar '
                            '\nque ele passe para outro jogador?')


                    elif opcao == 2:
                        print('Você escolheu continuar levando a bola sozinho, não trabalhou a bola'
                              '\ndeixou de lado o trabalho de equipe e todos os jogadores do outro time foram em cima de vc'
                              '\nacabou perdendo a bola para o time adversário e levou seu time à derrota')
                        exit()



        else:
            while opcao != 1 and opcao != 2:
                print('Escolha uma opção válida')
                opcao = int(input('E aí? '))
                if opcao == 1:
                    print('Você passou a bola para o lateral mas ele perdeu a bola para '
                          '\no lateral do outro time, o lateral do outro time passou a bola para o atacante que '
                          '\npassou para o ponta direita e fez um gol'
                          '\nInfelizmente você escolheu errado e seu time perdeu o campeonato')
                    exit()



                elif opcao == 2:
                    print('Você escolheu driblar o o jogador a sua frente'
                          '\nÓtima escolha, voccê conseguiu avançar com a bola para o meio de campo e agora precisa decidir se'
                          '\n1 - Vai passar a bola para o Maycon ou \n2 - vai tentar continuar levando a bola sozinho até o gol')

                    opcao = int(input('O que vai fazer?'))
                    if opcao == 1:
                        print(
                            'Muito bem, você passou a bola para Maycon, ele avançou pela direita até a grande área e agora está '
                            '\nprocurando alguém para passar a bola. Você vai:'
                            '\n1 - correr até lá para receber a bola ou \n2 - vai ficar onde está para descansar e deixar '
                            '\nque ele passe para outro jogador?')

                        opcao = int(input('E aí, vai lá ou está cansado demais?'))
                        if opcao == 2:
                            print(
                                'Você escolheu ficar deixar que Maycon faça o passe para outro jogador porque está cansado'
                                '\nInfelizmente maycon passou para um jogador que chutou a bola na trave'
                                '\no goleiro do time oposto pegou a bola e passou para frente, seu time acabou levando gol'
                                ''
                                '\nFim de jogo')
                            exit()

                        elif opcao == 1:
                            print('Você escolheu correr até a grande áre e receber a bola, muito bem'
                                  '\nMaycom passou a bola para você e vc ficou livre para chutar ao gol ou passar para João que está livre'
                                  '\nE aí?'
                                  '\n1 - Chuto pro gol'
                                  '\n2 - Passo para João que está livre')

                            opcao = int(input('E aí?'))
                            if opcao == 1:
                                print(
                                    'Muito bem, você deu um ótimo chute e o goleiro não conseguiu pegar a bola na gaveta'
                                    '\nTodo o time comemora porque essa vitória foi linda demais'
                                    '\nParabéns pela vitória')

                            elif opcao == 2:
                                print('Muito bem, João recebeu e chutou a bola na gaveta'
                                      '\nTodo o time comemora porque essa vitória foi linda demais'
                                      '\nParabéns pela vitória')

                            else:
                                while opcao != 1 and opcao != 2:
                                    print('Tente outra vez')
                                    opcao = int(input('E aí?'))
                                    if opcao == 1:
                                        print(
                                            'Muito bem, você deu um ótimo chute e o goleiro não conseguiu pegar a bola na gaveta'
                                            '\nTodo o time comemora porque essa vitória foi linda demais'
                                            '\nParabéns pela vitória')

                                    elif opcao == 2:
                                        print('Muito bem, João recebeu e chutou a bola na gaveta'
                                              '\nTodo o time comemora porque essa vitória foi linda demais'
                                              '\nParabéns pela vitória')





                    elif opcao == 2:
                        print('Você escolheu continuar levando a bola sozinho, não trabalhou a bola'
                              '\ndeixou de lado o trabalho de equipe e todos os jogadores do outro time foram em cima de vc'
                              '\nacabou perdendo a bola para o time adversário e levou seu time à derrota'
                              ''
                              '\nFim de jogo')
                        exit()





#___________________________Maycon______________________________


    elif opcao == 2:
        print('Você escolheu Maycon o lateral direito, corre muito')
        print('O jogo rolou e tocaram a bola pra você,'
              '\nEstá vindo um jogador na sua direção pegar a bola, você não dribla bem mas é rápido'
              '\nPode tocar a bola e passar afrente'
              '\nVocê vai \n1 - driblar ou \n2 - passar?')
        opcao = int(input('E aí? '))
        if opcao == 1:
            print('Você tentou driblar o oponente mas perdeu a bola'
                  '\no lateral do outro time pegou e passou a bola para o atacante que '
                  '\npassou para o ponta direita e fez um gol'
                  '\nInfelizmente você escolheu errado e seu time perdeu o campeonato')
            exit()



        elif opcao == 2:
            print('Você escolheu tocar a bola para o jogador a sua frente e passar'
                  '\nÓtima escolha, voccê conseguiu avançar com a bola para o meio de campo e agora precisa decidir se'
                  '\n1 - Vai passar a bola para o Laio ou \n2 - vai tentar continuar levando a bola sozinho até o gol')

            opcao = int(input('O que vai fazer?'))
            if opcao == 1:
                print(
                    'Muito bem, você passou a bola para Laio, ele avançou pelo meio até a grande área e agora está '
                    '\nprocurando alguém para passar a bola. Você vai:'
                    '\n1 - correr até lá para receber a bola ou \n2 - vai ficar onde está para descansar e deixar '
                    '\nque ele passe para outro jogador?')

                opcao = int(input('E aí, vai lá ou está cansado demais?'))
                if opcao == 1:
                    print('Você escolheu ficar deixar que Laio faça o passe para outro jogador porque está cansado'
                          '\nInfelizmente Laio passou para outro jogador que chutou a bola na trave'
                          '\no goleiro do time oposto pegou a bola e passou para frente, seu time acabou levando gol'
                          ''
                          '\nFim de jogo')
                    exit()

                elif opcao == 2:
                    print('Você escolheu correr até a grande áre e receber a bola, muito bem'
                          '\nLaio passou a bola para você e vc ficou livre para chutar ao gol ou passar para João que está livre'
                          '\nE aí?'
                          '\n1 - Chuto pro gol'
                          '\n2 - Passo para João que está livre')

                    opcao = int(input('E aí?'))
                    if opcao == 1:
                        print('Muito bem, você deu um ótimo chute e o goleiro não conseguiu pegar a bola na gaveta'
                              '\nTodo o time comemora porque essa vitória foi linda demais'
                              '\nParabéns pela vitória')

                    elif opcao == 2:
                        print('Muito bem, João recebeu e chutou a bola na gaveta'
                              '\nTodo o time comemora porque essa vitória foi linda demais'
                              '\nParabéns pela vitória')

                    else:
                        while opcao != 1 and opcao != 2:
                            print('Tente outra vez')
                            opcao = int(input('E aí?'))
                            if opcao == 1:
                                print(
                                    'Muito bem, você deu um ótimo chute e o goleiro não conseguiu pegar a bola na gaveta'
                                    '\nTodo o time comemora porque essa vitória foi linda demais'
                                    '\nParabéns pela vitória')

                            elif opcao == 2:
                                print('Muito bem, João recebeu e chutou a bola na gaveta'
                                      '\nTodo o time comemora porque essa vitória foi linda demais'
                                      '\nParabéns pela vitória')





            elif opcao == 2:
                print('Você escolheu continuar levando a bola sozinho, não trabalhou a bola'
                      '\ndeixou de lado o trabalho de equipe e todos os jogadores do outro time foram em cima de vc'
                      '\nacabou perdendo a bola para o time adversário e levou seu time à derrota'
                      ''
                      '\nFim de jogo')
                exit()



            else:
                while opcao != 1 and opcao != 2:
                    print('Tente novamente')
                    opcao = int(input('O que vai fazer?'))
                    if opcao == 1:
                        print(
                            'Muito bem, você passou a bola para Laio, ele avançou pela direita até a grande área e agora está '
                            '\nprocurando alguém para passar a bola. Você vai:'
                            '\n1 - correr até lá para receber a bola ou \n2 - vai ficar onde está para descansar e deixar '
                            '\nque ele passe para outro jogador?')


                    elif opcao == 2:
                        print('Você escolheu continuar levando a bola sozinho, não trabalhou a bola'
                              '\ndeixou de lado o trabalho de equipe e todos os jogadores do outro time foram em cima de vc'
                              '\nacabou perdendo a bola para o time adversário e levou seu time à derrota')
                        exit()



        else:
            while opcao != 1 and opcao != 2:
                print('Escolha uma opção válida')
                opcao = int(input('E aí? '))
                if opcao == 1:
                    print('Você passou a bola para o meio-campo mas ele perdeu a bola para '
                          '\no lateral do outro time, o lateral do outro time passou a bola para o atacante que '
                          '\npassou para o ponta direita e fez um gol'
                          '\nInfelizmente você escolheu errado e seu time perdeu o campeonato')
                    exit()



                elif opcao == 2:
                    print('Você escolheu driblar o jogador a sua frente'
                          '\nÓtima escolha, voccê conseguiu avançar com a bola para o meio de campo e agora precisa decidir se'
                          '\n1 - Vai passar a bola para o Laio ou \n2 - vai tentar continuar levando a bola sozinho até o gol')

                    opcao = int(input('O que vai fazer?'))
                    if opcao == 1:
                        print(
                            'Muito bem, você passou a bola para Laio, ele avançou pela direita até a grande área e agora está '
                            '\nprocurando alguém para passar a bola. Você vai:'
                            '\n1 - correr até lá para receber a bola ou \n2 - vai ficar onde está para descansar e deixar '
                            '\nque ele passe para outro jogador?')

                        opcao = int(input('E aí, vai lá ou está cansado demais?'))
                        if opcao == 2:
                            print(
                                'Você escolheu ficar deixar que Maycon faça o passe para outro jogador porque está cansado'
                                '\nInfelizmente Laio passou para um jogador que chutou a bola na trave'
                                '\no goleiro do time oposto pegou a bola e passou para frente, seu time acabou levando gol'
                                ''
                                '\nFim de jogo')
                            exit()

                        elif opcao == 1:
                            print('Você escolheu correr até a grande áre e receber a bola, muito bem'
                                  '\nLaio passou a bola para você e vc ficou livre para chutar ao gol ou passar para João que está livre'
                                  '\nE aí?'
                                  '\n1 - Chuto pro gol'
                                  '\n2 - Passo para João que está livre')

                            opcao = int(input('E aí?'))
                            if opcao == 1:
                                print(
                                    'Muito bem, você deu um ótimo chute e o goleiro não conseguiu pegar a bola na gaveta'
                                    '\nTodo o time comemora porque essa vitória foi linda demais'
                                    '\nParabéns pela vitória')

                            elif opcao == 2:
                                print('Muito bem, João recebeu e chutou a bola na gaveta'
                                      '\nTodo o time comemora porque essa vitória foi linda demais'
                                      '\nParabéns pela vitória')

                            else:
                                while opcao != 1 and opcao != 2:
                                    print('Tente outra vez')
                                    opcao = int(input('E aí?'))
                                    if opcao == 1:
                                        print(
                                            'Muito bem, você deu um ótimo chute e o goleiro não conseguiu pegar a bola na gaveta'
                                            '\nTodo o time comemora porque essa vitória foi linda demais'
                                            '\nParabéns pela vitória')

                                    elif opcao == 2:
                                        print('Muito bem, João recebeu e chutou a bola na gaveta'
                                              '\nTodo o time comemora porque essa vitória foi linda demais'
                                              '\nParabéns pela vitória')





                    elif opcao == 2:
                        print('Você escolheu continuar levando a bola sozinho, não trabalhou a bola'
                              '\ndeixou de lado o trabalho de equipe e todos os jogadores do outro time foram em cima de vc'
                              '\nacabou perdendo a bola para o time adversário e levou seu time à derrota'
                              ''
                              '\nFim de jogo')
                        exit()

















    # ___________________________João______________________________





    elif opcao == 3:
        print('Você escolheu João ponta esquerda, tem uma ótima canhota')
        print('O jogo rolou e tocaram a bola pra você,'
              '\nEstá vindo um jogador na sua direção pegar a bola'
              '\nVocê vai \n1 - passar ou \n2 - driblar?')
        opcao = int(input('E aí? '))
        if opcao == 1:
            print('Você passou a bola para Laio mas ele perdeu a bola para '
                  '\no lateral do outro time, o lateral do outro time passou a bola para o atacante que '
                  '\npassou para o ponta direita e fez um gol'
                  '\nInfelizmente você escolheu errado e seu time perdeu o campeonato')
            exit()



        elif opcao == 2:
            print('Você escolheu driblar o o jogador a sua frente'
                  '\nÓtima escolha, voccê conseguiu avançar com a bola para o meio de campo e agora precisa decidir se'
                  '\n1 - Vai passar a bola para o Maycon ou \n2 - vai tentar continuar levando a bola sozinho até o gol')

            opcao = int(input('O que vai fazer?'))
            if opcao == 1:
                print(
                    'Muito bem, você passou a bola para Maycon, ele avançou pela direita até a grande área e agora está '
                    '\nprocurando alguém para passar a bola. Você vai:'
                    '\n1 - correr até lá para receber a bola ou \n2 - vai ficar onde está para descansar e deixar '
                    '\nque ele passe para outro jogador?')

                opcao = int(input('E aí, vai lá ou está cansado demais?'))
                if opcao == 1:
                    print('Você escolheu ficar deixar que Maycon faça o passe para outro jogador porque está cansado'
                          '\nInfelizmente maycon passou para um jogador que chutou a bola na trave'
                          '\no goleiro do time oposto pegou a bola e passou para frente, seu time acabou levando gol'
                          ''
                          '\nFim de jogo')
                    exit()

                elif opcao == 2:
                    print('Você escolheu correr até a grande áre e receber a bola, muito bem'
                          '\nMaycom passou a bola para você e vc ficou livre para chutar ao gol ou passar para João que está livre'
                          '\nE aí?'
                          '\n1 - Chuto pro gol'
                          '\n2 - Passo para João que está livre')

                    opcao = int(input('E aí?'))
                    if opcao == 1:
                        print('Muito bem, você deu um ótimo chute e o goleiro não conseguiu pegar a bola na gaveta'
                              '\nTodo o time comemora porque essa vitória foi linda demais'
                              '\nParabéns pela vitória')

                    elif opcao == 2:
                        print('Muito bem, João recebeu e chutou a bola na gaveta'
                              '\nTodo o time comemora porque essa vitória foi linda demais'
                              '\nParabéns pela vitória')

                    else:
                        while opcao != 1 and opcao != 2:
                            print('Tente outra vez')
                            opcao = int(input('E aí?'))
                            if opcao == 1:
                                print(
                                    'Muito bem, você deu um ótimo chute e o goleiro não conseguiu pegar a bola na gaveta'
                                    '\nTodo o time comemora porque essa vitória foi linda demais'
                                    '\nParabéns pela vitória')

                            elif opcao == 2:
                                print('Muito bem, João recebeu e chutou a bola na gaveta'
                                      '\nTodo o time comemora porque essa vitória foi linda demais'
                                      '\nParabéns pela vitória')





            elif opcao == 2:
                print('Você escolheu continuar levando a bola sozinho, não trabalhou a bola'
                      '\ndeixou de lado o trabalho de equipe e todos os jogadores do outro time foram em cima de vc'
                      '\nacabou perdendo a bola para o time adversário e levou seu time à derrota'
                      ''
                      '\nFim de jogo')
                exit()



            else:
                while opcao != 1 and opcao != 2:
                    print('Tente novamente')
                    opcao = int(input('O que vai fazer?'))
                    if opcao == 1:
                        print(
                            'Muito bem, você passou a bola para Maycon, ele avançou pela direita até a grande área e agora está '
                            '\nprocurando alguém para passar a bola. Você vai:'
                            '\n1 - correr até lá para receber a bola ou \n2 - vai ficar onde está para descansar e deixar '
                            '\nque ele passe para outro jogador?')


                    elif opcao == 2:
                        print('Você escolheu continuar levando a bola sozinho, não trabalhou a bola'
                              '\ndeixou de lado o trabalho de equipe e todos os jogadores do outro time foram em cima de vc'
                              '\nacabou perdendo a bola para o time adversário e levou seu time à derrota')
                        exit()



        else:
            while opcao != 1 and opcao != 2:
                print('Escolha uma opção válida')
                opcao = int(input('E aí? '))
                if opcao == 1:
                    print('Você passou a bola para o lateral mas ele perdeu a bola para '
                          '\no lateral do outro time, o lateral do outro time passou a bola para o atacante que '
                          '\npassou para o ponta direita e fez um gol'
                          '\nInfelizmente você escolheu errado e seu time perdeu o campeonato')
                    exit()



                elif opcao == 2:
                    print('Você escolheu driblar o o jogador a sua frente'
                          '\nÓtima escolha, voccê conseguiu avançar com a bola para o meio de campo e agora precisa decidir se'
                          '\n1 - Vai passar a bola para o Maycon ou \n2 - vai tentar continuar levando a bola sozinho até o gol')

                    opcao = int(input('O que vai fazer?'))
                    if opcao == 1:
                        print(
                            'Muito bem, você passou a bola para Maycon, ele avançou pela direita até a grande área e agora está '
                            '\nprocurando alguém para passar a bola. Você vai:'
                            '\n1 - correr até lá para receber a bola ou \n2 - vai ficar onde está para descansar e deixar '
                            '\nque ele passe para outro jogador?')

                        opcao = int(input('E aí, vai lá ou está cansado demais?'))
                        if opcao == 2:
                            print(
                                'Você escolheu ficar deixar que Maycon faça o passe para outro jogador porque está cansado'
                                '\nInfelizmente maycon passou para um jogador que chutou a bola na trave'
                                '\no goleiro do time oposto pegou a bola e passou para frente, seu time acabou levando gol'
                                ''
                                '\nFim de jogo')
                            exit()

                        elif opcao == 1:
                            print('Você escolheu correr até a grande áre e receber a bola, muito bem'
                                  '\nMaycom passou a bola para você e vc ficou livre para chutar ao gol ou passar para João que está livre'
                                  '\nE aí?'
                                  '\n1 - Chuto pro gol'
                                  '\n2 - Passo para João que está livre')

                            opcao = int(input('E aí?'))
                            if opcao == 1:
                                print(
                                    'Muito bem, você deu um ótimo chute e o goleiro não conseguiu pegar a bola na gaveta'
                                    '\nTodo o time comemora porque essa vitória foi linda demais'
                                    '\nParabéns pela vitória')

                            elif opcao == 2:
                                print('Muito bem, João recebeu e chutou a bola na gaveta'
                                      '\nTodo o time comemora porque essa vitória foi linda demais'
                                      '\nParabéns pela vitória')

                            else:
                                while opcao != 1 and opcao != 2:
                                    print('Tente outra vez')
                                    opcao = int(input('E aí?'))
                                    if opcao == 1:
                                        print(
                                            'Muito bem, você deu um ótimo chute e o goleiro não conseguiu pegar a bola na gaveta'
                                            '\nTodo o time comemora porque essa vitória foi linda demais'
                                            '\nParabéns pela vitória')

                                    elif opcao == 2:
                                        print('Muito bem, João recebeu e chutou a bola na gaveta'
                                              '\nTodo o time comemora porque essa vitória foi linda demais'
                                              '\nParabéns pela vitória')





                    elif opcao == 2:
                        print('Você escolheu continuar levando a bola sozinho, não trabalhou a bola'
                              '\ndeixou de lado o trabalho de equipe e todos os jogadores do outro time foram em cima de vc'
                              '\nacabou perdendo a bola para o time adversário e levou seu time à derrota'
                              ''
                              '\nFim de jogo')
                        exit()

    else:
        while opcao != 1 and opcao != 2:
            escolher_personagem()


# __________________________________________________________________________________







escolher_personagem()