#-------------------------------------------------------------------------------------------------------------
#day10 Dictionaries
#-------------------------------------------------------------------------------------------------------------

#1. Create and Access

student={
  "name":"Ram",
  "age": 19,
  "city": "Chennai"
}
print(student["name"])
print(student["age"])
print(student["city"])

#---------------------------------------------------------------------------------------------------------------

#2.add and update 

student={
  "name":"Sammy",
  "age": 49,
}
#adding new key
student["city"]="Hyderabad"
print("After adding a new key:", student)
#updating existing value
student["age"]= 20
print("after updating:", student)

#-----------------------------------------------------------------------------------------------------------------

#3.deleting

student={
  "name":"Elen",
  "F_name":"Mosh",
  "M_name":"Jack",
  "age":21
}
print("Before deleting:",student)
del student["age"]
print("After deleting:",student)

#-----------------------------------------------------------------------------------------------------------------

#4. counting frequency of numbers

num=[2,3,4,5,2,3,4,3,6,7,6,6]
freq={}
for i in num:
  if i in freq:
    freq[i]+=1
  else:
    freq[i]=1

print(freq)

#--------------------------------------------------------------------------------------------------------------------

#5.find key with maximum value 

scores={
  "Language":89,
  "Maths":98,
  "Physics":99,
  "Chemistry":86,
}
res=max(scores, key=scores.get)
print(res)

#----------------------------------------------------------------------------------------------------------------------

#6. merge two dictionaries

dict1={"apple":5,"orange":2}
dict2={"mango":7, "cherry":4}
merged= dict1.update(dict2)
print("After merging:", merged)

#-----------------------------------------------------------------------------------------------------------------------

#7.check if key exists

dict_1={
  "Men":45
  "Women:36
  "Children":13
}
if "Children" in dict_1:
  print("Key exists")
else:
  print("Key does not exists")

#------------------------------------------------------------------------------------------------------------------------







