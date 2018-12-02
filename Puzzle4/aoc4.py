# Load in the input
with open("input.txt","r") as file:
	lines = file.readlines()

importantLines=[]

# This is to find the 2 lines which have a 1 character difference
for line in lines:
	for line2 in lines:
		comparison=[i for i in range(len(line)) if line[i] != line2[i]]
		if (len(comparison)==1):
			importantLines.append(line[:-1])
			importantLines.append(line2[:-1])
			break
	if (len(importantLines)>0):
		break

# This is to remove the difference between the 2 lines
finalAnswer=""
for i in range(len(importantLines[0])):
	if importantLines[0][i]==importantLines[1][i]:
		finalAnswer += importantLines[0][i]
print(finalAnswer)
