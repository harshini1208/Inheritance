# #from class method of child class.we can access instance methods  and constructors of parent class
# class Parent:
#     def __init__(self):
#         print("parent class constructor")
#     def m1(self):
#         print("parent class instance method")
# class Child(Parent):
#     @classmethod
#     def m2(cls):
#         super(Child,cls).__init__(cls)
#         super(Child,cls).m1(cls)
# s=Child()
# s.m2()


#how to use super() to access parent class from child class static method
class Parent:
    def __init__(self):
        print("parent class constructor")
    def m1(self):
        print("parent class instance method")
    @classmethod
    def m2(cls):
        print("Parent class method")
    @staticmethod
    def m3():
      print("parent class static  method")
class Child(Parent):
    @staticmethod
    def m4():
        # super().m1()  #not possible
        # super().m2()  #not possible
        # super().m3()   #not possible
        super(Child,Child).m3()    #parent class staticmethod can be accessed by child class static method
c=Child()
c.m4()

