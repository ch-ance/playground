import time


times = []

def add_items():
	box = []
	for x in range(100000):
		box.append(x)

for i in range(2000):
	start_time = time.time()

	add_items()	

	end_time = time.time()
	total_time = end_time - start_time

	times.append(total_time)


running_total = 0

for time in times:
	running_total += time

average_time = running_total / len(times)

print(average_time)