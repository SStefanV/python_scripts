def ggg():
    no_intentos = 7
    low_limit = 0
    hi_limit = 100
    my_guess = (hi_limit + low_limit) // 2
    respuesta = ''
    intentos = 1
    print('Piensa en un numero de 1 a 100')
    print('Lo adivinare en 7 intentos como mucho')
    input('Pulsa enter si quieres jugar\n')
    while no_intentos >= 1:
        my_guess = (hi_limit + low_limit) // 2
        print(f'INTENTO: {intentos}')
        print(f'Es tu numero {my_guess}?')
        respuesta = input('Pon\nmayor\nmenor\nsi\n\n')
        if respuesta == 'mayor':    
            intentos += 1
            no_intentos -= 1
            low_limit = my_guess   
        elif respuesta == 'menor':  
            intentos += 1
            no_intentos -= 1
            hi_limit = my_guess
        else:
            if respuesta == 'si':
                if intentos == 1:
                    print(f'He adivinado tu numero en {intentos} intento!')
                else:
                    print(f'He adivinado tu numero en {intentos} intentos!') 
                break
    new_game = input('Quieres jugar otra vez?\n')
    if new_game == 'si':
        ggg()
    else:
        quit()
ggg()