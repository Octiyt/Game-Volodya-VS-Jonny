class Character:
    name = "Jonny"
    health = 100
    damage = 5
    defence = 0


    def __init__(self,name,health = 100,damage=5,defence=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence

    def print_stats(self):
        print(f'-<{self.name} >-')
        print(f" Здоров\'я: {self.health}")
        print(f" Шкода: {self.damage}")
        print(f" Захист: {self.defence}")

    def take_damage(self, damage):
        actual_damage = max(damage - self.defence, 0)
        self.health = max(self.health - actual_damage, 0)
        print(f"{self.name} отримує {actual_damage} шкоди! Залишилось {self.health} здоров'я.")

    def attack(self, target):
        print(f"{self.name} атакує {target.name}")
        target.take_damage(self.damage)

