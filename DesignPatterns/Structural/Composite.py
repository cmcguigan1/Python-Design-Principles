from abc import ABC, abstractmethod

# Component -> Interface for objects 
class FileSystem(ABC):
    @abstractmethod
    def ls(self):
        pass

    @abstractmethod
    def add(self, name):
        pass

# Composite -> Class with children that are also type classes that implement Component
class Folder(FileSystem):
    def __init__(self, name):
        self._name = name
        self._contents = [] # Array of objects that implement FileSystem

    def ls(self):
        print(self._name)
        for item in self._contents:
            item.ls()
    
    def add(self, name):
        self._contents.append(name)
    
# Leaf -> Class with no children
class File(FileSystem):
    def __init__(self, name):
        self._name = name
    
    def ls(self):
        print(self._name)
    
    def add(self, name):
        pass

folderOne = Folder("1")
folderTwo = Folder("2")

fileA = File("A")
fileB = File("B")
fileC = File("C")

folderTwo.add(fileB)
folderTwo.add(fileC)

folderOne.add(folderTwo)
folderOne.add(fileA)

folderOne.ls()