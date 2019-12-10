Field = []

with open ('FieldData.txt','r') as FieldData:
    for line in FieldData:
        data1 = line.replace("\n","")
        data2 = data1.replace("#","A")
        Field.append(data2)

FieldDict = {} #Represents Locations of Asteroids
pointDict = {} #Represents Number of Asteroids that can be detected from a point
#print(Field)
for item in Field:
    x = 0
    for char in item:
        if char == ".":
            x = x + 1
        else:
            #print(char)
            Coords = (x,Field.index(item))
            FieldDict[Coords] = char
            #print(Coords)
            x = x + 1
print(FieldDict)
##Test = (3,3)
##if Test in FieldDict.keys():
##    print("Yes")

for point in FieldDict.keys():
    Grads = []
    GradDict = {}
    for comparePoint in FieldDict.keys():
        if comparePoint == point:
            pass
        else:
            if (point[0] - comparePoint[0]) == 0:
                if point[1] > comparePoint [1]:
                    Gradient = "Infinity"
                else:
                    Gradient = "-Infinity"
            else:
                Gradient = (point[1] - comparePoint[1]) / (point[0] - comparePoint[0])
            #print("Gradient for point " + str(point) + " compared to " + str(comparePoint) + " : " + str(Gradient))
            if Gradient in Grads:
                #print("Duplicate Gradient found - " + str(Gradient) + " - point " + str(comparePoint))
                if Gradient == 0:
                    check1 = GradDict.get(Gradient)
                    if str(Gradient) == "-0.0":
                        check2 = check1.get('Negative')
                        if check2 == 1:
                            pass
                        if check2 == 0:
                            Grads.append(Gradient)
                            GradDict[Gradient]['Negative'] = 1
                    else:
                        check2 = check1.get('Positive')
                        if check2 == 1:
                            pass
                        if check2 == 0:
                            Grads.append(Gradient)
                            GradDict[Gradient]['Positive'] = 1
                        
                elif (point[0] - comparePoint[0]) > 0:
                    check1 = GradDict.get(Gradient)
                    check2 = check1.get('Positive')
                    if check2 == 1:
                        pass
                    if check2 == 0:
                        Grads.append(Gradient)
                        GradDict[Gradient]['Positive'] = 1
                elif (point[0] - comparePoint[0]) < 0:
                    check1 = GradDict.get(Gradient)
                    check2 = check1.get('Negative')
                    if check2 == 1:
                        pass
                    if check2 == 0:
                        Grads.append(Gradient)
                        GradDict[Gradient]['Negative'] = 1
                    
            else:
                if (point[0] - comparePoint[0]) > 0:
                    GradDict[Gradient] = {'Positive' : 1, 'Negative': 0}
                elif (point[0] - comparePoint[0]) < 0:
                    GradDict[Gradient] = {'Positive' : 0, 'Negative': 1}
                elif (point[0] - comparePoint[0]) == 0:
                    if str(Gradient) == "-0.0":
                        GradDict[Gradient] = {'Positive' : 0, 'Negative': 1}
                    if str(Gradient) == "0.0":
                        GradDict[Gradient] = {'Positive' : 1, 'Negative': 0}
                Grads.append(Gradient)

    print("Total number of Asteroids for point " + str(point) + " : " + str(len(Grads)))
    pointDict[point] = len(Grads)
print(pointDict)
BestValue = max(pointDict.values())
for Location, value in pointDict.items():
    if value == BestValue:
        print("Best Location : " + str(Location) + " - " + str(BestValue) + " asteroids detected")

