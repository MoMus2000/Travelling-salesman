import pygame
import random
import math
import random

def swap(arr,i,j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp
	return arr


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



def calculate_fitness(cities,population,best_distance):
	fitness = []
	for i in range(0,len(population)):
		d = calulate_distance(cities,population[i])
		if d < best_distance:
			best_distance = d
			best_order = population[i]
		fitness.append(1/(d+0.01))

	return fitness, best_order

def normalize_fitness(fitness, pop_size):
	total_fitness = 0
	for i in range(0,pop_size):
		total_fitness+= fitness[i]
	for i in range(0,pop_size):
		fitness[i]= fitness[i]/total_fitness

	return fitness

def next_generation(population,fitness):
	new_population = []
	for i in range(0,len(population)):
		order = pick_best(population,fitness)
		order = mutate(order)
		new_population.append(order)
	return new_population

def mutate(order):
	rand_val = random.uniform(0,1)
	if rand_val< 0.01:
		index_1 = random.randint(0,len(order)-1)
		index_2 = random.randint(0,len(order)-1)
		return swap(order,index_1,index_2) 
	return order

def pick_best(population,fitness):
	index = 0
	r = random.uniform(0,1)
	while(r > 0):
		r = r - fitness[index]
		index+=1
	index-=1
	return population[index].copy()


def main():
	running = True
	SCREEN_SIZE = (500,500)
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	cities = []
	order = []
	population = []
	fitness = []
	NUM_CITIES = 10
	clock = pygame.time.Clock()
	for i in range(NUM_CITIES):
		randx = random.randint(0,SCREEN_SIZE[0])
		randy = random.randint(0,SCREEN_SIZE[1])
		cities.append((randx,randy))
		order.append(i)

	for i in range(0,10):
		temp = order.copy()
		population.append(random.sample(temp,len(temp)))

	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE)
	screen.fill(WHITE)
	max_iter = math.factorial(NUM_CITIES)
	curr_iter = 0
	best_distance = float('inf')
	best_order = []
	
	while(running):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		screen.fill(WHITE)

		fitness , best_order = calculate_fitness(cities,population,best_distance)

		fitness = normalize_fitness(fitness, len(population))

		population = next_generation(population,fitness)

		new_order = []
		for i in range(0,len(best_order)):
			n = best_order[i]
			new_order.append(cities[n])
			pygame.draw.circle(screen,(0,0,0),(cities[n][0],cities[n][1]),10)
		pygame.draw.polygon(screen, (255, 145,230), new_order, 5)


		print(best_order)


		pygame.display.flip()



if __name__ == '__main__':
	main()




