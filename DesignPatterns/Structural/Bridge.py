'''
The Bridge Pattern allows you to support multiple platforms and rendering engines independently. 
You can add new rendering engines or GUI elements without modifying existing code, 
promoting flexibility and extensibility in your GUI library.

'''
from abc import ABC, abstractmethod

# Implementor interface for rendering enigines
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass

# Concrete Implementors for different rendering engines
class DirectXRenderer(Renderer):
    def render_circle(self, radius):
        return f"Drawing a circle with radius {radius} using DirectX."

class OpenGLRenderer(Renderer):
    def render_circle(self, radius):
        return f"Drawing a circle with radius {radius} using OpenGL."
    

# Abstraction for GUI elements
class Shape(ABC):
    def __init__(self, renderer):
        self._renderer = renderer # Reference to the Implementor
    
    @abstractmethod
    def draw(self):
        pass


# Refined Abstractions for different GUI elements
class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        return self.renderer.render_circle(self.radius)
    

# Client code
directx_renderer = DirectXRenderer()
opengl_renderer = OpenGLRenderer()

circle1 = Circle(directx_renderer, 5)
circle2 = Circle(opengl_renderer, 10)

print(circle1.draw())  # Output: Drawing a circle with radius 5 using DirectX.
print(circle2.draw())  # Output: Drawing a circle with radius 10 using OpenGL.