from random import randrange

def tah_pocitace(herni_pole):
    cislo_policka = randrange(0, 19)
    herni_pole_list = list(herni_pole)
    while herni_pole_list[cislo_policka] == 'x' or herni_pole_list[cislo_policka] == 'o':
        cislo_policka = randrange(0, 19)
    herni_pole_list[cislo_policka] = 'o'
    herni_pole = ''.join(herni_pole_list)
    return herni_pole

#print(tah_pocitace(herni_pole))