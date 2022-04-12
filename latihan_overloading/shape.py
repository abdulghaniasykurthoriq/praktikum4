class Shape2D:
    # class mewakili komponen setiap bentuk bangun datar
    
    def __init__(self, a, b):
        self.a =a
        self.b = b
        
    def luas(self):
        print('Luas = ', self.a * self.b)
        
        