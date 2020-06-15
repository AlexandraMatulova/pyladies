rodne_cislo = input("Jake je tvoje rodne cislo? ")

# (a)
if len(rodne_cislo) > 11:
    print('Zadane rodne cislo ma moc znaku')
if rodne_cislo[6] != '/':
    print('Nezadal jsi cislo ve spravnem formatu, za 6 cisly musi nasledovat /')
for i in rodne_cislo[0:6]:
    if ord(i) < 48 or ord(i) > 57:
        print('Nezadal jsi cislo ve spravnem formatu, prvnich 6 znaku musi byt cisla')
for i in rodne_cislo[7:11]:
    if ord(i) < 48 or ord(i) > 57:
        print('Nezadal jsi cislo ve spravnem formatu, posledni 4 znaky musi byt cisla') 

# (b)
rodne_cislo_withoutslash = rodne_cislo[:6] + rodne_cislo[7:]
rodne_cislo_int = int(rodne_cislo_withoutslash)
if rodne_cislo_int % 11 != 0:
    print('Nezadal jsi cislo ve spravnem formatu, zadane cislo neni delitelne 11')

# (c)
# rok
if int(rodne_cislo[:2]) < 85 and int(rodne_cislo[:2] > 20):
    print('Program akceptuje pouze rodna cisla vydana od roku 1985 do dneska')
# den
if int(rodne_cislo[4:6]) > 31:
    print('Den narozeni v rodnem cisle je nespravny, musi to byt cislo od 1 do 31')
# mesic
if int(rodne_cislo[2:4]) == 0:
    print('Zadany mesic rodneho cisla je nespravny')
elif int(rodne_cislo[2:4]) > 12 and int(rodne_cislo[2:4]) < 21:
    print('Zadany mesic rodneho cisla je nespravny')
elif int(rodne_cislo[2:4]) > 32 and int(rodne_cislo[2:4]) < 51:
    print('Zadany mesic rodneho cisla je nespravny')
elif int(rodne_cislo[2:4]) > 62 and int(rodne_cislo[2:4]) < 71:
    print('Zadany mesic rodneho cisla je nespravny')
elif int(rodne_cislo[2:4]) > 82:
    print('Zadany mesic rodneho cisla je nespravny')

# (d)
if int(rodne_cislo[2:4]) > 50:
    print('Pokud jsi muz, zadane rodne cislo neni spravne, ale format je v poradku')
if int(rodne_cislo[2:4]) < 50:
    print('Pokud jsi zena, zadane rodne cislo neni spravne, ale format je v poradku')

