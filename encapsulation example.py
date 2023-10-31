class Udemy():
    def __init__(self):
        self.course="PYTHON PROGRAMMING COURSE"
        self.technology="Python"
        self.__framework="Django"
    def CourseName(self):
        return self.course+self.technology+self.__framework
c=Udemy()
print(c.course)
print(c.technology)
print(c._Udemy__framework)
print(c.CourseName)