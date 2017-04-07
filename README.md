Python Tuples

Tuples are like lists, but are immutable. They can't be modified once defined. However, finding values in a tuple is faster than in a list.

Setup

mkdir -p ~/workspace/python/exercises/tuples && cd $_
touch zoo.py
subl .
References

Python tuples
Introducing Tuples
Instructions

Create a tuple named zoo that contains your favorite animals.

Find one of your animals using the .index(value) method on the tuple.

Determine if an animal is in your tuple by using for value in tuple.

Create a variable for each of the animals in your tuple with this cool feature of Python.

# example
(lizard, fox, mammoth) = zoo
print(lizard)
Convert your tuple into a list.

Use extend() to add three more animals to your zoo.

Convert the list back into a tuple.