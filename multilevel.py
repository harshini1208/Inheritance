class Branch:
    def get_bdata(self):
        self.bcode=int(input("enter branch code:"))
        self.bname=input("enter branch name:")
        self.baddress=input("enter branch address")
    def display_bdata(self):
        print("branch code is :",self.bcode)
        print("branch name is :",self.bname)
        print("branch address is:",self.baddress)
class Employee(Branch):
    def get_empdata(self):
        self.eid=int(input("enter emp Id:"))
        self.ename=input("enter emp name:")
        self.eaddress=input("enter emp address")
    def display_empdata(self):
        print("empid is:",self.eid)
        print("empname is:", self.ename)
        print("empaddress is:", self.eaddress)
class empsalary(Employee):
    def getsal(self):
        self.basic=float(input("enter basic salary:"))
    def calculate(self):
        self.DA=0.04*self.basic
        self.HRA=0.6*self.basic
        self.gross=self.basic+self.DA+self.HRA
    def displaysal(self):
        print("basic salary is:",self.basic)
        print("DA is :",self.DA)
        print("HRA is:",self.HRA)
        print("Gross salary is:",self.gross)
e=empsalary()
e.get_empdata()
e.display_empdata()
e.getsal()
e.calculate()
e.displaysal()

