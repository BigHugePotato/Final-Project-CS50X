
class Player:
    def __init__(self, name):
        self.name = name
        self.location = None
        self.inventory = []

    def pick_up_item(self, item):
        self.inventory.append(item)
        self.location.remove_object(item)


    def drop_item(self, item):
        self.inventory.remove(item)
        self.location.add_object(item)

    def has_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                return True
            return False

    def show_inventory(self):
        if not self.inventory:
            print("You're not carrying anything.")
        else:
            print("You're carrying:")
            for item in self.inventory:
                print(item.name)


class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.objects = []
        self.characters = []
        self.adjacent_locations = {}

    def add_adjacent_location(self, direction, location):
        self.adjacent_locations[direction] = location

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def add_character(self, character):
        self.characters.append(character)


class Item:
    def __init__(self, name, description, use_text=None):
        self.name = name
        self.description = description
        self.use_text = use_text or (f"You use the {self.name}. Nothing happens.")

    def use(self, game):
        print(self.use_text)



class Character:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

class Game:
    def __init__(self, player):
        self.player = player
        self.locations = []
        self.current_location = None


    def add_location(self, location):
        self.locations.append(location)


    def set_location(self, location):
        if location in self.locations:
            self.current_location = location
            self.player.location = location
        else:
            print("That location donsn't exist!")


    def get_current_state(self):
        current_location = self.player.location

        #describe the location
        state_description = current_location.description

        #describe the characters
        if current_location.characters:
            state_description += "\nYou see the following people here:"
            for character in current_location.characters:
                state_description += f"\n - {character.name}"

        #describe the objects
        if current_location.objects:
            state_description += "\nYou see the following items here:"
            for object_ in current_location.objects:
                state_description += f"\n - {object_.name}"

        return state_description




    def interact_with_item(self, item):
                print("Sucess!")
                print(item.description)


    def interact_with_character(self, character_name):
        current_location = self.player.location
        for character in current_location.characters:
            if character.name.lower() == character_name.lower():
                print("Sucess")
                return character.dialogue
        return "There's no one with that name here!"


    def run(self):
        print("You've just received an old, worn-out diary from a mysterious stranger. "
              "They told you it's crucial for you to explore and uncover the secrets of Bergen. "
              "You're now standing in your quiet house, diary in hand. "
              "It's time to venture out, and see what lies in store...")


        print("\nCommands: ")
        print("- 'look': Get a description of your current location.")
        print("- 'go [direction]': Move a direction.")
        print("- 'interact [item]': Interact with an item in your location.")
        print("- 'talk [character]': Talk to a specific character in you location.")
        print("- 'pickup [item]': Pick up a item in your location.")
        print("- 'drop [item]': Drop item.")
        print("- 'use [item]': Use item from inventory.")
        print("- 'inventory' : Show inventory.")

        while True:
            command = input("What would you like to do? ")
            self.execute_command(command)

    def move(self, direction):
        current_location = self.player.location
        if direction in current_location.adjacent_locations:
            new_location = current_location.adjacent_locations[direction]
            if new_location.name == "Lair" and not self.player.has_item("Silver Key"):
                print("You need a key to enter!")
                return
            elif new_location.name == "Lair" and self.player.has_item("Silver Key"):
                print("You unlock the lair with the silver key!")
                print("As the key turns in the lock, you brace yourself and push the heavy door open. The lair is darker than the night outside, yet, in the shadows, you can make out the silhouette of a slender man.")
                print("\nSuddenly, the room is filled with the eerie sound of laughter. The Clown steps forward into a beam of moonlight filtering in through a cracked window. Its face, is illuminated.")
                print("\nIt speaks in a voice that seems to echo from the walls, 'Ah, Geir, I was wondering when you'd join us. You've uncovered the secrets, pieced together the past, but the future? The future is where the real game begins.")
                exit()
            self.player.location = new_location
            print(f"You move to the {direction}. You're now at {self.player.location.name}.")
        else:
            print("You can't move in that direction!")


    def execute_command(self, command):
        command_parts = command.lower().split(" ", 1)
        action = command_parts[0]

        if len(command_parts) > 1:
            argument = command_parts[1]#.lower()
        else:
            argument = None

# LOOK
        if action == "look":
            print(self.get_current_state())
# GO
        elif action == "go":
            if argument:
                self.move(argument)
            else:
                print("Go where?")
# INTERACT
        elif action == "interact":
            if argument:
                for item in self.player.location.objects:
                    if argument.lower() in item.name.lower():
                        self.interact_with_item(item)
                        return
                print("There is no such item here.")
            else:
                print("Interact with what?")
# TALK
        elif action == "talk":
            if argument:
                print(self.interact_with_character(argument))
            else:
                print("Talk to whom?")
#QUIT
        elif action == "quit":
            print("Goodbye!")
            exit()
#USE
        elif action == "use":
            if argument:
                self.use_item(argument)
            else:
                print("Use what?")

#INVENTORY
        elif action == "inventory":
            self.player.show_inventory()
#PICKUP
        elif action == "pickup":
            if argument:
                for item in self.player.location.objects:
                    if argument.lower() in item.name.lower():
                        self.player.pick_up_item(item)
                        print(f"Sucsess! You picked up {item.name}")
                        return
                print("There is no such item here.")
            else:
                print("Pick up what?")
#DROP
        elif action == "drop":
            if argument:
                for item in self.player.inventory:
                    if argument.lower() in item.name.lower():
                        self.player.drop_item(item)
                        print(f"You dropped {item.name}")
                        return
                print("You're not carrying that.")
            else:
                print("Drop what?")
#ELSE
        else:
            print("I don't understand that command")


    def use_item(self, item_name):
        #print("Player's inventory:", [item.name for item in self.player.inventory])
        for item in self.player.inventory:
            if item_name.lower() in item.name.lower():
                item.use(self)
                return
        print("You're not carrying that.")



def create_locations():

    # Create some locations
    home = Location("House", "your quiet house in the eastside of Bergen.")
    town_center = Location("Town Center", "The busy Bergen town center, a mix of unease and normalcy.")
    library = Location("Bergen Library", "Bergen public library, a place full of old archives and secrets.")
    abandoned_house = Location("Abandoned House", "An eerie abandoned house, rumored to be haunted.")
    lair = Location("Lair", "A hidden lair, with a large metallic door. A silver clock stuck at 11:11 hangs above it.")

    #Create adjacent loactions
    home.add_adjacent_location("west", town_center)

    town_center.add_adjacent_location("east", home)
    town_center.add_adjacent_location("north", abandoned_house)
    town_center.add_adjacent_location("south", library)

    abandoned_house.add_adjacent_location("north", lair)
    abandoned_house.add_adjacent_location("south", town_center)

    library.add_adjacent_location("north", town_center)

    lair.add_adjacent_location("south", abandoned_house)

    return home, town_center, library, abandoned_house, lair


def create_characters():
    # Create some characters
    libby = Character("Libby",
        "Hello, Geir. Is everything okei? You seem perturbed. You know, Bergen has a long and complicated history."
        "There are cycles...terrible things that happen every 27 years. You can read more about the legend in an old book in the library in the south part of the town."
        "And there's something about a key, too, but it's been so long..."
        )
    henry = Character("Henry",
        "Geir, you seem like you're searching for answers. I've seen things in this town, things that would make your skin crawl."
        "Im glad you are here, it was me who sendt you the diary. The diary was written a psychotherapist, about something evil in this town."
        "The therapist have since gone missing. So have alot of kids. "
        "Im just trying to find out whats happening, nobody else is doing anything. I think somethings hiding in the cave to the north.."
        )
    bobby = Character("Bobby", "A Jolly bake, always ready with a pie and a smile.")
    clown = Character("Eerie Clown",
        "The eerie clown emerges from the shadows, a twisted grin on his face and a silver clock medallion around his neck, its hands also stuck at 11:11."
        "Welcome, Geir. I've been expecting you. The cycle is almost complete. Will you try to stop it, just like the others? Or will you join me in the eternal dance of time?."
        )
    return libby, henry, bobby, clown

def create_items():
    # Create some items
    diary = Item("Old diary", "A diary belonging to a long-deceased psychotherapist. It might have some valuable information.", use_text = "You open the diary and read about a patient with a split personality and a fascination for clowns.""Some of the pages is splattered with blood")
    silver_key = Item("Silver Key", "An old key made of silver. Its intricate design resembles a clown.", use_text = "You use the silver key. It fits perfectly in the lock of the lair's door.")
    clock_medallion = Item("Clock Medallion", "A silver medallion in the shape of a clock, stuck at 11:11.", use_text = "You touch the medallion. And eerie shiver runs down your spine.")
    dusty_book = Item("Dusty Book",
        "An aged book about Derry's folklore, lying in the library.", use_text =
        "As you open the 'Clockwork of Silver', a tale unfolds of a shape-shifting entity that terrorizes Bergen every 27 years, often appearing as a clown."
        "Each cycle is marked by clocks freezing at 11:11."
        "Previous victims pushed the clown into its lair, hidden west of the town. A silver key is needed for access."
        "The book ends with a prophecy: 'When time freezes at 11:11, Derry will face its greatest fear once again.")
    return diary, silver_key, clock_medallion, dusty_book



def main():

    # Create a player
    player = Player("Alex Robinchaud")
    game = Game(player)

    home, town_center, library, abanodoned_house, lair = create_locations()
    libby, henry, bobby, clown = create_characters()
    diary, silver_key, clock_medallion, dusty_book = create_items()


    # Add characters and items to locations
    town_center.add_character(libby)
    town_center.add_character(bobby)
    abanodoned_house.add_character(henry)
    lair.add_character(clown)

    home.add_object(diary)
    town_center.add_object(silver_key)
    library.add_object(dusty_book)
    lair.add_object(clock_medallion)



    # Add locations to the game
    for location in [home, town_center, library, abanodoned_house, lair]:
        game.add_location(location)

    game.set_location(home)

    game.run()




if __name__ == "__main__":
    main()