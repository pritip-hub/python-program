#example to apply conditions for licence

age=17
if(age>=18):
    print ("can apply for licence")
else:
    print("you can't apply for licence")


#example for traffic lights
light= input("enterthe signal you see: ")
if(light=="red"):
     print("stop")
elif(light=="green"):
     print("go")
elif(light== "yellow"):
    print("wait")
else:
    print("you are fool")

 #example of giving vote

if(age >= 18):
  print("i can give the vote")
else:
  print("i can't give the vote")

#example of student marksheet
mark= int(input("enter your mark: "))

if(mark >= 90):
    grade ="A"
elif(mark>=80 and mark< 90):
 grade= "B"
elif(mark >= 70 and mark < 80):
  grade ="c" 
elif(mark)
else:
   grade="future chai wala"
print ("grade of the student is - ",grade)


#list example
list= [45,67,34,90,76,32]
print(list)
print(type(list))
print(list[0])#45
print(list[1])#67
print(list[2])#34
print (len(list))#6

#mark example
marks=[32,76,98,67,56,90]
print(marks[1:5])#[76,98,67,56]
print(marks[3:5])
print(marks[:5])
print(marks[3:])

#example of list method

list= [2,1,3]
list.append(5)
print(list) # [2,1,3,5]
print(list.sort()) # is sorting for background of the list so that we can get the result none
print(list) # when we print the sorteds list so we can get the result of [1,2,3] [1,2,3,5]
print(list.sort(reverse=True)) # none
print(list) #[5,3,2,1]
print(list.reverse()) # none
print(list) # [1,2,3,5]
print(list.insert(1,4))
print(list) # [1,4,2,3,5]
list.pop(4)
print(list)#[1,4,2,3]