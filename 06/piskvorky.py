from random import randrange

# ukol 9
def vyhodnot(herni_pole):
    if 'xxx' in herni_pole:
        return 'x'
    elif 'ooo'in herni_pole:
        return 'o'
    elif not '-' in herni_pole:
        return '!'
    else:
        return '-'

#print(vyhodnot('----------ooo-------'))

# ukol 10
herni_pole = '--------------------'
cislo_policka = 0
symbol = ''

def tah(herni_pole, cislo_policka, symbol):
    herni_pole_list = list(herni_pole)
    herni_pole_list[cislo_policka] = symbol
    herni_pole = ''.join(herni_pole_list)
    return herni_pole

#print(tah(herni_pole, 2, 'x'))

# ukol 11
herni_pole = '--------------------'
def tah_hrace(herni_pole):
    cislo_policka = int(input('Na kterou pozici chces hrat? (Zadej cislo od 0 do 19) ')) 
    herni_pole_list = list(herni_pole)
    while herni_pole_list[cislo_policka] == 'x' or herni_pole_list[cislo_policka] == 'o':
        print('Toto policko je uz obsazene')
        cislo_policka = int(input('Zadej jine cislo (od 0 do 19)'))
    return tah(herni_pole, cislo_policka, 'x')

#print(tah_hrace(herni_pole))

# ukol 12
def tah_pocitace(herni_pole):
    cislo_policka = randrange(0, 19)
    herni_pole_list = list(herni_pole)
    while herni_pole_list[cislo_policka] == 'x' or herni_pole_list[cislo_policka] == 'o':
        cislo_policka = randrange(0, 19)
    herni_pole_list[cislo_policka] = 'o'
    herni_pole = ''.join(herni_pole_list)
    return herni_pole

#print(tah_pocitace(herni_pole))

# ukol 13
def piskvorky1d():
    herni_pole = '--------------------'
    while vyhodnot(herni_pole) != 'x' or vyhodnot(herni_pole) != 'o' or vyhodnot(herni_pole) != '!':
        herni_pole = tah_hrace(herni_pole)
        print('pole po tahu hrace:', herni_pole)
        if vyhodnot(herni_pole) == 'x' or vyhodnot(herni_pole) == 'o' or vyhodnot(herni_pole) == '!':
            return 'Vyhral jsi'
        else:
            herni_pole = tah_pocitace(herni_pole)
            print('pole po tahu pocitace:', herni_pole)
            if vyhodnot(herni_pole) == 'x' or vyhodnot(herni_pole) == 'o' or vyhodnot(herni_pole) == '!':
                return 'Pocitac vyhral'

print(piskvorky1d())

    

    