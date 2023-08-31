# Unraveling Bergen: A text-based Adventure

#### Video Demo: https://youtu.be/4Te8zoYXQfg
#### Description:
This is a text-based adventure game set in the fantasy version town of Bergen. The player receives a mysterious diary and is tasked with uncovering the secrets of the town.

The core classes in the game are Player, Location, Item, Character, and Game.
Also functions such as the "create" functions and the main at the end.

### Player
The Player class is your digital alter ego in the game, maintaining records of your whereabouts and the loot you've collected along your journey. It allows you to gather items, discard them, and verify whether a particular item is in your inventory.

### Location
The Location class represents a place in the game. Each location has a name, description, objects, characters, and adjacent locations. Locations can have objects added or removed from them, and they can be connected to other locations in certain directions.

### Item
The Item class represents an object that can be picked up and used by the player. Each item has a name, description, and use text.

### Character
The Character class represents a non-player character (NPC) in the game. Each character has a name and a dialogue, which is shown when the player interacts with them.

## Game
The Game class is the main driver. It stores the player object, a list of all game locations, and the player's current location. It provides methods for adding locations, setting the player's current location, interacting with items, characters, and moving the player around the game world. It also includes a run method that starts the game, accepts player commands, and processes them.

## Main
The main function sets up the game by creating the player, locations, characters, and items. It adds characters and items to the locations, adds the locations to the game, sets the player's initial location, and starts the game.



### About
I made some design choices were made to make the game more intuitive and user-friendly, such as the use of lower case for commands and items, allowing the user to type commands and items in any case. Also, a error message is displayed if the user tries to use an item they don't have, rather than the game crashing.
There was a plan to implement a multi-choise system, but at that point i was halfway done.

### End
As i said in the video, this took far longer than i thought it would. And a lot more can be done.
I had to stop becouse i just added more and more. I forced an early ending, so its not a "game" yet i would say. But i have shown the fuctions and the stucture behind. And adding more text dosn't really do anything for this project/course. So i am happy with what is been done so far.