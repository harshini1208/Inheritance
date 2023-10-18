#MULTIPLE INHERITENCE USING MORE THAN TWO CLASSES
class Car():
    def Benz(self):
        print("This is Benz car")
class Scooty():
    def Ather(self):
        print("This is a Ather scooty")
class Bus():
    def Volvo(self):
        print("This is volvo bus")
class Plane():
    def AirIndia(self):
        print("This is a AirIndia plane")
class Transport(Car,Scooty,Bus,Plane):
    def vehicle(self):
        print("This is the vehicle that i used")
v=Transport()
v.Benz()
v.Ather()
v.Volvo()
v.AirIndia()
v.vehicle()




