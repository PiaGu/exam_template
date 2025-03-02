import random
from src.trap import Trap


class Grid:
    """Representerar spelplanen. """
    width = 60
    height = 20
    empty = "."  # Tecken för en tom ruta
    wall = "■"   # Tecken för en ogenomtränglig vägg

    def __init__(self):
        """Skapa ett objekt av klassen Grid"""
        # Spelplanen lagras i en lista av listor. Vi använder "list comprehension"
        # för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.data = [[self.empty for y in range(self.width)]
                     for z in range(self.height)]

    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs


    def make_walls(self):
        """Skapa väggar runt hela spelplanen"""
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)

    #Horisontell vägg vänster sida
    def place_wall_from_left(self, x_start, y, length):
        """Placera en horisontell vägg från en startpunkt åt höger."""
        for i in range(length):
            if x_start + i < self.width:  # Kontrollera att vi inte går utanför griden
                self.set(x_start + i, y, self.wall)

    # Horisontell vägg höger sida
    def place_wall_from_right(self, x_start, y, length):
        """Placera en horisontell vägg från en startpunkt åt vänster."""
        for i in range(length):
            if x_start - i >= 0:  # Kontrollera att vi inte går utanför griden
                self.set(x_start - i, y, self.wall)

    def place_vertical_wall_up(self, x, y_start, length):
        """Placera en vertikal vägg från en startpunkt uppåt."""
        for i in range(length):
            if y_start - i >= 0:
                self.set(x, y_start - i, self.wall)

    def place_vertical_wall_down(self, x, y_start, length):
        """Placera en vertikal vägg från en startpunkt nedåt."""
        for i in range(length):
            if y_start + i < self.height:
                self.set(x, y_start + i, self.wall)

    def place_u_shaped_wall(self, x, y, width, height):
        """Placera en U-formad vägg."""
        # Vänster sida av U, uppåt
        self.place_vertical_wall_down(x, y, height)
        # Höger sida av U, uppåt
        self.place_vertical_wall_down(x + width - 1, y, height)
        # Botten av U
        self.place_wall_from_left(x, y + height - 1, width)

    def place_trap(self, x, y):
        """Placera en fälla på en specifik position på spelplanen."""
        self.data[y][x] = Trap()


        # Används i filen pickups.py
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width-1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height-1)


    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty

