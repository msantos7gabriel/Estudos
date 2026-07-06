from random import randint
bot_escolha = randint(1, 3)
escolha = int(
    input('Faça sua escolha: \n\n1. Pedra\n2. Papel\n3. Tesoura\n\n'))
jokenpo = ['','Pedra', 'Papel', 'Tesoura']

if escolha == bot_escolha:
    print('Empate ambos escolheram: {}'.format(jokenpo[escolha]))
elif bot_escolha == 1 and escolha == 2:
    print('Você Ganhou!!! \nSua escolha: {} \nEscolha do bot: {} '.format(
        jokenpo[escolha], jokenpo[bot_escolha]))
elif bot_escolha == 1 and escolha == 3:
    print('Você Perdeu \nSua escolha: {} \nEscolha do bot: {} '.format(
        jokenpo[escolha], jokenpo[bot_escolha]))
elif bot_escolha == 2 and escolha == 1:
    print('Você Ganhou!!! \nSua escolha: {} \nEscolha do bot: {} '.format(
        jokenpo[escolha], jokenpo[bot_escolha]))
elif bot_escolha == 2 and escolha == 3:
    print('Você Perdeu \nSua escolha: {} \nEscolha do bot: {} '.format(
        jokenpo[escolha], jokenpo[bot_escolha]))
elif bot_escolha == 3 and escolha == 2:
    print('Você Ganhou!!! \nSua escolha: {} \nEscolha do bot: {} '.format(
        jokenpo[escolha], jokenpo[bot_escolha]))
elif bot_escolha == 3 and escolha == 1:
    print('Você Perdeu \nSua escolha: {} \nEscolha do bot: {} '.format(
        jokenpo[escolha], jokenpo[bot_escolha]))
else:
    print('Error')