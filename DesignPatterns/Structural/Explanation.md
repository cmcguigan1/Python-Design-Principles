# Strucutral Design Patters
Use composition for merging classes and objects into a bigger structure to solve complex problems, making 
a solution extensible and flexible

## Decorator Pattern
Decorator is a structural pattern that allows adding new behaviors to objects dynamically by placing them inside special wrapper objects, called decorators.

Often used to extend the functionality of classes in a flexible and reusable way, without modifying their source code.

Main Idea:
- Wrap an existing class with one or more decorator classes, each adding new functionality or behavior to the original class.
- Decorators are stacked on top of each other, allowing you to combine features or responsibilities dynamically.

Key Components:
1. Component -> The base interface or abstract class. Defines the common interface for both the concrete components (original class to be extended) and the decorators (classes that add functionality)
2. Concrete Component -> The original class/object you want to enhance or extend
3. Decorator -> An abstract class. Implements the same interface as the component and maintains a reference to that component. Serves as the base class for concrete decorators
4. Concrete Decorator -> A concrete class. Extends the functionality of the component by adding new behavior or state. They override or add new methods to the component while delegating the original behavior to the component.


