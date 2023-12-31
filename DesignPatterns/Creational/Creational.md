# Creational Design Patterns
Creational design patterns are design patterns which focus on creating objects effectively. They bring flexibility to the software design and help in the reusability of existing code. There are mainly 6 types of creational design patterns: Factory Method, Abstract Factory, Singleton, Prototype, Builder and Object Pool pattern.



## Factory Method
The Factory Method provides an interface for creating objects but allows subclasses to alter the type of objects that will be created. In other words, it declares an interface for creating an object, but the specific subclass implementing the factory method determines the class of objects that will be instantiated.

<img src="../../Assets/FactoryMethod.png" width="70%">

### Use Cases
- Hide the existence of subclasses from the client
- i.e. We order an ice cream cone (either vanilla, chocolate or strawberry) from a store. We aren't concerned with the process of making the ice cream, the ingredients that go into it. The internal call by the shopkeeper to create a vanilla, chocolate, or strawberry ice cream is hidden from the user.

### Main Idea
- Factory Method can produce only one type of object (only icecreams)
- Simplifying the creation of different Products of similar types

### Key Components
1. Creator -> Interface or Abstract Class. Declares the Factory Method that creates Products. Can declare other methods for the Products. 
2. Concrete Creator -> Class implements or is a sub-class of Creator. Each concrete creator implements the factory method to create specific product objects. 
3. Product -> Interface or Abstract Class. Declares the common interface that all concrete product classes must implement.
4. Concrete Product -> Class implements or is a sub-class of Product. Provides its own implementation of the common interface.

<img src="../../Assets/FactoryMethodClassDiagram.gif" width="70%">



## Abstract Factory
The Abstract Factory Pattern creates an object of several families of classes. Lets us produce families of related objects without specifying their concrete classes. One generalized factory can consist of multiple specialized factories, each producing a different kind of object.

<img src="../../Assets/AbstractFactory.png" width="70%">

### Use Cases
- Often used in scenarios where you need to ensure that the objects you create are consistent and compatible within a certain context. 
- It is commonly used in GUI libraries, where different platforms (e.g., Windows, macOS, Linux) require different families of widgets (buttons, text fields, etc.).
- i.e. A multi-cuisine restaurant that serves different kinds of foods like Chineese, Indian and French. There might be different chefs for each cusines/dish, but we aren't concerned with that. We order a dish from a cusine, and don't care how or where it's made. 

### Main Idea
- Abstract Factory can produce a family of different kinds of objects (multi-course and multi-cuisine meals)

### Key Components
1. Abstract Factory -> Interface or Abstract Class. Declares a set of factory methods, each responsible for creating a family of related objects. 
2. Concrete Factories -> Class implements or is a sub-class of Abstract Facotry. Each concrete factory is responsible for creating a family of objects that are compatible with each other.
3. Abstract Products -> Interface or Abstract Class. Declares the common interface that all concrete product classes must implement. Abstract products are typically organized into different families, each associated with a specific factory.
4. Concrete Products -> Class implements or is a sub-class of Product. Provides its own implementation of the common interface. Each concrete product belongs to a specific family and provides its own implementation of the declared methods.

<img src="../../Assets/AbstractFactoryClassDiagram.png" width="70%">



## Singleton
The Singleton Pattern specifies that only one instance can be instantiated from a given class. It ensures that a class has only one instance and provides a global access point to this particular instance. Singleton pattern helps in saving memory since the object is not created at every request. It either creates a new object or returns an existing object which has already been created.

<img src="../../Assets/Singleton.png" width="70%">

### Use Cases
- Used when a given class can have only one instance is available to all clients. 
- For example, a single database object which is shared by all the different parts of a program is an example of a singleton class.

### Key Components of the Singleton Class
1. Private Constructor -> A private constructor method. So Singleton Class cannot be instantiated from outside the class
2. Private Instance -> A private static instance of itself. This instance is the only one that will exist throughout the entire application's lifetime
3. Public Access Point -> A public static method (usually called getInstance()). Returns the private instance. This method is responsible for creating the instance on the first call and returning the existing instance on subsequent calls.
4. Lazy Initialization -> The Singleton instance is often created lazily (i.e., the instance is created only when it is first needed). This is done to minimize resource usage when the Singleton is not used immediately.

<img src="../../Assets/SingletonClassDiagram.gif" width="70%">



## Prototype
Prototype pattern creates a fully initialized instance that can be cloned. It lets us copy already existing objects without making the code dependent on other classes. A prototype pattern builds a product by copying the initial state of a prototype object.

<img src="../../Assets/Prototype.png" width="70%">

### Use Case
- For example, We can take a board game like chess as an example. The initial setup of a chess board is initialized once with the king, rooks, bishops, and other pieces in their designated places. Every time a new game starts, we call this object with the initial setup is already done, clone it and begin the game. There’s no need to create a new setup every single time the game is played.

### Main Idea
- The key idea behind this pattern is to avoid the overhead of creating objects from scratch when their structure is similar, and instead, create new instances by cloning an existing object (prototype).

### Key Components
1. Prototype Interface or Abstract Class -> Declares a method for cloning itself. It defines a clone() method that concrete prototypes must implement.
2. Concrete Prototype -> Class that implements the Prototype Interface and implement the clone() method 
3. Client -> Responsible for creating new objects by cloning existing prototypes. It requests a new object by invoking the clone() method on a prototype instance.

<img src="../../Assets/PrototypeClassDiagram.gif" width="70%">



## Builder
<img src="../../Assets/Builder.png" width="70%">
<img src="../../Assets/BuilderClassDiagram.png" width="70%">



## Object Pool
<img src="../../Assets/ObjectPool.png" width="70%">
<img src="../../Assets/ObjectPoolClassDiagram.gif" width="70%">