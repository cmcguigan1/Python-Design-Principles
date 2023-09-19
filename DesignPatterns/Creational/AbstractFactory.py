from abc import ABC, abstractmethod

# Abstract Products
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class TextBox(ABC):
    @abstractmethod
    def display(self):
        pass

# Concrete Product
class WindowsButton(Button):
    def paint(self):
        return "Windows Button"

# Concrete Product
class WindowsTextBox(TextBox):
    def display(self):
        return "Windows TextBox"

# Concrete Product
class MacOSButton(Button):
    def paint(self):
        return "Mac OS Button"

# Concrete Product
class MacOSTextBox(TextBox):
    def display(self):
        return "Mac OS TextBox"
    

# Abstract Factory Interface
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self): 
        pass
    @abstractmethod
    def create_textbox(self):
        pass

# Concrete Factory
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_textbox(self):
        return WindowsTextBox()
    
# Concrete Factory
class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()
    
    def create_textbox(self):
        return MacOSTextBox()
    

    
# Client code
def create_gui(factory):
    button = factory.create_button()
    text_box = factory.create_text_box()
    return f"{button.paint()} and {text_box.display()}"

# Create GUI for Windows
windows_factory = WindowsFactory()
windows_gui = create_gui(windows_factory)
print(f"Windows GUI: {windows_gui}")

# Create GUI for macOS
macos_factory = MacOSFactory()
macos_gui = create_gui(macos_factory)
print(f"macOS GUI: {macos_gui}")