class Account:
    def __init__(self,acc_no,acc_pass):
         self.acc_no=acc_no
         self._acc_pass =acc_pass
acc1=Account("12345","abcde")
print(acc1.acc_no)
print(acc1._acc_pass)




class Account:
    def __init__(self, acc_no, acc_pass):
          self.acc_no = acc_no # public attributes
          self._acc_pass= acc_pass #private attributes

    def reset_pass(self):
      print(self._acc_pass)

#we can't access private attributes or methods
#directly so we take a another method to pass these value and execute it.
acc1= Account("12345","abcde")
print(acc1.acc_no)
print(acc1.reset_pass())


class person:
  _name = "rohit" # private attribute


  def _hello(self): # private method print("hello person!")
      print("hello person!")
  def welcome(self): # a method to pass our private method self._hello()
      self._hello()


p1= person()
print(p1.welcome())

#hello person!





#multilevel inheritance

#carl= Toyota Car ("Fortuner")

#car2 =ToyotaCar ("Legender")

#print(car1.stop())

#print(car2.start())


class Car:

     @staticmethod # decorator
     def start():
         print("car strated..")

     @staticmethod #decorator
     def stop():
      print("car stopped..")

class ToyotaCar(Car):
   def __init__(self, name):
      self.name = name
car1=ToyotaCar("Fortuner")
car2= ToyotaCar("Legender")
print(car1.stop())
print(car2.start())




class Complex:
        def __init__(self, real, img):
         self.real= real
         self.img= img


        def showNumber(self): 
             print(self.real,"i +", self.img,"j")


        def __add__(self, num2): 
                newReal= self.real + num2.real 
                newImg =self.img +num2.img 
                return Complex(newReal, newImg)


num1 = Complex(1,3)
num1.showNumber()

num2 =Complex(4,6)
num2.showNumber()

num3=num1.add(num2)
num3.showNumber()