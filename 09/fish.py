class Fish:
    def __init__(self, type):
        self.type = type
    
    def swim(self):
        print('{} can swim in water.'.format(self.type))

class Whales(Fish):
    def swim(self):
        super().swim()
        print('But it\'s not really a fish.')
    
    def size(self):
        print('{} is a giant of the sea.'.format(self.type))

class Sailfish(Fish):
    def swim(self):
        print('Many fish can swim, but Sailfish is the fastest swimmer.')
    
    def size(self):
        print('{} is not the biggest fish of the sea, but it is still the fastest.'.format(self.type))

white_shark = Fish('White shark')
humpback_whale = Whales('Humpback whale')
atlantic_sailfish = Sailfish('Atlantic sailfish')
white_shark.swim()
humpback_whale.swim()
humpback_whale.size()
atlantic_sailfish.swim()
atlantic_sailfish.size()