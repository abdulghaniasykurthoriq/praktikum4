from shape import Shape2D

class PersegiPanjang(Shape2D):
    def __init__(self, a, b):
        Shape2D.__init__(self,a,b)
        self.luas()