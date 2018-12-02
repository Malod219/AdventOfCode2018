with open("input.txt","r") as file:
	lines = file.readlines()
print(len(lines[0]))
print(len(lines))
idList = [[] for i in range(len(lines))]


# Totals up all the occurences of each character into a nice list to search
for count, line in enumerate(lines):
	for count2, character in enumerate(line):
		#print(character)
		idList[count].append(line.count(character))
#print(idList[0])

# Add up all times there is 3 letters or 2 letters
dosCount = 0
tresCount= 0

for boxID in idList:
	if 2 in boxID:
		dosCount  +=1
	if 3 in boxID:
		tresCount +=1
	print(str(boxID)+str(dosCount)+" "+str(tresCount))

print(dosCount * tresCount)
