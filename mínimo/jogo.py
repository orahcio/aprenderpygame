# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((800,640))
    screen.fill((255,0,0))

    image = pygame.image.load("01_image.png")
    screen.blit(image, (0, 320))
    
    pygame.display.flip()
    # define a variable to control the main loop
    running = True
    
    t = 0

    # main loop
    while running:
        # screen.fill((255,0,0))
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        
        screen.fill((255,0,0))
        screen.blit(image, (t%864-64, 320))
        pygame.display.flip()
        
        t += 0.1

        # if t>800:
        #    t=-32
    
    print(t)
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()