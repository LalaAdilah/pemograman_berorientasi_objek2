#Nama   : Lala 'Adilah
#NIM    : 210511117
#Kelas  : R3/TI21C

class Animal:
    def make_sound(self):
        print("The animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows")

class Siberian_Husky(Dog):
    def make_sound(self):
        print("The siberian husky aiik")

class Ragdoll(Cat):
    def make_sound(self):
        print("The Ragdoll purrs")

def animal_sound(animal):
    animal.make_sound()

# Instantiate objects of each class
animal = Animal()
dog = Dog()
cat = Cat()
siberian_husky = Siberian_Husky()
ragdoll = Ragdoll()
# Call the animal_sound function for each object
animal_sound(animal)
animal_sound(dog) 
animal_sound(cat) 
animal_sound(siberian_husky)
animal_sound(ragdoll) 