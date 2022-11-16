import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Flappy bird")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
x_bird = 50
y_bird = 350
x_tube1 = 400
x_tube2 = 600
x_tube3 = 800
tube_width = 50
tube_velocity = 2
tube1_height = randint(100, 400)
tube2_height = randint(100, 400)
tube3_height = randint(100, 400)
d_2tube = 150
bird_drop_velocity = 0
gravity = 0.5
backround_img = pygame.image.load("background.png")
backround_img = pygame.transform.scale(backround_img, (400, 600))
bird_img = pygame.image.load("bird.png")
bird_img = pygame.transform.scale(bird_img, (35, 35))
tube_img = pygame.image.load("tube.png")
tube_op_img = pygame.image.load("tube_op.png")
running = True
pausing = False
score = 0
font = pygame.font.SysFont("san", 20)
font1 = pygame.font.SysFont("san", 40)

tube1_pass = False
tube2_pass = False
tube3_pass = False

while running:
	clock.tick(60)
	screen.fill(WHITE)
	screen.blit(backround_img, (0, 0))

	bird = screen.blit(bird_img, (x_bird, y_bird))
	y_bird += bird_drop_velocity
	bird_drop_velocity += gravity

	tube1_img = pygame.transform.scale(tube_img, (tube_width, tube1_height))
	tube1 = screen.blit(tube1_img, (x_tube1, 0))
	tube2_img = pygame.transform.scale(tube_img, (tube_width, tube2_height))
	tube2 = screen.blit(tube2_img, (x_tube2, 0))
	tube3_img = pygame.transform.scale(tube_img, (tube_width, tube3_height))
	tube3 = screen.blit(tube3_img, (x_tube3, 0))

	tube1_op_img = pygame.transform.scale(tube_op_img, (tube_width, 600-tube1_height-d_2tube))
	tube1_op = screen.blit(tube1_op_img, (x_tube1, tube1_height+d_2tube))
	tube2_op_img = pygame.transform.scale(tube_op_img, (tube_width, 600-tube2_height-d_2tube))
	tube2_op = screen.blit(tube2_op_img, (x_tube2, tube2_height + d_2tube))
	tube3_op_img = pygame.transform.scale(tube_op_img, (tube_width, 600-tube3_height-d_2tube))
	tube3_op = screen.blit(tube3_op_img, (x_tube3, tube3_height+d_2tube))
	
	x_tube1 -= tube_velocity
	x_tube2 -= tube_velocity
	x_tube3 -= tube_velocity

	if x_tube1 < -tube_width:
		x_tube1 = 550
		tube1_height = randint(100, 400)
		tube1_pass = False
	if x_tube2 < -tube_width:
		x_tube2 = 550
		tube2_height = randint(100, 400)
		tube2_pass = False
	if x_tube3 < -tube_width:
		x_tube3 = 550
		tube3_height = randint(100, 400)
		tube3_pass = False

	if x_tube1+tube_width <= x_bird and tube1_pass == False:
		score += 1
		tube1_pass = True
	if x_tube2+tube_width <= x_bird and tube2_pass == False:
		score += 1
		tube2_pass = True
	if x_tube3+tube_width <= x_bird and tube3_pass == False:
		score += 1
		tube3_pass = True

	score_txt = font.render("Score: " + str(score), True, RED)
	screen.blit(score_txt, (5, 5))

	tubes = [tube1, tube2, tube3, tube1_op, tube2_op, tube3_op]
	for tube in tubes:
		if bird.colliderect(tube) or y_bird >= 600:
			tube_velocity = 0
			bird_drop_velocity = 0
			game_over_txt = font1.render("Game over, Score: " + str(score), True, RED)
			screen.blit(game_over_txt, (85, 260))
			space_txt = font.render("PRESS SPACE TO CONTINUE!", True, BLUE)
			screen.blit(space_txt, (120, 290))
			pausing = True

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				bird_drop_velocity = 0
				bird_drop_velocity -= 7
				if pausing:
					x_bird = 50
					y_bird = 350
					x_tube1 = 400
					x_tube2 = 600
					x_tube3 = 800
					tube_velocity = 2
					score = 0
					pausing = False

	pygame.display.flip()

pygame.quit()