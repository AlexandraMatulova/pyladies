value = ['pes', 'kocka', 'andulka', 'kralik', 'had']
key = []
for i in value:
    key.append(i[1:])
animals_dict = dict(zip(key, value))
#print(animals_dict)

sorted_animals = []
for key in sorted(animals_dict):
    sorted_animals.append(animals_dict[key])
print(sorted_animals)







