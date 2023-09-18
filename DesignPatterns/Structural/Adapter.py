# Interface that defines the methods the client will need/interact with
class TargetInterface:
    def request(self):
        pass

# Legacy Code whose methods functionality we require
class Adaptee:
    def old_request(self, special_string):
        print(special_string)

# Bridge between the 2
class Adapter(TargetInterface):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        self._adaptee.old_request("Acting as a bridge")


# Client requesting 
def client(target):
    target.request()


adaptee = Adaptee()
adapter = Adapter(adaptee)

client(adapter)