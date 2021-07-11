import pygame
import random
import pygame.gfxdraw
import math
import sys


def main():
	cities = []
	order = []
	NODES = 5
	i=0
	clock = pygame.time.Clock()
	HEIGHT = 500
	WIDTH = 500
	best_ever = []
	orig_dist = float('inf')

	pygame.init()

	screen = pygame.display.set_mode((WIDTH,HEIGHT))

	screen.fill((255,255,255))



	for i in range(NODES):
		randx = random.randint(0,WIDTH)
		randy = random.randint(0,HEIGHT)
		cities.append((randx,randy))
		order.append(i)

	population = []
	for i in range(NODES):
		population.append(random.sample(order,len(order)))


	for pop in population:
		pass
	
	running = True	

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		for city in cities:
			pygame.draw.circle(screen, (0,0,0), (city[0],city[1]),10)

		pygame.draw.polygon(screen, (255, 156,56), cities, width = 5)


		pygame.display.flip()


		

	
	


	









if __name__ =='__main__':
	main()