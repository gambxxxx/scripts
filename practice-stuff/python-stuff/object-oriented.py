class Dog():
    def __init__(self, breed, name):
        self.breed=breed
        self.name=name
    
    def bark (self):
        print('Woof!, my nammeth beith {}'.format(self.name))

mydog=Dog(breed='Lab',name='Spike')
print(type(mydog))
print(mydog.breed)
mydog.bark()