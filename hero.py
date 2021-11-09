# hero.py
import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
  def __init__(self, name, starting_health=100):
    self.abilities = list()
    self.armors = list()
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    self.deaths = 0
    self.kills = 0

  def add_ability(self, ability):
    self.abilities.append(ability)

  def add_weapon(self, weapon):
    self.abilities.append(weapon)

  def attack(self):
    total_damage = 0
    for ability in self.abilities:
      total_damage += ability.attack()
    return total_damage

  def add_armor(self, armor):
    self.armors.append(armor)

  def defend(self):
    total_block = 0
    for armor in self.armors:
        total_block += armor.block()
    return total_block 

  def take_damage(self, damage):
    defense = self.defend()
    if defense < damage:
        self.current_health -= (damage - defense)
    return self.current_health

  def is_alive(self):  
    return self.current_health >= 0

  def fight(self, opponent): 
    if len(self.abilities) <= 0 and len(opponent.abilities) <= 0:
        print("Draw")
        return
    while True:
        self.take_damage(opponent.attack())
        print(self.is_alive())
        print(self.current_health)
        if self.is_alive() == False:
            print(f"{opponent.name} won!")
            opponent.add_kill(1)
            self.add_death(1)
            return False
    
        opponent.take_damage(self.attack())
        if opponent.is_alive() == False:
            print(f"{self.name} won!")
            self.add_kill(1)
            opponent.add_death(1)
            return True

  def add_kill(self, num_kills):
    self.kills += num_kills

  def add_death(self, num_deaths):
    self.deaths += num_deaths




if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)


    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())



