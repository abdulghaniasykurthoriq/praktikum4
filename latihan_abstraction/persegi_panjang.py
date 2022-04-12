from shape import Shape

class PersegiPanjang(Shape):
    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar
        
    def luas(self):
        print('Luas : ', self.panjang * self.lebar)
        
    def volume(self):
        # methiod ini harus ditulis meskiupan tidak valid karena mengikuti aturan abstraction
        pass