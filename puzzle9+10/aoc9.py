line = open("input.txt").read().splitlines()[0]
# Part1
oldline = None
while oldline != line:
    oldline = line
    for i in range(0,26):
        line = line.replace(chr(ord("a") + i) + chr(ord("A") + i),"")
        line = line.replace(chr(ord("A") + i) + chr(ord("a") + i),"")

print(len(line))
#Part2
line = line = open("input.txt").read().splitlines()[0]

best = len(line)
for i in range(0,26):
    line = open("input.txt").read().splitlines()[0]
    line = line.replace(chr(ord("a") + i),"").replace(chr(ord("A") + i),"")
    while oldline != line:
        oldline = line
        for i in range(0,26):
            line = line.replace(chr(ord("a") + i) + chr(ord("A") + i),"")
            line = line.replace(chr(ord("A") + i) + chr(ord("a") + i),"")
            if len(line)<best:
                best=len(line)

print(best)