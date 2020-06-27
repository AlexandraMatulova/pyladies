import piskvorky


def test_tah_check_index():
    herni_pole = '--------------------'
    cislo_policka = 0
    symbol = 'x'
    herni_pole = piskvorky.tah(herni_pole, cislo_policka, symbol)
    assert herni_pole == 'x-------------------'

def test_tah

