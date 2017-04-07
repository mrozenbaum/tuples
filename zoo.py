# Create a tuple named zoo that contains your favorite animals.
zoo = ('Zebra', 'Tiger', 'Penguin', 'Elephant')
# Find one of your animals using the .index(value) method on the tuple.
print(zoo.index('Tiger'))
# Determine if an animal is in your tuple by using for value in tuple.
for animal in zoo:
  if animal is 'Tiger':
    print('Roarrrrrr')
# Create a variable for each of the animals in your tuple with this cool feature of Python.
(Zebra, Tiger, Penguin, Elephant) = zoo
print(Zebra)
print(Tiger)
print(Penguin)
print(Elephant)
# Convert your tuple into a list.
zoo = list(zoo)
print(type(zoo)) 
# Use extend() to add three more animals to your zoo.
zoo.extend(['Aligator', 'Giraffe', 'Donkey'])
print(zoo)  
# Convert the list back into a tuple.
zoo = tuple(zoo)
print(type(zoo)) 
print(zoo)
