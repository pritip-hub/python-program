

from logging import info


tup =(2,4,7,5,3,8)
print(type(tup))
print(tup[1])
print(tup[2])
print(tup)

tup =(1,)
print(tup)
print(type(tup))



tup1 =(1.0)
print(tup)
print(type(tup1))



tup =(3,5,7,8,5,2)
print(tup[1:4])
print(tup[3:])
print(tup[:4])


tup=(1,7,5,8,5,3)
print(tup.index(3))
print(tup.count(5))
print(tup[4])

dict ={
    "name":"priti",
    "learning":"coading",
    "age":22,
    "carrier":"good"
}
print(info)
print(info["name"])
print(info["carrier"])
print(info["age"])
print(type(info))

info["name"]="rajesh"
info["surname"]="sahoo"
print(info)#the property of mutable (its change their value)




student={
    "name":"priti"
    "subject" : {
       "java":{
           "core-java" :78,
           "adv-java" :89
       },
       "c++":67,
       "python":99
    }
}

print(student)
print(student["name"])
print(student["subject"]["python"])
print(student["subject"]["java"]["core-java"])


student1={
    "name":"Gudu",
    "subject":{
    "c++":67,
    "python":99
    }
}

print(info)
print(student1.keys())
print(student1["subject"].keys)
print(student1)



collection= {1,2,3,2,4,1,5, "hello", "world", "hello"}

print(collection)#{1,2,3,4,5,"hello","world"}
print(type(collection))#set
collection= set() #empty set
print(type(collection)) #set
collection =set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.remove(1)
collection.clear()
print(collection) #set()


collection1= {"hello", "rahul", "rajeev", "biswa", "world"}
print(collection1.pop())#randomly popout one element