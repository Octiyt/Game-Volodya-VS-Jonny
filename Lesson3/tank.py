from Lesson2.character import Character

class Tank(Character):
    def take_damage(self, damage):
        reduced_damage = damage - self.defence
        if reduced_damage < 0:
            reduced_damage = 0
        self.health -= reduced_damage
        return reduced_damage
