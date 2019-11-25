

class Dog:

    #classes create objects, which have attributes, the __init__() method initializes an object's initial attributes by giving them their default values
    def __init__(self,name,age): #basically just saying that each class, dog, has these two properties needed to initialize it, name and age
        self.name = name
        self.age = age

    #note, init is called autoamtically when we create new dog instances

    species = 'mammal'
    #all dogs share this, that their species is mammal, but name and age are particular to each dog


    #also have "instance methods" have to pass it "self"
    def description(self):
        return "{} is {} years old".format(self.name,self.age)

    #can also take an external input
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


ava = Dog("Ava",3)

print(ava.name, ava.age)
print(ava.species)

print(ava.description())
print(ava.speak('woof woof'))