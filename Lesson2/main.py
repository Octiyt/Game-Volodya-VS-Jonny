from character import Character

player1 = Character("Jonny",120,7,0)
player1.print_stats()

player2= Character("Volodya",100,10,0)
player2.print_stats()

def game(player1, player2):
    while player1.health > 0 and player2.health > 0:
        player1.attack(player2)
        if player2.health == 0:
            print(f"{player2.name} програв раунд в RealLife")
            break
        player2.attack(player1)
        if player1.health == 0:
            print(f"{player1.name} програв раунд в RealLife")
            break

game(player1, player2)
