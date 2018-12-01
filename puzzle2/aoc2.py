with open("input.txt","r") as file:
	lines = file.readlines()

counter = 0
counterList = []
cont = True
i = 0

def returnDupeFrequency(counter, counterList):
	cont = True
	for line in lines:
		counter += int(line)
		if counter in counterList:
			cont = False
			return (counter, counterList, cont)
		counterList.append(counter)
	return (counter, counterList, cont)
while(cont == True):
	i+=1
	counter, counterList, cont = returnDupeFrequency(counter, counterList)
	#print("Iteration " + str(i) + " passed")

print(counter)