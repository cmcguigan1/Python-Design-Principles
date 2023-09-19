from abc import ABC, abstractmethod

# Product -> Interface
class IceCream(ABC):
    @abstractmethod
    def prepare(self):
        pass

# Concrete Product
class VanillaIceCream(IceCream):
    def prepare(self):
        return "Preparing Vanilla Ice Cream"

class ChocolateIceCream(IceCream):
    def prepare(self):
        return "Preparing Chocolate Ice Cream"

class StrawberryIceCream(IceCream):
    def prepare(self):
        return "Preparing Strawberry Ice Cream"

# Creator -> Interface
class IceCreamCreator(ABC):
    @abstractmethod
    def create_ice_cream(self):
        pass

# Concrete Creators
class VanillaIceCreamCreator(IceCreamCreator):
    def create_ice_cream(self):
        return VanillaIceCream()

class ChocolateIceCreamCreator(IceCreamCreator):
    def create_ice_cream(self):
        return ChocolateIceCream()

class StrawberryIceCreamCreator(IceCreamCreator):
    def create_ice_cream(self):
        return StrawberryIceCream()
    

# Client code
def order_and_prepare_ice_cream(ice_cream_creator):
    ice_cream = ice_cream_creator.create_ice_cream()
    print(ice_cream.prepare())

# Order and prepare different flavors of ice cream
vanilla_creator = VanillaIceCreamCreator()
chocolate_creator = ChocolateIceCreamCreator()
strawberry_creator = StrawberryIceCreamCreator()

order_and_prepare_ice_cream(vanilla_creator)
order_and_prepare_ice_cream(chocolate_creator)
order_and_prepare_ice_cream(strawberry_creator)



