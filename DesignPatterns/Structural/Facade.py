# Subsystem classes
class Engine:
    def start(self):
        print("Engine: Starting")

class FuelInjector:
    def inject_fuel(self):
        print("Fuel Injector: Injecting fuel")

class IgnitionSystem:
    def ignite(self):
        print("Ignition System: Igniting")

# Facade
class CarFacade:
    def __init__(self):
        self.engine = Engine()
        self.fuel_injector = FuelInjector()
        self.ignition_system = IgnitionSystem()

    def start_car(self):
        print("Car: Starting the car")
        self.engine.start()
        self.fuel_injector.inject_fuel()
        self.ignition_system.ignite()
        print("Car: Started successfully")

# Client code
car = CarFacade()
car.start_car()