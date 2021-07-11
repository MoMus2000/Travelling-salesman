import pygame
import random
import pygame.gfxdraw
import math
import sys


# x1,y1  x2,y2

def swap(arr,i,j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp
	return arr



def distance(arr):
	sum_of_distance = 0
	for i in range(0,len(arr)-1):
		x = math.pow(arr[i][0] - arr[i+1][0],2)
		y = math.pow(arr[i][1] - arr[i+1][1],2)
		dist = math.sqrt(x+y)
		sum_of_distance+=dist
	return sum_of_distance


def main():
	NODES = 7
	i=0
	clock = pygame.time.Clock()
	HEIGHT = 500
	WIDTH = 500
	best_ever = []
	orig_dist = float('inf')

	pygame.init()

	screen = pygame.display.set_mode((WIDTH,HEIGHT))

	screen.fill((255,255,255))

	cities = []
	for i in range(NODES):
		randx = random.randint(0,WIDTH)
		randy = random.randint(0,HEIGHT)
		cities.append((randx,randy))
	
	running = True

	orig = cities[0]
	

	while running:
		i+=1
		if(i >= math.factorial(NODES)):
			pass
			# screen.fill((255,255,255))
			# pygame.draw.polygon(screen, (255, 0,0), best_ever, width = 5)

		else:	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
			screen.fill((255,255,255))


			for city in cities:
				pygame.draw.circle(screen, (0,0,0), (city[0],city[1]),10)

			pygame.draw.polygon(screen, (255, 255,0), cities, width = 5)
			# pygame.gfxdraw.polygon(screen, cities,(255,0,0))

			calc_d = distance(cities)
			if(calc_d < orig_dist):
				orig_dist = calc_d
				# print(orig_dist)
				best_ever = cities.copy()
				# pygame.gfxdraw.polygon(screen, best_ever,(0,0,255),width=10)
				
				

			
			else:
				idx1 = random.randint(0,NODES-1)
				idx2 = random.randint(0,NODES-1)
				cities = swap(cities,idx1,idx2)


			pygame.draw.polygon(screen, (255, 0,0), best_ever, width = 5)
			# pygame.draw.circle(screen, (0,255,0), (orig[0],orig[1]),10)
			pygame.font.init()
			myfont = pygame.font.SysFont('Comic Sans MS', 30)
			textsurface = myfont.render(f"{i/math.factorial(NODES) *100:.2f} Complete", False, (0, 0, 0))
			screen.blit(textsurface,(0,0))

			pygame.display.flip()


		# clock.tick(60)



		

	
	


	









if __name__ =='__main__':
	main()