# PET NAMES
pet = {'Fluffy': 'hamster', 'Slimy': 'snake', 'Cutie': 'spider'}
for key, value in pet.items():
    print('{} is a {}.'.format(key, value))

# PET NAMES 2
def pets_at_home(pet):
    for key, value in pet.items():
        print('{} is a {}.'.format(key, value))

pet['Cutie'] = 'cat'
pets_at_home(pet)
    
pet['Lucky'] = 'dog'
pets_at_home(pet)

del pet['Slimy']
pets_at_home(pet)


