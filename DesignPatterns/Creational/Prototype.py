from copy import deepcopy

# Prototype Interface (or Abstract Base Class)
class Prototype:
    def clone(self):
        pass

# Concrete Prototype
class ConcretePrototype(Prototype):
    def __init__(self, value):
        self.value = value

    def clone(self):
        # Use deepcopy to create a deep copy of the object
        return deepcopy(self)

# Client
if __name__ == "__main__":
    # Create a prototype instance
    prototype = ConcretePrototype(10)

    # Clone the prototype to create a new object
    new_object = prototype.clone()

    # Check if the new object is a separate instance with the same value
    print(prototype is new_object)  # Output: False
    print(prototype.value == new_object.value)  # Output: True