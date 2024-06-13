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
list sort(reverse =True)-sorts the element in decending order-[98741]
list.reverse()-reversing the list-[18749]
list.insert(idx,el)-insert the element at index
list.remove(1)-remove  the ffirst occurance of element-[9,7,3,8,1]
list.pop(idx)-remove element at index
