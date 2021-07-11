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
		dist = math.pow(cityA[0]-cityB[0],2) + math.pow(cityA[1]-cityB[1],2)
		total_distance+=dist
	return total_distance



def calculate_fitness(cities,population,best_distance,best_order):
	fitness = []
	current_best = float('inf')
	current_order = []
	for i in range(0,len(population)):
		d = calulate_distance(cities,population[i])
		if d < best_distance:
			best_distance = d
			best_order = population[i]

		if d < current_best:
			current_best = d
			current_order = population[i]
		fitness.append(1/(math.pow(d,8)))

	return fitness, best_order, best_distance, current_order

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
		order1 = pick_best(population,fitness)
		order2 = pick_best(population,fitness)
		order = crossover(order1,order2)
		order = mutate(order)
		new_population.append(order)
	return new_population


def crossover(order1,order2):
	start = random.randint(0,len(order1)-2)
	end = random.randint(start+1,len(order1)-1)
	new_order = order1[start:end]
	for i in range(0,len(order2)):
		if(order2[i] not in new_order):
			new_order.append(order2[i])
	return new_order


def mutate(order):
	rand_val = random.uniform(0,1)
	for i in range(0,len(order)):
		if rand_val< 0.05:
			index_1 = random.randint(0,len(order)-1)
			# swapping neighbors
			index_2 = (index_1 + 1) % len(order)
			order = swap(order,index_1,index_2) 
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
	SCREEN_SIZE = (600,600)
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	cities = []
	order = []
	population = []
	fitness = []
	NUM_CITIES = 20
	POPULATION_SIZE = 100
	current_best = []
	current_distance = 0
	clock = pygame.time.Clock()
	for i in range(NUM_CITIES):
		randx = random.randint(0,SCREEN_SIZE[0])
		randy = random.randint(0,SCREEN_SIZE[1])
		cities.append((randx,randy))
		order.append(i)

	for i in range(0,POPULATION_SIZE):
		temp = order.copy()
		population.append(random.sample(temp,len(temp)))

	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE)
	screen.fill(WHITE)
	max_iter = math.factorial(NUM_CITIES)
	curr_iter = 0
	best_distance = float('inf')
	best_order = []

	best_order = population[0]

	display_creation = False
	
	while(running):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					display_creation = not display_creation

		screen.fill(WHITE)

		fitness , best_order , best_distance, current_order= calculate_fitness(cities,population,best_distance,best_order)

		fitness = normalize_fitness(fitness, len(population))

		population = next_generation(population,fitness)

		new_order = []
		curr_order = []

		for i in range(0,len(current_order)):
			n = current_order[i]
			curr_order.append(cities[n])

		for i in range(0,len(best_order)):
			n = best_order[i]
			new_order.append(cities[n])
			pygame.draw.circle(screen,(0,0,0),(cities[n][0],cities[n][1]),10)
			pygame.font.init()
			myfont = pygame.font.SysFont('Comic Sans MS', 18)
			textsurface = myfont.render(f"{i}", False, (0, 0, 0))
			screen.blit(textsurface,(cities[n][0],cities[n][1]))

		if display_creation:
			pygame.draw.polygon(screen, (120, 145,120), curr_order, 10)
		pygame.draw.polygon(screen, (255, 145,230), new_order, 5)


		pygame.display.flip()
		clock.tick(5)



if __name__ == '__main__':
	main()




