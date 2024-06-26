class Student:
    name = "web bocket"

s1 = Student()
print(s1)#memory location where our s1 object will located.
print(s1.name)


s2 = Student()
print(s2.name)# web bocket

class Car:
    color="blue"
    brand="toyota"
car1 = Car()
print(car1.color)
print(car1.brand)


class Student:
    def __init__(self,fullname):
        self.name = fullname
        print("we can add a student in our database")

s1 = Student("web bocket")
print(s1.name)

s2 = Student("software")
print(s2.name)


class Student:
    #default Constructor
    def __init__(self):
        pass
    #parameterized constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks= marks
        print("adding new student to the database...")

s1=Student("web bocket",89)
print(s1.name,s1.marks)

s2= Student("software" ,98)
print(s2.name, s2.marks)


class Student:

    college_name ="ABC college"
    name = "anonymous"

    def __init__(self,name,marks):
        self.name=name#
        self.marks=marks
        print("adding new student to the DB")
s1=Student("rohan",98)
print(s1.name)

class Student:
     def __init__(self,name,marks):
         self.name=name
     def welcome (self):
         print("welcome student",self.name)
     def get_marks(self):
         print("your mark is",self.marks)


s1 =Student("rohan", 98)
s1.welcome()
s1.get_marks()