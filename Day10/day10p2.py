import math
#Best Location : (13, 17) - 269 asteroids detected <- Answer from p1
Field = []
Base = (13,17)
with open ('FieldData.txt','r') as FieldData:
    for line in FieldData:
        data1 = line.replace("\n","")
        data2 = data1.replace("#","A")
        Field.append(data2)
FieldDict = {} #Represents Locations of Asteroids
pointDict = {} #Represents Location/Distance/Gradiant/Shared (Points with same Gradient)
#print(Field)
for item in Field:
    x = 0
    for char in item:
        if char == ".":
            x = x + 1
        else:
            Coords = (x,Field.index(item))
            FieldDict[Coords] = char
            x = x + 1

RemainingAstroids = [x for x in FieldDict.keys()]
#print(RemainingAstroids)
RemainingAstroids.remove(Base)
for point in FieldDict.keys():
    HomePoint = Base
    if point == HomePoint:
        pass
    else:
        if (point[0] - HomePoint[0]) == 0:
            if point[1] > HomePoint[1]:
                Gradient = 9999999999
            else:
                Gradient = -999999999
        else:
            Gradient = (point[1] - HomePoint[1]) / (point[0] - HomePoint[0])
    Distancex =(point[0]-HomePoint[0])**2
    Distancey = (point[1]-HomePoint[1])**2
    Distance = math.sqrt(Distancex + Distancey)
    pointDict[point] = {"Distance" : Distance, "Gradient" : Gradient}

#Next step is to use pointDict to have an ordered list.
def Sort(sublist):
    sublist.sort(key = lambda x: x[1])
    return sublist
GradList = []
finalList = []
for element in pointDict:
    pointList = []
    Grad = pointDict[element]["Gradient"]
    GradList.append(Grad)
    for Location, value in pointDict.items():
        if value["Gradient"] == Grad:
            pointList.append(Location)
    #print(str(pointList) + " List for element " + str(element))
    Sorting = []
    for Point in pointList:
        Dist = pointDict[Point]["Distance"]
        Toople = (Point, Dist)
        Sorting.append(Toople)
    SortedList = Sort(Sorting)
    SortedList2 = []
    for obj in SortedList:
        Loc = obj[0]
        SortedList2.append(Loc)
    finalList.append(SortedList2)
    pointDict[element].update({'Shared' : SortedList2})#By here, all the points that have same gradient are ordered by distance
#print(pointDict)
      
GradList = list(set(GradList))
GradList.sort(reverse=False)
#print(GradList)
KillCount = 0
def Arc1():
    for x in range(0,len(GradList)):
        CurrentLaser = GradList[x]
        PointSearch = (0,0)
        SharedPoints = []
        PointDistance = 0
        for Point, value in pointDict.items():
            if value["Gradient"] == CurrentLaser:
                PointSearch = Point
                SharedPoints = value["Shared"]
                PointDistance = value["Distance"]
        #print("Aiming Laser at " + str(PointSearch) + "    Distance : " + str(PointDistance) + "   Points in-line : " + str(SharedPoints))
        MinimumDist = 9999999
        MinimumTarg = (999,999)
        for target in SharedPoints:
            if target not in RemainingAstroids:
                pass
            elif target[0] >= Base[0]:
                TestDistance = pointDict[target]["Distance"]
                if TestDistance < MinimumDist:
                    MinimumDist = TestDistance
                    MinimumTarg = target
            else:
                pass
        if MinimumTarg == (999,999):
            x = x + 1
        else:
            global KillCount
            KillCount = KillCount + 1
            print("Laser Destroying Asteroid #"+str(KillCount)+ " at point : " +str(MinimumTarg))
            RemainingAstroids.remove(MinimumTarg)
            x = x + 1
    print("Arc Complete")

def Arc2():
    for x in range(1,len(GradList)): #Starts at 1 to avoid double-fire from Arc1
        CurrentLaser = GradList[x]
        PointSearch = (0,0)
        SharedPoints = []
        PointDistance = 0
        for Point, value in pointDict.items():
            if value["Gradient"] == CurrentLaser:
                PointSearch = Point
                SharedPoints = value["Shared"]
                PointDistance = value["Distance"]
        #print("Aiming Laser at " + str(PointSearch) + "    Distance : " + str(PointDistance) + "   Points in-line : " + str(SharedPoints))
        MinimumDist = 9999999
        MinimumTarg = (999,999)
        for target in SharedPoints:
            if target not in RemainingAstroids:
                pass
            elif target[0] <= Base[0]:
                TestDistance = pointDict[target]["Distance"]
                if TestDistance < MinimumDist:
                    MinimumDist = TestDistance
                    MinimumTarg = target
            else:
                pass
        if MinimumTarg == (999,999):
            x = x + 1
        else:
            global KillCount
            KillCount = KillCount + 1
            print("Laser Destroying Asteroid #"+str(KillCount)+ " at point : " +str(MinimumTarg))
            RemainingAstroids.remove(MinimumTarg)
            x = x + 1

Arc1()
Arc2()
#if 200 not destroyed add more cycles of Arc1() followed by Arc2()

#Functions only split up to resolve a problem of when checking for the closest astroid on a given gradient,
#There was a chance the closest was 180 degrees from the direction of the lazer. 
        
