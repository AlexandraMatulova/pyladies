from random import randrange 

pocet_bodu = 0
odpoved = input('Chces hrat? ')

while odpoved == 'ano':
    hodnota_karty = randrange(2,11)
    print(hodnota_karty)
    pocet_bodu = pocet_bodu + hodnota_karty
    if pocet_bodu > 21:
        print('Game over')
        break
    elif pocet_bodu == 21:
        print('You won!')
        break
    else:
        print('Celkovy pocet bodu je:', pocet_bodu)
        odpoved = input('Chces pokracovat? ')
print('Finalni pocet bodu je:', pocet_bodu)
