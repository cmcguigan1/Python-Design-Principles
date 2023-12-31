''' Decorator Pattern with Classes'''
# Interface
class Coffee:
    def cost(self):
        pass

# Concrete Class. Extends the interface Coffee
class Espresso(Coffee):
    def cost(self):
        return 1.00

# Decorator. Extends the Coffee interface. Base Class for concrete decorators
class CoffeeDecorator(Coffee):
    # Maintaing a reference to the component
    def __init__(self, coffee):
        self._coffee = coffee
    
    # Implementing required method
    def cost(self):
        return self._coffee.cost()
    
# Concrete Implementation of the Decorator Abstract Class
class AddMilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.2
    
class AddSugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.5
    

''' Decorator Pattern with Functions '''
def my_decorator(func):
    def wrapper():
        print("Adding something before the function call")
        func()
        print("Adding something after the function call")
    
    return wrapper

# "Decorating the function"
@my_decorator
def example_function():
    print("Inside the function!!")

example_function()
''' Output: 
Adding something before the function call
Inside the function!!
Adding something after the function call 
'''