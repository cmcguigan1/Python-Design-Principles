from abc import ABC, abstractmethod

# Subject -> Interface Proxy and RealSubject both implement
class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

# Real Subject -> Concrete Class implements Subject. Where the true functionality lies
class RealSubject(Subject):
    def request(self):
        return "RealSubject: Handling request."

# Proxy -> Directs requests to Real Subject
class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        # Additional behavior before forwarding the request
        result = "Proxy: Logging request.\n"
        result += self._real_subject.request()
        # Additional behavior after forwarding the request
        result += "\nProxy: Caching request result."
        return result

# Client code
real_subject = RealSubject()
proxy = Proxy(real_subject)

print("Client: Calling the proxy to request something.")
print(proxy.request())