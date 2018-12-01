with open("input.txt","r") as file:
	lines = file.readlines()

counter = 0

for line in lines:
	counter += int(line)
print(counter)