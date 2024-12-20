from Lesson2.character import Character
from Lesson3.berserk import Berserk
from Lesson3.tank import Tank
from Assasin import Assassin

player1 = Tank("Jonny",120,7,7 )
player1.print_stats()

player2= Assassin("Volodya",100,10,0)
player2.print_stats()

while player1.health > 0 and player2.health > 0:
    player1_damage = player1.attack(player2)
    print(f"{player1.name} атакував {player2.name} і наніс {player1_damage} шкоди")
    print(f"У {player2.name} лишилося {player2.health} здоров\'я. ")

    player2_damage = player2.attack(player1)
    print(f"{player2.name} атакував {player1.name} і наніс {player2_damage} шкоди")
    print(f"У {player1.name} лишилося {player1.health} здоров\'я. ")
    print("")

print("\n")
player1.print_stats()
player2.print_stats()

