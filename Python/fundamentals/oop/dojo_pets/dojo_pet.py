from dojo_pets import Pet
class Ninja:
    def __init__(self,first_name,last_name,treats,pet_food,pet):
        self.first_name = first_name
        self.last_name= last_name
        self.treats = treats
        self.pet_food= pet_food
        self.pet = Pet(pet['name'],pet['type'],pet['tricks'],pet['noise'])
        
    def walk(self):
        print (f"Walking {pet['name']}")
        self.pet.play()

    def feed(self):
        print (f"Feeding {pet['name']} {self.pet_food}")
        self.pet.eat()

    def bathe(self):
        print (f"Bathing {pet['name']}")
        self.pet.noise()
    




pet ={
    "name": "Bouillon",
    "type": "dog",
    "tricks" : ["play dead","sit","bang"],
    "noise" : "Bark!"
}

pets=Ninja("Michelle","Lu","peanut butter","oats",pet)

pets.feed()
pets.bathe()
pets.walk()