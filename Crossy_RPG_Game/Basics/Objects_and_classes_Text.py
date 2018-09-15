# Python language basics 7
# classes and objects
# Class fields, methods, and constractors
# Object instatiation

# A class is just a blueprint that defines an objects attributes and behaviours
class GameCharacter:

    # A field or a global variable (assinged this value when class is instantiated)
    speed = 5


    # Constructor creates a new class instance and sets up the defined fields
    def __init__(self, name, width, height, x_pos, y_pos):
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    # A methos is just a function that typically modifies the classes fields
    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

# charcter_0 is a new instance of the GameCharacter class
character_0 = GameCharacter('char_0', 50, 100, 100, 100) ## this is an object!
character_0.name   # 'char_0'
character_0.name = 'char_1'
character_0.name   # 'char_1'

character_0.move(50,100)
character_0.x_pos  # 150
character_0.y_pos  # 200

# Python language basics 8
# subclasses, superclasses, and inheritance

# Player character is a subclass of GameCharacter
# Player character has access to everything defined in GameCharacter
class PlayerCharacter(GameCharacter):

    speed = 10

    # Should still provide a constructor/initializer
    def __init__(self, name, x_pos, y_pos):
        super().__init__(name, 100, 100, x_pos, y_pos)

    def move(self, by_y_amount):
        super().move(0,by_y_amount)

# player_character is a new instance of the PlayerCharacter Sub-class
player_character = PlayerCharacter('P_character',500, 500)
player_character.name  # 'P_character'
player_character.move(100)
print(player_character.x_pos) #600
print(player_character.y_pos) #600




