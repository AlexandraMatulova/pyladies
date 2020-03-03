a = float(input('Zadej stranu ctverce v cm: '))
cislo_je_spravne = a > 0

if cislo_je_spravne:
    print('Obvod ctverce se stranou', a, 'cm je', 4 * a, 'cm')
    print('Obsah ctverce se stranou', a, 'cm je', a * a, 'cm2')
else:
    print('Strana musi byt kladna, jinak z toho nebude ctverec')

print('Dekujeme za pouziti geometricke kalkulacky')