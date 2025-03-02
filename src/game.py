from .grid import Grid
from .player import Player
from .status import print_status
import random
from .import pickups
from .trap import Trap

player = Player(16, 5)
score = 0
inventory = []
g = Grid()
g.set_player(player)
g.make_walls()
g.place_wall_from_left(1, 4, 20)  # Placera en vägg
g.place_wall_from_left(1, 15, 10)  # Placera en vägg
g.place_wall_from_right(59, 15, 20)  # Placera en vägg s
g.place_wall_from_right(59, 6, 20)  # Placera en vägg
g.place_vertical_wall_up(10, 19,3)
g.place_vertical_wall_down(30,0,6)
g.place_vertical_wall_down(30,15,4)
g.place_u_shaped_wall(25,8,10,5)
g.place_u_shaped_wall(6,10,8,3)
g.place_u_shaped_wall(45,8,8,3)
g.place_u_shaped_wall(42,2,6,3)
pickups.randomize(g)


#placera fällor slumpmässigt
for _ in range(5):  # Antal fällor
    x, y = random.randint(0, g.width - 1), random.randint(0, g.height - 1)
    g.place_trap(x, y)

command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(score, g)
    #Ta emot användarens input
    command = input("Use WASD to move, Q/X to quit, I for current inventory: ")
    command = command.casefold()[:1]

    if command == "i":
        print("Current inventory:")
        if inventory:
            for item in inventory:
                print(item)
        else:
            print("Your inventory is empty.")
        continue


    # Kolla ifall inmatningen är någon av WASD tangenterna
    if command == 'w':  # Flytta upp
        dx, dy = 0, -1
    elif command == 'a':  # Flytta vänster
        dx, dy = -1, 0
    elif command == 's':  # Flytta ner
        dx, dy = 0, 1
    elif command == 'd':  # Flytta höger
        dx, dy = 1, 0
    else:
        continue  # Om ingen giltig input ges, flytta inte spelaren utan fortsätt med loopen.

        # Kontrollera om rörelsen är möjlig
    if player.can_move(dx, dy, g):
        player.move(dx, dy)
        score -= 1
        print(f"Moved one step, -1 point. Current score: {score}")  # Ger feedback till spelaren
        maybe_item = g.get(player.pos_x, player.pos_y)

        #Kontrollera ifall spelaren kliver i en fälla
        if isinstance(g.get(player.pos_x, player.pos_y), Trap):
            score -= g.get(player.pos_x, player.pos_y).penalty
            print(f"You fell into a trap!!! -{g.get(player.pos_x, player.pos_y).penalty} points.")

        # Kontrollera om det finns något föremål att plocka upp
        if maybe_item is not None and isinstance(maybe_item, pickups.Item):
            score += maybe_item.value
            inventory.append(maybe_item.name)  # Lägg till objektet i inventariet
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")

            g.clear(player.pos_x, player.pos_y)  # Ta bort objektet från spelplanen


# Hit kommer vi när while-loopen slutar

print("Thank you for playing!")