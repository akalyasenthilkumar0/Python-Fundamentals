#--------------------------------------------------------------------------------------------------

#day_08List

#--------------------------------------------------------------------------------------------------

#1. maximum and minimum 
#without using built-in function 

l1=[11,22,33,44,55]
max=l1[0]
min=l1[0]
for i in l1:
  if i > max:
    max=i
  if i < min:
    min=i 
    
print("Maximum number in the list:",max)
print("Minimum number i the list:",min)
    
#---------------------------------------------------------------------------------------------------    

#2.remove duplicates

l1=[2,4,6,8,9,9,0]
print("Existing list with duplicates:",l1)
l2=[]
for i in l1:
  if i not in l2:
    l2.append(i)
print("New list after removing the duplicates",i) 

#------------------------------------------------------------------------------------------------------

#3.second largest number 

num=[20,99,80,76,554,7676]
num.sort()
sl_num=num[-2]
print("second largest number in the list:",sl_num)

#--------------------------------------------------------------------------------------------------------

#4.sum of all elements 

list_1=[12,34,56,78,9,73]
sum=0
for i in list_1:
  sum += i
print("total"=,sum)

#----------------------------------------------------------------------------------------------------------

#5.merge two lists

l1=[0,2,4,6,8]
l2=[1,3,5,7,9]
merged= l1+l2
print("Merged list:",merged)

#-----------------------------------------------------------------------------------------------------------

#6.split odd and even 

l=[22,77,90,86,45,6,10,59]
even=[]
odd=[]
for i in l:
  if (i%2==0):
    even=even.append(i)
  else:
    odd=odd.append(i)
print("Even List:",even)
print("Odd LIst:", odd)

#------------------------------------------------------------------------------------------------------------

#7.finding the missingnumber in a sequence 

num=[1,2,4,5,6,7]
for i in range(1,len(num)+2):
  if i not in num:
    print(i)
    break

#------------------------------------------------------------------------------------------------------------


