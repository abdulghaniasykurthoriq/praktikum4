import pygame
from overloading import Overloading

pygame.init()
active = True
window = pygame.display.set_mode((200,300))

#main
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        
    # ini yang dimaksud dengan overloading
    #cara 1 : menggunakan default kordinat constructor __init__
    overloading1 = Overloading(window)
    overloading1.draw_circle()
    
    #cara 2: mengisi kordinat sesaui keinginan
    overloading2 = Overloading(window,(200,300))
    overloading2.draw_circle()
    
    # cara 3: mengisi kordinat dan circle radius sesuai keinginan
    overloading2 = Overloading(window,(200,300), 50)
    overloading2.draw_circle()
    
    pygame.display.update()
    
    
    