import pygame

#class
class Overloading:
    # pada dasarnya pythoin tidak dapat 
    # melakukan overloading constructor
    
    def __init__(self, window, kordinat=None, radius=None):
        self.window = window
        if kordinat == None:
            self.kordinat = (10,10)
        else:
            self.kordinat = kordinat
        if radius == None:
            self.radius = 10
        else:
            self.radius = radius
        
    def draw_circle(self):
        circle_radius = self.radius
        border_width = 0
        colour = (0,0,255)
        pygame.draw.circle(self.window, colour, self.kordinat, circle_radius, border_width)