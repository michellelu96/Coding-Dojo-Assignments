from classes.ninja import Ninja
from classes.pirate import Pirate



normal = Ninja('Christian',10,10,100)
boss = Ninja("Sensei Jim",50,15,150)
blue = Ninja("Max",15,10,100)
red= Ninja("Michealanglo",20,5,100)


jack_sparrow = Pirate("Captain Jack Sparrow")

boss.attack(jack_sparrow)
blue.attack(jack_sparrow)
red.attack(jack_sparrow)
normal.attack(jack_sparrow)
jack_sparrow.show_stats()
jack_sparrow.attack(normal)
boss.attack(jack_sparrow)
red.attack(jack_sparrow)
blue.attack(jack_sparrow)
jack_sparrow.show_stats()
blue.run()
jack_sparrow.attack(red)
blue.cameback()
boss.attack(jack_sparrow)
jack_sparrow.show_stats()
boss.attack(jack_sparrow)
jack_sparrow.show_stats()
jack_sparrow.heal()
boss.attack(jack_sparrow)
blue.attack(jack_sparrow)
jack_sparrow.attack(boss)
boss.potion(100)
boss.attack(jack_sparrow)
blue.attack(jack_sparrow)
jack_sparrow.show_stats()
jack_sparrow.attack(boss)
boss.potion(100)
boss.attack(jack_sparrow)
blue.attack(jack_sparrow)
jack_sparrow.show_stats()
jack_sparrow.attack(boss)
boss.potion(100)
boss.attack(jack_sparrow)
blue.attack(jack_sparrow)
jack_sparrow.show_stats()
jack_sparrow.attack(boss)
boss.potion(100)
boss.attack(jack_sparrow)


