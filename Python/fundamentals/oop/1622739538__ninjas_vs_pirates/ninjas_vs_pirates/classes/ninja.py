class Ninja:

    def __init__( self ,name,strength,speed,health):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        print(f"{self.name} attacked {pirate.name} for {self.strength} health")
        if (pirate.health >  0):
            print("aaaaaarggggg i've been hit")
        elif(pirate.health <= 0):
            print("aaaaaarggggg I've been defeated, but I will be back!")
        return self

    def run(self):
        if self.speed < 10:
            print(f"{self.name} failed to escape")
        else:
            print(f"{self.name} escaped")
    
    def potion(self,healing):
        if (self.health > 0 and healing <= 100):
            self.health += healing
            print(f"{self.name} used a potion and healed for: {healing} {self.name} health is now {self.health}")
        elif(self.health<= 0):
            print(f"{self.name} has been defeated")
        elif( healing >= 100 and self.health<= 0):
            print(f"{self.name} has too much health, you can't use a potion")
        return self

    def cameback(self):
        print(f"{self.name} came back to help!")