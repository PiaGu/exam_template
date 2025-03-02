#from src.grid import Grid

class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=20, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol

pickups = [
    Item("carrot"), Item("apple"), Item("strawberry"), Item("cherry"), Item("watermelon"), Item("radish"),
    Item("cucumber"), Item("meatball"), Item("raspberry"), Item("blueberry"), Item("pasta"), Item("parmesan"),
    Item("tomato"), Item("mulberry"), Item("peach"), Item("grape"), Item("mango"), Item("banana"), Item("pineapple"),
    Item("kiwi"), Item("broccoli"), Item("spinach"), Item("mushroom"), Item("chocolate"), Item("cookie"), Item("cake"),
    Item("cheese"), Item("peanut"), Item("almond"), Item("walnut"), Item("lettuce"), Item("bell pepper"), Item("onion"),
    Item("garlic"), Item("ginger"), Item("date"), Item("fig"), Item("lemon"), Item("lime"), Item("avocado"),
    Item("hamburger"), Item("hotdog"), Item("pretzel"), Item("rice"), Item("salmon"), Item("gravy"), Item("sushi"),
    Item("taco"), Item("pizza"), Item("bread"), Item("butter"), Item("cheese"), Item("stew"), Item("falafel")
]


def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen


