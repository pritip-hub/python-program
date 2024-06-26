#example of abstraction

class Car:
    #parameterized constructor
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("car started...")
car1=Car()
car1.start()



#example of Encapsulation

#class Student:
 #   def _init_(self, name="rajesh", marks=50): 
  #      self.name = name 
        # self.marks = marks
#s1=Student()
##s2=Student("bharat",25)
#print("Name:{}marks: {}".format(s1.name, s1.marks))
#print("Name:{}marks: {}".format(s2.name, s2.marks))
    
#pratice question-
# -create account class with 2 attributes - balance & create  methods for debits,credits&printing the total balance.

class Account:
      def init_(self, bal, acc):
        self.balance = bal
        self.account = acc

      def debit(self, amount):
        self.balance =amount
        print("Rs.", amount, "was debited")
        print("total balance", self.get_balance())

      def credit(self, amount):
          self.balance = amount
          print("Rs.", amount, "was credited")
          print("total balance", self.get_balance())

      def get_balance(self):
           return self.balance

acc1 = Account (10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit (450000)
