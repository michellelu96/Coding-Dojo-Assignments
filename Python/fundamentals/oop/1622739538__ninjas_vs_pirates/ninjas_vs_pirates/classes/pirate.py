import random
class Pirate:
    def __init__( self , name ):
        self.name = name
        self.strength = 100
        self.speed = 5
        self.health = 500

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        print(f"{self.name} attacked {ninja.name} for {self.strength} health")
        if(ninja.health <= 0):
            print  (f"I have defeated you {ninja.name}")
        return self

    def heal(self):
        healing = random.randint(1,100)
        if (self.health > 0):
            self.health += healing
            print(f"{self.name} healed for {healing} his health is now {self.health}")
        return self







