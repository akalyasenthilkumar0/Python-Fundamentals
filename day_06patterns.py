#-----------------------------------------


#day_6patterns


#-----------------------------------------


#1.Square Star

n=4
for i in range(n):
   for j in range(n):
      print("*",end=" ")
   print()

#-----------------------------------------


#2.Right Triangle 

n=5
for i in range(1,n+1):
   for j in range(i):
       print("*",end=" ")
   print()

#-----------------------------------------


#3.Inverted Triangle 

n=5
for i in range(n,0,-1):
   for j in range(i):
       print("*",end=" ")
   print()

#-----------------------------------------


#4.Number Triangle 

n=4
for i in range(1,n+1):
   for j in range(1,i+1):
       print(j,end=" ")
   print()

#-----------------------------------------


#5.Same Number Pattern

n=5
for i in range(1,n+1):
   for j in range(i):
       print(i,end=" ")
   print()

#----------------------------------------


#6.Pyramid Pattern

n = 4

for i in range(1,n+1):
  print(" " * (n - i), end="")
  for j in range(i):
      print("*", end=" ")
   print() 

#----------------------------------------


#7.Diamond Pattern

n=5
for i in range(1,n+1):
   print(" "*(n-i),end="")
   for j in range(i):
        print("*",end=" ")
   print()
    
for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    for j in range(i):
        print("*",end=" ")
    print()

#--------------------------------------- 


#8. Number Diamond 

n=5
for i in range(1,n+1):
  print(" "*(n-1),end=" ")
  for j in range(i):
     print(j,end=" ")
  print()

for i in range(n-1,0,-1):
    print(" "*(n-1),end=" ")
    for j in range(i):
       print(j,end=" ")
    print()

#------------------------------------- 

