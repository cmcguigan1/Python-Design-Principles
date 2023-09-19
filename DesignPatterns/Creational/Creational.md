# Creational Design Patterns
Creational design patterns are design patterns which focus on creating objects effectively. They bring flexibility to the software design and help in the reusability of existing code. There are mainly 6 types of creational design patterns: Factory Method, Abstract Factory, Singleton, Prototype, Builder and Object Pool pattern.

## Factory Method
The Facctory Method provides an interface for creating objects but allows subclasses to alter the type of objects that will be created. In other words, it defines an interface for creating an object, but the specific subclass implementing the factory method determines the class of objects that will be instantiated.

### Use Cases
- Hide the existence of subclasses from the client
- i.e. We order an ice cream cone (either vanilla, chocolate or strawberry) from a store. We aren't concerned with the process of making the ice cream, the ingredients that go into it. The internal call by the shopkeeper to create a vanilla, chocolate, or strawberry ice cream is hidden from the user.

### Key Components
1. Creator -> Interface or Abstract Class. Defines the Factory Method that creates Products. Can declare other methods for the Products. 
2. Concrete Creator -> Class implements or is a sub-class of Creator. Each concrete creator implements the factory method to create specific product objects. 
3. Product -> Interface or Abstract Class. Defines the common interface that all concrete product classes must implement.
4. Concrete Product -> Class implements or is a sub-class of Product. Provides its own implementation of the common interface.

<img src="../../Assets/FactoryMethodClassDiagram.gif" width="70%">

## Abstract Factory

## Singleton

## Prototype

## Builder

## Object Pool