from collections import deque

count_petrol_stations = int(input())
petrol_stations = deque()

for _ in range(count_petrol_stations):
    #On the next N lines, you will receive the amount of petrol that each petrol pump will give and the distance between that petrol pump and the next petrol pump, separated by a single space
    fuel, distance = [int(x) for x in input().split()]
    petrol_stations.append({'fuel': fuel, 'distance': distance})

start_position = 0
stops = 0

while stops < count_petrol_stations:
    curr_fuel = 0
    for i in range(count_petrol_stations):
        curr_fuel += petrol_stations[i]['fuel']
        dist = petrol_stations[i]['distance']
        if curr_fuel < dist:
            stops = 0
            petrol_stations.rotate(-1)
            start_position += 1
            break
        curr_fuel -= dist
        stops += 1

print(start_position)
        