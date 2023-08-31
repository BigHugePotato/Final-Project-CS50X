import pytest
from project import Game, Player, Location, Item

def main():
    test_pick_up_item()

def test_pick_up_item():
    player = Player("Geir")
    game = Game(player)
    location = Location("House", "your quiet house in the eastside of Bergen.")
    item =  Item("Old diary", "A diary belonging to a long-deceased psychotherapist. It might have some valuable information.", use_text = "You open the diary and read about a patient with a split personality and a fascination for clowns.""Some of the pages is splattered with blood")
    location.add_object(item)
    player.location = location
    player.pick_up_item(item)
    assert item in player.inventory
    assert item not in location.objects

def test_drop_item():
    player = Player("Geir")
    game = Game(player)
    location = Location("House", "your quiet house in the eastside of Bergen.")
    item =  Item("Old diary", "A diary belonging to a long-deceased psychotherapist. It might have some valuable information.", use_text = "You open the diary and read about a patient with a split personality and a fascination for clowns.""Some of the pages is splattered with blood")
    player.location = location
    player.inventory.append(item)
    player.drop_item(item)
    assert item not in player.inventory
    assert item in location.objects

def test_move():
    player = Player("Geir")
    game = Game(player)
    location1 = Location("House", "your quiet house in the eastside of Bergen.")
    location2 = Location("Town Center", "The busy Bergen town center, a mix of unease and normalcy.")
    location1.add_adjacent_location("west", location2)
    player.location = location1
    game.move("west")
    assert player.location == location2

if __name__ == "__main__":
    main()