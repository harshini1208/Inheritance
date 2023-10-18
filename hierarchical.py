#HIERARCHICAL INHERITANCE
class Brands:               #parent class
 def __init__(self,site_1,site_2,site_3):
  self.site_1=site_3
  self.site_2=site_2
  self.site_3=site_1
 def Sites(self):
  print("These are Famous Sites",self.site_1,self.site_2,self.site_3)

class Products(Brands):     #child class1
 def __init__(self,product_1,product_2,product_3):
  self.product_1=product_1
  self.product_2=product_2
  self.product_3=product_3
 def Shop(self):
  print("Happy Shopping",self.product_1,self.product_2,self.product_3)
class Value(Brands):      #childclass2
  def __init__(self,item_1_value,item_2_value,item_3_value):
    self.item_1_value=item_1_value
    self.item_2_value=item_2_value
    self.item_3_value=item_3_value
  def Discount(self):
   print("Festive season discount",self.item_1_value,self.item_2_value,self.item_3_value)
c1=Products("Zara","H&M","Soch")                                               #object creation
c1.Shop()
c2=Value("20%","30%","40%")
c2.Discount()
c3=Brands("Amazon","Myntra","Flipkart")
c3.Sites()




