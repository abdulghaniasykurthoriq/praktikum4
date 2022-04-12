class Vehicle:
    
    def __init__(self,name:str,speed:float):
        self.name = name
        self.speed = speed
    
    def get_name(self) -> str:
        return (f"The vehicle name {self.name}")
    
    def get_speed(self) -> str:
        return (f"The vehicle speed {self.speed}")
    def engine(self):
        print('-- Engine --')
        pass
    
    def start_engine(self):
        print('Start ', end="")
        self.engine()
        
class Car(Vehicle):
    def start_engine(self):
        Vehicle.start_engine(self)
        
class Bicycle(Vehicle):
    def start_engine(self):
        Vehicle.start_engine(self)