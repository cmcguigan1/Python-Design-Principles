''' Using Python's abc's module for inheritance to define abstract classes and 
enforce that certain methods must be implemented by concrete (i.e., non-abstract) subclasses '''
from abc import ABC, abstractmethod

# You can create an abstract class by:
# 1. inheriting from ABC and 
# 2. using the @abstractmethod decorator to mark methods as abstract

# Makeshift interface extends ABC imported class
class MyInterface(ABC):
    # abstract method definition with decorator
    @abstractmethod
    def abstract_method(self):
        pass

class ConcreteClass(MyInterface):
    def abstract_method(self):
        return print("Implemented Abstract Method")


test = ConcreteClass()
test.abstract_method()


''' Using the duck tape concept '''
# No imports. The interface is just a class that demontrates strucutre and sub classes extend it

class MyOtherInterface:
    def required_method(self):
        pass

class MyOtherConcreteClass(MyOtherInterface):
    def abstract_method(self):
        return print("Another implementation")