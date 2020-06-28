from random import randrange
import ai


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


herni_pole = '--------------------'
cislo_policka = 0
symbol = ''

def tah(herni_pole, cislo_policka, symbol):
    herni_pole_list = list(herni_pole)
    try:
        if herni_pole_list[cislo_policka] == '-':
            herni_pole_list[cislo_policka] = symbol
        else:
            print('Toto policko je uz obsazene, zkus to znovu.')
            return herni_pole
    except IndexError:
        print('Nezadal jsi cislo od 0 do 19. Zkus to znovu.')
        return herni_pole
    herni_pole = ''.join(herni_pole_list)
    return herni_pole

#print(tah(herni_pole, 2, 'x'))


herni_pole = '--------------------'
def tah_hrace(herni_pole):
    cislo_policka = int(input('Na kterou pozici chces hrat? (Zadej cislo od 0 do 19) ')) 

    return tah(herni_pole, cislo_policka, 'x')

#print(tah_hrace(herni_pole))


def piskvorky1d():
    herni_pole = '--------------------'
    while vyhodnot(herni_pole) == '-':
        tmp_herni_pole = herni_pole  
        while tmp_herni_pole == herni_pole:
            herni_pole = tah_hrace(herni_pole)
        print('pole po tahu hrace:', herni_pole)
        if vyhodnot(herni_pole) == 'x':
            return 'Vyhral jsi'
        elif vyhodnot(herni_pole) == '!':
            return 'Remiza'
        else:
            herni_pole = ai.tah_pocitace(herni_pole)
            print('pole po tahu pocitace:', herni_pole)
            if vyhodnot(herni_pole) == 'o':
                return 'Pocitac vyhral'
            elif vyhodnot(herni_pole) == '!':
                return 'Remiza'

    