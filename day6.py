Instructions = []

with open('day6input.txt', 'r') as data:
    for line in data:
        data3 = line.replace("\n","")
        Instructions.append(data3)

#print(Instructions)

##VisitedNodes = {}
##while len(Instructions) > 0:
##    for item in Instructions:
##        #print("Evaluating : " + str(item))
##        content = item.split(")")
##        if len(VisitedNodes) == 0:
##            if content[0] == "COM":
##                VisitedNodes = {str(content[0]) : {"orbits" : 0}, str(content[1]) : {"orbits" : 1}}
##            else:
##                pass
##        else:
##            Nodekeys = VisitedNodes.keys()
##            if str(content[0]) not in Nodekeys:
##                pass
##            else:
##                checker = VisitedNodes[str(content[0])]
##                data = checker.get("orbits")
##                VisitedNodes[str(content[1])] = {"orbits" : data + 1}                
##                Instructions.remove(item)
##
##GrandTotal = 0
##for Location in VisitedNodes:
##    x = VisitedNodes[Location]["orbits"]
##    GrandTotal = GrandTotal + x
##print(VisitedNodes)
##print("The total number of orbits is : " + str(GrandTotal))


#####################part 2############################
Search1 = "YOU"
Storage1 = []
Search2 = "SAN"
Storage2 = []
x = 0
y = 0
while x == 0:
    for item in Instructions:
        #print("Evaluating : " + str(item) + "   - Comparing to : " + str(Search1))
        content = item.split(")")
        if content[0] == "COM" and content[1] == Search1:
            Storage1.append("COM")
            x = 1
        elif content[1] == Search1:
            Storage1.append(content[0])
            Search1 = str(content[0])
print("Path from COM to YOU  : " + str(Storage1))
while y == 0:
    for item in Instructions:
        #print("Evaluating : " + str(item) + "   - Comparing to : " + str(Search1))
        content = item.split(")")
        if content[0] == "COM" and content[1] == Search2:
            Storage2.append("COM")
            y = 1
        elif content[1] == Search2:
            Storage2.append(content[0])
            Search2 = str(content[0])
print("Path from COM to SAN : " + str(Storage2))
SharedObj = []
for e in Storage1:
    if e in Storage2:
        SharedObj.append(e)
    else:
        pass
print("Shared objects : " +str(SharedObj))
orbitleaps = []
for obj in SharedObj:
    r1 = Storage1.index(obj)
    r2 = Storage2.index(obj)
    r3 = int(r1) + int(r2)
    orbitleaps.append(r3)
print("Leaps required : "+str(orbitleaps))
print("Minimum Leaps Required : " + str(min(orbitleaps)))

