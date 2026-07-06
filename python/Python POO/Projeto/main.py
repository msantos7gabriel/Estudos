from modules import modules as md

loop = True

while loop == True:
    print('Codificar - 1\nDecodificar - 2\n')

    md.user_choice()

    loop = md.ask_continue()
    if loop == False:
        print('Volte Sempre :D')
    else:
        md.clear()
