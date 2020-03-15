jmeno = input('Jake je tvoje krestni jemno ')
prijmeni = input('Jake je tvoje prijmeni ')

print('Tve inicialy jsou ', jmeno[0].upper() + prijmeni[0].upper())

retezec = input('zadej slovo ')
pozice = input('zadej cislo(od nuly do poctu pismen ve slovu - 1) ')
pismeno = input('zadej pismeno ')

print(retezec[:int(pozice)] + pismeno + retezec[int(pozice) + 1:])