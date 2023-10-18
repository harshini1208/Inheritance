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
e=Employee()
e.get_bdata()
e.get_empdata()
e.display_bdata()
e.display_empdata()

