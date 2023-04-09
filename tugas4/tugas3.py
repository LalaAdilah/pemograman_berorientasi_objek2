class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
class Item:
    def __init__(self, name):
        self.name = name
class Inventory:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)
    def print_inventory(self):
        print("add items:");
        for item in self.items:
            print(item.name)
player = Player("John")
gun = Item("Gun")
bomb = Item("Bomb")
player.inventory.add_item(gun)
player.inventory.add_item(bomb)
player.inventory.print_inventory()


