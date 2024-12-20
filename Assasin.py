import random
from Lesson2.character import Character

class Assassin(Character):
    def take_damage(self, damage):
        if random.random() < 0.1:
            damage = 1000
            print(f"{self.name} завдав супер удар! Нанесено 1000 одиниць шкоди.")
        self.health = max(self.health - damage, 0)
        return damage
