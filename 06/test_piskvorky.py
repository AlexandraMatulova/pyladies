import piskvorky
import ai


def test_tah_check_index():
    herni_pole = '--------------------'
    cislo_policka = 0
    symbol = 'x'
    herni_pole = piskvorky.tah(herni_pole, cislo_policka, symbol)
    assert herni_pole == 'x-------------------'

def test_tah_cislo_policka():
    herni_pole = '--------------------'
    cislo_policka = 23
    symbol = 'x'
    herni_pole = piskvorky.tah(herni_pole, cislo_policka, symbol)
    assert herni_pole == '--------------------'

def test_vyhodnot_prazdne_pole():
    herni_pole = '--------------------'
    assert piskvorky.vyhodnot(herni_pole) == '-'

def test_vyhodnot_pocitac_vyhral():
    herni_pole = 'ooo-----------------'
    assert piskvorky.vyhodnot(herni_pole) == 'o'

def test_tah_pocitace_zmena_pole():
    herni_pole = '--------------------'
    assert ai.tah_pocitace(herni_pole) != herni_pole

def test_tah_pocitace_zmenen_pouze_spravny_znak():
    herni_pole = '--------------------'
    assert ai.tah_pocitace(herni_pole).count('o') == 1
    assert ai.tah_pocitace(herni_pole).count('x') == 0
    assert len(ai.tah_pocitace(herni_pole)) == len(herni_pole)






