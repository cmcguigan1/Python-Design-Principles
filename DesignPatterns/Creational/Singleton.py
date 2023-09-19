
class Singleton:
    _instance = None # private static instance

    # getInstance() method
    def __new__(cls):
        # Creating the instance if it doesn't already exist
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    

# Client code
singleton_instance1 = Singleton()
singleton_instance2 = Singleton()

print(singleton_instance1 is singleton_instance2)  # Output: True (both variables reference the same instance)