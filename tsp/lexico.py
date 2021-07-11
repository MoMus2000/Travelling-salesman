import pygame
import random
import math

def swap(arr,i,j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp
	return arr


def lexico_ordering(vals):
	largest_i = -1
	largest_j = -1
	for i in range(len(vals)-1):
		if(vals[i] < vals[i+1]):
			largest_i = i

	if largest_i == -1:
		return vals

	for j in range(len(vals)):
		if vals[largest_i] < vals[j]:
			largest_j = j

	vals = swap(vals,largest_i,largest_j)
	temp_vals = vals[largest_i+1:].copy()
	temp_vals.reverse()
	valz = vals[:largest_i+1] + temp_vals
	vals = valz.copy()
	return vals


def calulate_distance(cities,order):
	total_distance = 0
	for i in range(len(order)-1):
		indexA = order[i]
		indexB = order[i+1]
		cityA = cities[indexA]
		cityB = cities[indexB]
		dist = math.sqrt(math.pow(cityA[0]-cityB[0],2) + math.pow(cityA[1]-cityB[1],2))
		total_distance+=dist
	return total_distance




def main():
	running = True
	SCREEN_SIZE = (500,500)
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	cities = []
	order = []
	NUM_CITIES = 5
	clock = pygame.time.Clock()
	for i in range(NUM_CITIES):
		randx = random.randint(0,SCREEN_SIZE[0])
		randy = random.randint(0,SCREEN_SIZE[1])
		cities.append((randx,randy))
		order.append(i)

	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE)
	screen.fill(WHITE)
	max_iter = math.factorial(NUM_CITIES)
	curr_iter = 0
	best_distance = float('inf')
	best_order = []
	while(running):
		if(curr_iter<max_iter):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

			screen.fill(WHITE)


			new_order = []
			for i in range(0,len(order)):
				n = order[i]
				new_order.append(cities[n])
				pygame.draw.circle(screen,(0,0,0),(cities[n][0],cities[n][1]),10)
			pygame.draw.polygon(screen, (255, 255,0), new_order, width = 5)
			curr_distance = calulate_distance(cities,order)
			if curr_distance < best_distance:
				best_distance = curr_distance
				print(best_distance)
				best_order = new_order.copy()


			pygame.draw.polygon(screen, (123, 155,234), best_order, width = 5)

			order = lexico_ordering(order)
			pygame.display.flip()
			curr_iter+=1
		else:
			screen.fill(WHITE)
			for i in range(0,len(best_order)):
				n = best_order[i]
				pygame.draw.circle(screen,BLACK,(n[0],n[1]),10)
			pygame.draw.polygon(screen,(123,155,234),best_order,width=3)
			pygame.display.flip()

			# best_order_poly = []
			# for i in range(0,len(best_order)):
			# 	n = best_order[i]
			# 	best_order_poly.append(cities[n])
			# 	pygame.draw.circle(screen,(0,0,0),(cities[n][0],cities[n][1]),10)
			# pygame.draw.polygon(screen, (255, 255,0), best_order_poly, width = 5)



if __name__ == '__main__':
	vals = [1,2,3]
	results = lexico_ordering(vals)
	print(len(results))
	main()




