from abc import ABC, abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def luas(self):
        pass
    
    @abstractclassmethod
    def volume(self):
        pass