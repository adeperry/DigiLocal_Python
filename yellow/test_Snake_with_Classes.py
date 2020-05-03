import pygame
import Snake_with_Classes

def test_initial_movement():

    prev_distance = Snake_with_Classes.head.distance(0, 0) ## distance snake head from bottom left
    prev_X = Snake_with_Classes.head.getX()
    prev_Y = Snake_with_Classes.head.getY()
    prev_direction = Snake_with_Classes.head.dir

    mainloop_index = 0  ## number of mainloop iterations
    max_index = 1000

    while True:
        last_distance = Snake_with_Classes.head.distance(0, 0)
        if last_distance != prev_distance or (mainloop_index > max_index):
            if False:
                print("index= %d, prev_distance= %.3f, last_distance=%.3f" % 
                                                (mainloop_index, prev_distance, last_distance))
            break
        mainloop_index += 1
        Snake_with_Classes.mainloop()

    assert mainloop_index > 0 and (mainloop_index < max_index), "unexpected index %d" % mainloop_index

def test_change_direction():

    max_index = 1000
    directions = {
        pygame.K_w: 'up',
        pygame.K_s: 'down',
        pygame.K_a: 'left',
        pygame.K_d: 'right'
    }

    for i in directions.keys():
        e = pygame.event.Event(pygame.KEYDOWN, key=i)   
        pygame.event.post(e)  ## inject keypress

        mainloop_index = 0  ## number of mainloop iterations
        while True:
            if Snake_with_Classes.head.dir == directions[i] or (mainloop_index > max_index):
                break
            mainloop_index += 1
            Snake_with_Classes.mainloop()

        assert mainloop_index > 0 and (mainloop_index < max_index), "unexpected index %d" % mainloop_index



