import math
import random
import copy
import time
import sys

'''
Point class. property of xPos and yPos represent the coordinate of pick up and drop off positions, id, identify which package
it belongs
'''
class Point:
    def __init__(self):
        self.xPos = 0
        self.yPos = 0
        self.id = 0

    def getParrent(self):
        for p in packages:
            if p.id == self.id:
                return p

'''
Package class. every package has a source coordinate, destiniation coordinate, if currentPos == dest then delivered is True
if the package is on vehicle then this.currentPos = cvehicle.currentPos, id, identify which pakckage it is
'''
class Package:
    def __init__(self):
        self.sours = Point
        self.dest = Point
        self.currentPos = Point
        self.onCar = False
        self.delivered = False
        self.id = 0
'''
sours and dest is always the garage's position for every vehicle, currentPos update when called goPick or goDrop
packages contain lists of packages current on car, history is the points this vehicle traveled, history_id is 
the package of those points
'''
class Vehicle:
    def __init__(self):
        self.sours = Point
        self.dest = Point
        self.currentPos = Point
        self.hasPackage = False
        self.packages = []
        self.numOfPackages = len(self.packages)
        '''
        keep track of where did the car went, and how many distance it traveled
        '''
        self.distanceTraveled = 0
        self.history = []
        self.history_id = []
        self.id = 0


''''
compute distance of two points
'''
def distanceOfPoints(self, point):
    dis = math.sqrt((point.xPos - self.xPos) ** 2 + (point.yPos - self.yPos) ** 2)
    return dis




'''
find the nearst pick point from garage, only called when start
'''
def car_start_point():
    minDis = 9999
    packageToPick = Package
    for p in packages:
        if p.onCar == False:
            dist = distanceOfPoints(car.currentPos, p.sours)
            if dist < minDis and dist != 0:
                minDis = dist
                packageToPick = p

    return packageToPick

'''
find the next point to go, return the package of that point
'''
def car_continue_point():
    minDis = 9999
    packageToPick = Package
    for p in points:
        dis = distanceOfPoints(car.currentPos,p)
        if dis < minDis and dis!=0:
            minDis = dis
            packageToPick = p.getParrent()
    return packageToPick

'''
create the problem state
'''
def create(vehicle,packageNum):
    cars = []
    packages = []
    points = []
    for i in range(0,vehicle):
        car = Vehicle()
        car.sours = garage
        car.dest = garage
        cars.append(car)
        car.currentPos = garage
        car.id = i+1

    for i in range(0,packageNum):
        pac = Package()

        pick = Point()
        pick.xPos = random.randint(0,50)
        pick.yPos = random.randint(1,50)
        pick.id = i
        drop = Point()
        drop.xPos = random.randint(0,50)
        drop.yPos = random.randint(0,50)
        drop.id = i
        points.append(pick)
        points.append(drop)

        pac.sours = pick
        pac.dest = drop
        pac.id = i
        packages.append(pac)

    return cars,packages,points

longest_dis = 0

'''
go pick up the package with vehicle 
'''
def goPickUp(car,package):
    print("Picked up package number ",package.id)
    car.distanceTraveled += distanceOfPoints(car.currentPos,package.sours)
    car.currentPos = package.sours
    car.packages.append(package)
    car.hasPackage = True
    car.numOfPackages = len(car.packages)
    package.currentPos = car.currentPos
    package.onCar = True
    car.history.append(package.sours)
    car.history_id.append(package)
    for po in points:
        if po == package.sours:
            points.remove(po)
deliveried = 0

'''
go drop the package with vehicle
'''
def goDrop(car,package):
    global deliveried
    deliveried +=1
    car.distanceTraveled += distanceOfPoints(car.currentPos,package.dest)
    car.currentPos = package.dest
    print("Dropping package number ", package.id, "                   Number of deliveried package: ",deliveried)
    car.packages.remove(package)

    car.numOfPackages = len(car.packages)
    if car.numOfPackages < 1:
        car.hasPackage = False
    package.currentPos = car.currentPos
    package.onCar = False
    car.history.append(package.dest)
    car.history_id.append(package)
    for po in points:
        if po == package.dest:
            points.remove(po)



'''
compare cost of send current car back to garage and send another car to next point and cost of go to next point with
current car and back to garage. If send another car is cheaper, then send another car and send current vehicle back
to garage, else, let current vehicle pick the next package
'''

def search(vehicle,packageToPick):
    for p in packages:
        if p == packageToPick:
            if p.onCar == False:


                localLong = 0
                if vehicle.distanceTraveled + disPickNextThenBacktoGarage(vehicle,p) > longest():
                    longest1=vehicle.distanceTraveled + disPickNextThenBacktoGarage(vehicle,p)
                else:
                    longest1 = longest()
                distanceForCurrentCars = vehicle.distanceTraveled + disPickNextThenBacktoGarage(vehicle,p)+longest1
                distanceForAnotherCarToNextPoint = distanceOfPoints(garage,p.sours)+distanceOfPoints(p.sours,p.dest)+distanceOfPoints(p.dest,garage)

                if distanceForAnotherCarToNextPoint > longest():
                    localLong = distanceForAnotherCarToNextPoint
                else:
                    localLong = longest()
                distanceForAnotherCar =vehicle.distanceTraveled+disBackToGarage(vehicle) +distanceForAnotherCarToNextPoint+ localLong
                if distanceForCurrentCars < distanceForAnotherCar or car.id==len(cars) and len(car.packages)<limit:
                    goPickUp(car,p)
                elif car.id<len(cars) :
                    print("Need another vehicle!")
                    goBackToGarage(vehicle)
                    sendAnotherCar(vehicle)

            else:
                goDrop(car,p)
    for p in car.packages:
        p.currentPos = car.currentPos
cccars=[]
carCount=1

'''
send another car, append current car to cccars, and set vehicle's history,distancetraveled to initial value
'''
def sendAnotherCar(vehicle):

    global carCount
    carCount+=1
    print("Active Another Vehicle! ")
    thiscar = copy.deepcopy(vehicle)
    cccars.append(thiscar)
    vehicle.history=[]
    vehicle.history_id=[]
    vehicle.distanceTraveled = 0
    vehicle.id = carCount

'''
compute the distance of pick the package and then delivery every packages current on the vehicle then back to garage
(but not fully implemented, so jsut find the farthest drop point, then compute the distance from current position PLUS
the distance from farthest drop point to garage)
'''
def disPickNextThenBacktoGarage(car,package):
    distanceOfPoints(car.currentPos,package.sours)

    maximum = 0
    point = Point()
    '''
    find the farest drop point from garage
    '''
    for p in car.packages:
        if distanceOfPoints(garage, p.dest) > maximum:
            maximum = distanceOfPoints(garage, p.dest)
            point = p.dest
    if distanceOfPoints(garage,package.dest) > maximum:
        point = package.dest

    estimateDis = distanceOfPoints(car.currentPos,package.sours) + distanceOfPoints(point,garage)
    return disBackToGarage(car)

'''
compute the distance of delivery every packages current on the vehicle then backto garage
'''
def disBackToGarage(vehicle):
    maximum = 0
    point = Point()
    '''
    find the farest drop point from garage
    '''
    for p in car.packages:
        if distanceOfPoints(garage,p.dest) > maximum:
            maximum = distanceOfPoints(garage,p.dest)
            point = p.dest

    estimateDis = distanceOfPoints(vehicle.currentPos,point) + distanceOfPoints(point,garage)

    return estimateDis

'''
Current vehicle delivery every packages on it
'''

def goBackToGarage(car):
    maximum = 0
    point = Point()
    '''
    find the farest drop point
    '''
    for p in car.packages:
        if distanceOfPoints(car.currentPos, p.dest) > maximum:
            maximum = distanceOfPoints(car.currentPos, p.dest)
            point = p.dest
    goDrop(car,point.getParrent())
    print("Dropping package number ", point.getParrent().id)
    pointNow = Point()
    while car.hasPackage:
        minDis = 9999

        for p in car.packages:
            if (p.sours != car.currentPos and p.dest!= car.currentPos):
                if distanceOfPoints(car.currentPos, p.dest) < minDis:
                    minDis = distanceOfPoints(car.currentPos, p.dest)
                    pointNow = p.dest

        goDrop(car, pointNow.getParrent())

    car.distanceTraveled += distanceOfPoints(car.currentPos,garage)
    car.currentPos = garage
    print("----------------------------------------------\n ----Vehicle #",car.id,"back to garage, Vehicle #",car.id+1,"is out for delivery")

'''
print how many vehicles were used
'''

def vehicleUsed():
    return len(cccars)

'''
print total distance traveled
'''
def totalDistanceTraveledForAllVehicles():
    dis = 0
    for car in cccars:
        dis = dis + car.distanceTraveled
    return dis

'''
print the longest single vehicle traveled
'''
def longest():
    maximum = 0
    for car in cccars:
        if car.distanceTraveled>maximum:
            maximum = car.distanceTraveled
    return maximum







'''
position of garage
'''
garage = Point()
garage.xPos = 0
garage.yPos = 0

'''
total_distance
'''
total = 0

v = int(input("How many vehicles: "))
p = int(input("How many packages:"))
limit = int(input("How many packages can each vehicle carry?"))
if v*limit < p:
    sys.exit("Number of vehicles * vehicle carry limit  must >= numer of packages!")
start_time = time.time()
cars, packages, points = create(v, p)

count=0
car = cars[count]
for p in packages:
    print(p.id, "'s  picking x and y pos: ", p.sours.xPos, p.sours.yPos)
    print(p.id, "'s  dropping x and y pos: ", p.dest.xPos, p.dest.yPos)

print("-------------------------------------------------------------------------")
print("Start: \n")
package4 = car_start_point()
search(car, package4)


while len(points) > 0:
    package2 = car_continue_point()
    search(car, package2)


if len(points) == 0:
    total = total + distanceOfPoints(car.currentPos,garage)
    car.distanceTraveled += distanceOfPoints(car.currentPos,garage)
    car.currentPos = garage
    cccars.append(car)
    print("FINISHED!!!")


print("Vehicle used:", vehicleUsed())
print("totaldistanceforall:", totalDistanceTraveledForAllVehicles())
print("longest:",longest())
for car in cccars:
    print("The vehicle # ",car.id,"traveled: ", car.distanceTraveled)
    print("The vehicle #",car.id,"'s Path: ")
    for package in car.history_id:
        print(package.id , "->")

print("Time used: ", time.time()-start_time)