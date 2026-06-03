#-----------------------------------------------------------------------------------------------------------------
#File Handling 
#-----------------------------------------------------------------------------------------------------------------
#File_name: data.txt
#contents in file(data.txt)
#Fruits: Apple, Mango, Orange, Banana
#Vegetables: Carrot, Potato, Cabbage, Raddish


#1. Reading Entire file

with open("data.txt", "r") as file:
    res = file.read()
    print(res)

#-----------------------------------------------------------------------------------------------------------------

#2. Reading the file line by line 

file = open("data.txt","r")
info = file.readline()
print(info)
file.close()

#-----------------------------------------------------------------------------------------------------------------

#3. Writing into the file

file = open("data.txt", "r")
nf = file.write("Dairy: Milk, Cheese, Butter, Panner, Curd")
print(nf)
file.close()

#-----------------------------------------------------------------------------------------------------------------

#4. Appending into the file

file = open("data.txt", "a")
af = ("Ice-cream: Vanilla, Chocolate, Strawberry, Blackcurrent")
res = file.write( af + "\n" )
print(res)
print("Sucessfully appended")

#-----------------------------------------------------------------------------------------------------------------

#5.counting lines using readlines()

with open("data.txt", "r") as f:
  lines = f.readlines()
  count = len(lines)
  print("Number of lines in the file:", count)

#------------------------------------------------------------------------------------------------------------------

#6.counting lines using loop

f=open("data.txt", "r")
  count=0
  for line in f:
    count+=1
print("Total lines:", count)

#------------------------------------------------------------------------------------------------------------------

#7.Counting Words in a file

with open("data.txt", "r") as f:
  line = f.readlines()
  count=0
  
  for line in f:
    words = line.split()
    count += len(words)

print("Total Words:", count)

#--------------------------------------------------------------------------------------------------------------------


