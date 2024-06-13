#str1="this is a good day"
#str2 ='This is beautyful day'
#str3 ="""this is abad day"""

gift ="this is a good day and will \n sleep whole day in my room."
print(gift)

#string concatenation ->
str1 = "web"
str2 = "bocket "
print (str1+str2) #webbocket

str3="raghab"
str4 = "dubay"
print(str3+str4)#raghabdubay



#length of String - >
str1="webbocket"
print (len(str1))#9

str1="coliege"
print(len(str1))#7


str1="web"
str2="bocket"
str3=str1+" "+str2
print(str3) #web bocket
print(len(str3)) #10

#Indexing of string ->
str= "gandhi engineering college"
print(str[1])
print(str[6])
print(str[13])

#slicing of String
str = "webbocket"
print(str[1:4]) #ebb
str ="gietcollege"
print(str[4:]) #college
print(str[:4]) #giet

str="i am a student from GIET college.GIET is a best college is the only one best  in odisha"
print(str.endswith("odisha"))#true
print(str.endswith("sha"))#true
print(str.endswith("GIET"))#false

print(str.capitalize())#first letter  of the first word shold be capital

print(str.replace ("GIET","GEC"))
print(str.replace("a","20"))


print(str.count("GIET"))#3 times