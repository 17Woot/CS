import pygame 
import math

pygame.init()
screen_size = (800, 600)

time_step = 1
angle_per_step = 0.5
line_len = screen_size[0] * 0.8
cx = screen_size[0] // 2
cy = screen_size[1] // 2
clock = pygame.time.Clock()
run_length = 0
global_time = 0




screen = pygame.display.set_mode(screen_size)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((255, 255, 255))

    
    
    angle = time_step * angle_per_step
    x = line_len / 2 * math.sin(angle)
    y = line_len / 2 * math.cos(angle)

    line = pygame.draw.line(screen, (0, 0, 0), ((cx + x, cy + y)), ((cx - x), (cy - y)), 8)
    time_step += 0.1
    clock.tick(60)
    dt = clock.tick()
    global_time += dt
    if global_time > 10000:
        pygame.quit()
    

    pygame.display.update()
    
    

    

