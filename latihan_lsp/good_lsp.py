class Vehicle:
    
    def __init__(self,name:str,speed:float):
        self.name = name
        self.speed = speed
    def get_name(self) -> str:
        return (f"The vehicle name {self.name}")
    
    def get_speed(self) -> str:
        return (f"The vehicle speed {self.speed}")

class VehicleWithoutEngine(Vehicle):
    
    def start_engine(self):
        # moving
        raise NotImplemented
        # start movung
    def start_moving(self):
        print("Moving")
        
class VehicleWitHEngine(Vehicle):
    def engine(self):
        pass

    def start_engine(self):
        self.engine()
        
class Car(VehicleWitHEngine):
    
    def start_engine(self):
        VehicleWitHEngine.start_engine(self)
        
class Bicycle(VehicleWithoutEngine):
    
    def start_engine(self):
        VehicleWithoutEngine.start_moving(self)