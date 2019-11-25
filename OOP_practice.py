

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


#then we can create child classes, that inherit everything from the dog class, but can extend or overwrite certain properties
class Pug(Dog):
    def chuff(self, num):
        return "{} chuffs {} times".format(self.name,num)

class Aussie(Dog):
    def run(self, speed):
        return "{} runs at {} miles per hour".format(self.name,speed)

ava = Aussie("Ava",3)

lou = Pug("Lou",1)
print(lou.chuff(3))
print(ava.run(10))
print(ava.name, ava.age)
print(ava.species)

#can check if different objects are an instance of a class
print(isinstance(ava,Dog))
print(isinstance(lou,Dog))
print(isinstance(lou,Pug))
print(isinstance(lou,Aussie))

#print(ava.description())
#print(ava.speak('woof woof'))