-what is python ?
-python is simple,easy & portable.
-python is free & open sourse.
- python is high level, interpreted language.
- python was developed by Guido Van Rosum.


-python is interpreted language means whhen we write python code its 
executed the code line by line thats why we called python is 
interpreted language.


-print is function to give output statement in python.
simply we can tell "print" is output function.


character set of python language :-
1.letter ->A-Z,a-z
2.digit -> 0-9
3. special charecter -> -,+,/,* etc...
4. whitespace -> blank space ,tab ,newline



what is variable in python ?
- A variable is a name given to a memory location in a program or else we can simply 
say variable is a container to store some data.


Examples->
name ="pinki"
age=20
salary=20000

variable names - name,age,salary
variables  values -"pinki", 20,20000

rules for identifiers:--
1. identifiers -name of the variables
2. identifiers can be combination of uppercase and lowercase letter ,digits or an 
underscore(_).
 ex-myvariable,variable_1
3. an identifiers can not start with digit.so while variables is valid but 1variable in  not valiud.
4. we can not use special character or any symbol like # , @ , % , ! etc...
5. identifier can be any length.
6. variable name should be small and meaningfull like- when we give our age in that case we take variables as "myAge".

myAge -> camel case letter


"type" is a operator to show the datatype name in our variables li9ke which datatypes we use in our variables.


Data Types :--
- mainly datatypes of 5 types in python.
- Thease data types are unmutable or  build-in data types.
1. Integer - +ve value , 0 , -ve value 
2. String -  "hello", "pinki" , etc..
3. Float - 3.14 , 7.89 , 9.1 etc...
4. Boolean - True, False
5. None - not assign

comments in python:-

 -When we write some code but we dont want to execute it then we give the comment line to that place so that line of code will not executed.
 -comments are of two type .
 1. Single line  comment -
    When we give the single line comments. in python we did it on "#".
    ex.
    # single line comment 
    # this is a comment
 2. Multi line comment
    When we gi ve multi line comment 
ex.
"""
multi line
comments
"""


Types of operator:-
- simply we can say operator is a symbol that performs a certain operation between operands.
ex. a + b
    a,b -> operands
    + -> operator
- there are 4 types of operator are present in python
1. arithmatic operator. -(+,-,/,%,*)    
2. relational operator. - (==,!=,> ,<,>=,<=)
3. assignment operator. -(=,+=,-=,*=,/=,%=)
4. logical operator -(and,or,not)


Input in Python:-
- Input() statement is used to accept values (use keyword) from users.

Task to do for practice-

 1. write program to input 2 numbers & print their sum
 2. Write a program to input side of a square & print its area.
 3. write a program to input 2 floating point numbers & print their average.

 4. write a program to input 2 int numbers a & b, print True if a is greater then or equal to if not print false.


Strings:-

-String is a datatype that stores a sequence of characters.

str1="this is a good day"
str2='This is beautyful day'
str3="""this is a bad day"""

-all the strings are real string because in python ,it supports all of these syntax like-" " ,' ',""" """

-\n (new line ) - when we want to break our line a new line we can give the new line symbol in that place so the line get breaked automatically.

Basic operations of Strings: -
1. concatenation - >
"hello" +"world"=
2. length of String ->
len(str)


Indexing of string ->

- webbocket -> 012345678(indexing)
- Always indexing start from '0'.


Slicing of string ->

-Accessing parts of a string.
-syntax str[starting_index ending_index]
str = "webbocket"
str[0:3] - web
str[:3]- web
str[3:] - bocket



Functions of string ->

ex-

str= "i am a coder."

1. str.endswith("er.") - returns true if string ends with substring

2. str.capitalize() -  returns 1st char is capital

3. str.replace(old, new) -  replace all occurances of old with new

4. str.find(word) -  returns 1st index of 1st occurrence

5. str.count("am")  - counts the occurrence of substring in string



Homework:-
1. Write a program to input users first name & print its length.
2. Write a program to find the occerrence of '$' in a string.









Homework:-
1. Write a program to check if a number entered by the user if odd or even.
2. write a program to find the greatest of 3 numbers entered by the userd.
3. write a program to check if a number is multiple of 7 or not.


lists in python:-
- lists is a built -in data type that stores set of values.
it can store elements of different types like integer, float& string etc....
in list we can make indexing.
in list we can find length of the list else.
in list we can also do the slicing activity.

ex-
marks= [87,45,67,83,45]- array and list
student= ["hitesh",85,"bhubaneswar"] - list

list slicing:-
 it similarly to string slicing.
syntax :- list name [starting_idx ; ending_idx]
ending index is not included.

mark=[23,25,67,78,98]
marks[1:4] ->[25,67,78]
marks[:3] ->[23,25,67]
marks[]



list methods:-

list=[9,4,7,8,1]
list .append(6)-sadds one element at the end of the list -[9,4,7,8,1,6]
list.sort()=sort the element in assending order-[1,4,7,8,9]
list sort(reverse =True)-sorts the element in decending order-[9,8,7,4,1]
list.reverse()-reversing the list-[1,8,7,4,9]
list.insert(idx,el)-insert the element at index
list.remove(1)-remove  the ffirst occurance of element-[9,7,3,8,1]
list.pop(idx)-remove element at index


git:-
-  git is a open source repository system where we can save ,manipulate,colaborate our code with any one else.
-  in our software era ,everyone can use git system for their software development.
- we also called git is a version control system.
- git provides some tools to use their functionallity and features ex -github,gitlab,etc....



Tuple in Python:-

Tuple is a build in data type that lets us create immutable(the value can't be changeble) sequence of values.
ex. tup (87,67,98,34,45)
tup[8] -> 87
tup[1] -> 67
we can do the tuple as
1. tupl()-> empty tuple
2. tup2 (1) a tuple
3. tup3 (34,67,89,20)-> tuple
tuple has also satisfy the slicing propety.

tuple methods:-

tup.index(element) -> returns index of first occurrence

tup.count(element) ->returns the count total occurrence

ex. tup= (2,1,3,1)

tup.index(1) -> 1
tup.count(1) -> 2

homework:-
1. write a program to ask the user

dictionary in python:

- dictionary are used to store the data values in key :value pair
- they are uderscored,mutable(changeable)& don't allow duplicate keys.
- ex.
dict = {
    "name" : "shradha"
    "cgpa" : 9,8,
    "marks" :[98,96,95]
}
- the left part of the dictionary are keys and right side part in their values so dictionary contains key:value pair structure.



Nested dictionary in python:-
- dictionary also satisfy the nested property.
- Dictionary under dictionary is called nested dictionary.
- ex.
student={
    "name" :"mithum"
    "score":{
        "chem":98,
        "math":87,
        "phy":74
    }
}

Dictionary methods:-

1. myDict.keys()
2. myDict.keys()
myDict.keys()
myDict.keys()
myDict.update(newDict)- insert the specified items to the dictionary.

set in python:-

- set is Che collection of the unordered items.
- Each element in the set must be unique & immutable (can't change).
ex.
nums = {1,2,3,4,5}
set2= {5,8,9,4}

set method :-

1. set.add(element) -> adds an element
2. set.remove(element) -> remove an element
3. set.clear() -> clear all elements
4. set.pop() -> remove a random value of set
5. set.union(set2) -> combine both set values & returns a new set
6. set.intersection(set2) -> combines the common value & returns a new set.
ex.
set1 = {1,2,3,2,4}
set2 =(3,7,2,6,4)
set1.union(set2) -> {1,2,3,4,6,7}
set1 intersection(set2)-> {2,3,4}


Loops in python:-
- Loops are used to repeat instruction.
- In python there are 2 loops - while loop,for loop
1. while loop:-
syntax_
initialization
while condition:
   statement
   increment/decrement


   range() :-
   - range function returns a sequence of numbers,starting from 0by defaults,and increaments by 1(by default),and stops before a specified number.



   function:

   - function is a block of statements that performs a specific task.
   - syntax :-
   def func_name(parameter 1, parameter 2...)
   some statement
   returns val
   func-name(arg1,arg2...)#function call
   
   - functions are of 2 types in python
   1. built-in-function-print(),len(),type(),range().........
   2. user defied function -user can develop the function.


   write a function to print the length of a list(list is the parameter)

2. write a function to print the element of a list in a single line(list is the paraneter)

3. write a function to find the factorial of n (n is the parameter)

factorial means

suppose i want to get the factorial of 5,

syntax of factorial -> n! 1*2*3... n (n-1)


4. write a function to convert USD to INR.




object oriented programming in python:-

- To map  with real world scenarios,we started using objects in code.this is called object oriented programming(oop).

1st concept->
2nd concept->
3rd concept->

class & object in python:-

- class is a blue print for creating objects.
ex. -> creating a class
class student:
      name="web bocket"

 ex. - creating a object(instance)
 s1 =Student()
    print(s1.name)

constructor:-
__init__function (constructor):-
- All class have a function called__init__(), which is always executed when the class is being initiated.

ex. -> creating a class
class Student:
    def__init__(self,fullname):
    self.name=fullname

ex.->creating a objects1= student("web bocket")
print(s1.name)

note: The self parameter is a reference to the current instance of the class ,and is used to access variable that belongs to the class.


class & instance Atributes :-
university -> college1,college2,
              student1

 
 methods in python:-
 - methods are function that belongs to objects.

 ex. ->creating class
 class Student:
     def__init__(self,fullname):
         self.name=fullname
    def hello (self):
         print("hello",self.name)

  ex.>creating object
  s1 =Student("rohan", 98)
  s1.hello()



  abstraction:
hiding the impl

  encapsulation:-
  wrapping data and function into a single unit(object).



Private(like) Attributes & Methods:

- private attributes & methods are accessible from outside the class. anly within the class and
the private class attrioutes are written in (attributes) attributes of a class, that call it private.


Inheritance :-
when one class (child class) derives the properties & methods of another class (parent class).
syntax :- class car:
      ------------
class ToyotaCar(car):
      ------------
in python inheritance are of 3 types. I
      ------------
1. single inheritance

2. Multi-level inheritance

3. Multiple inheritance



polymorphism:operator overloading:-

- when the same operator is allowed to have different meaning accordingly to the context.
- in that polymorphism we can use under functions.
1. a+b->__add__
2.a-b->__sub__
__mul__
__truediv__
__mod__

ex-(+)
print(1+2)