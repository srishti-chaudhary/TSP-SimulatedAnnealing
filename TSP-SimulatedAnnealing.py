import numpy
import random
import math


class City:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

def pathCost (route):
    for i in range(len(route)):
        # Distnace between very city
        if i >= len(route)-1:
            break
        else:
            dist = numpy.sqrt(((route[i].x - route[i+1].x) ** 2) + ((route[i].y - route[i+1].y) ** 2))
            distance =+ dist
    
    # Distance between first and last city
    distance =+ numpy.sqrt(((route[0].x - route[-1].x) ** 2) + ((route[0].y - route[-1].y) ** 2))
    return distance

# List of cities

cities = list()

Ajmer = City(45, 78, 'Ajmer')
cities.append(Ajmer)

Alwar = City(33, 67, 'Alwar')
cities.append(Alwar)

Bharatpur = City(28, 30, 'Bharatpur')
cities.append(Bharatpur)

Bikaner = City(15, 34, 'Bikaner')
cities.append(Bikaner)

Bundi = City(34, 90, 'Bundi')
cities.append(Bundi)

Chittaurgarh = City(56, 45, 'Chittaurgarh')
cities.append(Chittaurgarh)

Bundi = City(25, 67, 'Bundi')
cities.append(Bundi)

Jaipur = City(68, 55, 'Jaipur')
cities.append(Jaipur)

Jodhpur = City(54, 10, 'Jodhpur')
cities.append(Jodhpur)

Jaisalmer = City(23, 62, 'Jaisalmer')
cities.append(Jaisalmer)

Kota = City(48, 20, 'Kota')
cities.append(Kota)



# Initializing a random path
path = random.sample(cities, len(cities))
distance = pathCost(path)

print('INITIAL ROUTE:')
for i in range(len(path)):
    print(path[i].name)
# Initial temperature
Temp = 1000
Max_Iteration = 1000

for i in range(1, Max_Iteration):
    
    r = random.sample(cities, len(cities))

    city1 = path.index(r[0])
    city2 = path.index(r[1])

    newRoute = path
    newRoute[city1] = r[1]
    newRoute[city2] = r[0]

    newDistance = pathCost(newRoute)

    # Difference in old path cost and new path cost

    diff = distance - newDistance
    T = Temp/i

    pE = 1/(1 + math.exp(-diff/T))

    if diff > 0:
        path = newRoute
    else:
        rand = random.uniform(0,1)

        if rand < pE:
            path = newRoute 

    Final_Distance = pathCost(path)
    Distance_Matrix = [distance, Final_Distance]
    Probability = pE


print("\n \nFINAL ROUTE:")
for i in range(len(path)):
    print(path[i].name)

print('\nINITIAL TOTAL DISTANCE, FINAL TOTAL DISTANCE:')  
print(Distance_Matrix)

print('\nPROBABILITY FUNCTION:')
print(pE)

    



