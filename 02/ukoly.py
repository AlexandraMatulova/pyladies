# Ukol c.13

vahaRyby = float(input('Kolik kg vazi ryba, kterou jsi ulovil? '))

if vahaRyby < 1:
    print('To vypada spis na zizalu')
elif vahaRyby < 3:
    print('Slava, mas kapra')
elif vahaRyby < 6:
    print('Nasel jsi sumce!')
elif vahaRyby < 25:
    print('V rybnice plavou i zraloci, jo?')
else:
    print('To neni ryba, ale mastodont')



# Ukol c.17

tahCloveka = input('kamen, nuzky nebo papir? ')

from random import randrange 
cislo = randrange(3) 

if cislo == 0:
    tahPocitace = 'kamen'
elif cislo == 1:
    tahPocitace = 'nuzky'
else:
    tahPocitace = 'papir'

print(tahPocitace)

if tahPocitace == tahCloveka:
    print('plichta')
elif (tahPocitace == 'kamen' and tahCloveka == 'nuzky') or (tahPocitace == 'nuzky' and tahCloveka == 'papir') or (tahPocitace == 'papir' and tahCloveka == 'kamen'):
    print('pocitac vyhral')
else:
    print('vyhral jsi')



# Ukol c.18

stastna_retezec = input('jsi stastna? ')
bohata_retezec = input('jsi bohata? ')

if stastna_retezec == 'ano':
    if bohata_retezec == 'ano':
        print('Gratuluji!')
    elif bohata_retezec == 'ne':
        print('Zkus min utracet')
    else:
        print('Nerozumim')
elif stastna_retezec == 'ne':
    if bohata_retezec == 'ano':
        print('Zkus se vic usmivat')
    elif bohata_retezec == 'ne': 
        print('To je mi lito')
    else:
        print('Nerozumim')
else: 
    print('Nerozumim')