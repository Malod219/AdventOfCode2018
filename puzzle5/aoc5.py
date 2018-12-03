with open("input.txt","r") as file:
    lines = file.readlines()

allIds = []
# Parsing the input data
for id,line in enumerate(lines):
    currentIdList = []
    currentIdList.append(id+1)
    line = line.split('@')
    line = line[1].split(':')
    coordinates = line[0].split(',')
    sizes = line[1].split('x')
    currentIdList.append(int(coordinates[0])+1)
    currentIdList.append(int(coordinates[1])+1)
    currentIdList.append(int(sizes[0]))
    currentIdList.append(int(sizes[1]))
    allIds.append(currentIdList)
# Drawing to the 1000x1000 canvas
canvas = [[0]*1100 for i in range(1100)]
for idList in allIds:
    x0 = idList[1]
    y0 = idList[2]
    x1 = idList[3]
    y1 = idList[4]
    for y in range(y1):
        for x in range(x1):
            try:
                if canvas[y+y0][x+x0]==0:
                    canvas[y+y0][x+x0]=1
                elif canvas[y+y0][x+x0]==1:
                    canvas[y+y0][x+x0]=2
            except:
                pass
# Counting Overlaps
overlaps=0
for row in canvas:
    for column in row:
        if column == 2:
            overlaps+=1
print(overlaps)
