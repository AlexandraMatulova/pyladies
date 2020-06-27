from random import randrange
import images


words = ['kos', 'pes', 'slon']
def choose_word():
    return words[randrange(0, 3)]

chosen_word = choose_word()
print(chosen_word)


def playing_field_setup():
    playing_field = len(chosen_word) * '-'
    return playing_field

playing_field = playing_field_setup()
print('Hadane slovo:', playing_field)

pocet_pokusu = 0

def tah(playing_field):
    global pocet_pokusu
    pismeno = input('Zadej pismeno prosim: ')
    while len(pismeno) != 1:
        print('Zadal jsi spatny pocet pismenek')
        pismeno = input('Zadej pismeno prosim ')
    try:
        index = chosen_word.index(pismeno)
    except ValueError:
        pocet_pokusu += 1
        return playing_field
    playing_field_list = list(playing_field)
    playing_field_list[index] = pismeno
    playing_field = ''.join(playing_field_list)
    return playing_field
    
            
while '-' in playing_field:
    playing_field = tah(playing_field)
    if pocet_pokusu >= 1 and pocet_pokusu < len(images.images):
        print(images.images[pocet_pokusu-1])
        print('Hadane slovo:', playing_field)
    elif pocet_pokusu == len(images.images):
        print(images.images[pocet_pokusu-1])
        print('Hadane slovo bylo:', chosen_word, 'Prohral jsi')
        break
    else:
        print('Hadane slovo:', playing_field)
if not '-' in playing_field:
    print('Gratuluju, vyhral jsi')

