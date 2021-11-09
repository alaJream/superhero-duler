from ability import Ability
from random import randint

class Weapon(Ability):
  def attack(self):
    attack_dmg = randint(int(self.max_damage)//2,int(self.max_damage))
    return attack_dmg

