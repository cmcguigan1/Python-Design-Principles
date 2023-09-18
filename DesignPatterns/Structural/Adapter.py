class TargetInterface:
    def request(self):
        pass

class Adaptee:
    def old_request(self, special_string):
        print(special_string)

class Adapter(TargetInterface):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        self._adaptee.old_request("Acting as a bridge")

def client(target):
    target.request()


adaptee = Adaptee()
adapter = Adapter(adaptee)

client(adapter)