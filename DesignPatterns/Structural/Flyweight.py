from abc import ABC, abstractmethod

class FlyweightInterface(ABC):
    @abstractmethod
    def operation(self, extrinsic_state):
        pass

class ConcreteFlyweight(FlyweightInterface):
    def operation(self, extrinsic_state):
        return f"Intrinsic State: Shared, Extrinsic State: {extrinsic_state}"

class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}
    
    def get_flyweight(self, key):
        if key not in self._flyweights:
            self._flyweights[key] = ConcreteFlyweight()
        return self._flyweights[key]

# Client code
factory = FlyweightFactory()
flyweight1 = factory.get_flyweight("A")
flyweight2 = factory.get_flyweight("B")

print(flyweight1.operation("X"))  # Output: Intrinsic State: Shared, Extrinsic State: X
print(flyweight2.operation("Y"))  # Output: Intrinsic State: Shared, Extrinsic State: Y


''' Characters Example '''
'''
This approach allows you to efficiently represent and render text with different 
fonts and styles, minimizing memory usage by sharing common formatting information among characters.
'''

class CharacterFlyweight:
    def __init__(self, character, font, style):
        self.character = character
        self.font = font
        self.style = style

    def render(self):
        # Render the character with the specified font and style
        return f"Character: {self.character}, Font: {self.font}, Style: {self.style}"

class FontFlyweight:
    def __init__(self, font_name):
        self.font_name = font_name

class StyleFlyweight:
    def __init__(self, style_name):
        self.style_name = style_name

class FlyweightFactory:
    def __init__(self):
        self.character_flyweights = {}
        self.font_flyweights = {}
        self.style_flyweights = {}

    def get_character_flyweight(self, character, font, style):
        key = (character, font, style)
        if key not in self.character_flyweights:
            self.character_flyweights[key] = CharacterFlyweight(character, font, style)
        return self.character_flyweights[key]

    def get_font_flyweight(self, font_name):
        if font_name not in self.font_flyweights:
            self.font_flyweights[font_name] = FontFlyweight(font_name)
        return self.font_flyweights[font_name]

    def get_style_flyweight(self, style_name):
        if style_name not in self.style_flyweights:
            self.style_flyweights[style_name] = StyleFlyweight(style_name)
        return self.style_flyweights[style_name]

# Client code
factory = FlyweightFactory()

text = "Hello, World!"
formatted_text = []

# Assuming that "Hello" should be in Arial font and "World!" should be in Times New Roman
for char in text:
    font = factory.get_font_flyweight("Arial" if char == "H" else "Times New Roman")
    style = factory.get_style_flyweight("Bold" if char == "H" else "Regular")
    character = factory.get_character_flyweight(char, font, style)
    formatted_text.append(character.render())

print("\n".join(formatted_text))