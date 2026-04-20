#-----------------------------------------

# day_07String

#-----------------------------------------


#1.Accessing of strings

s="GOOD"
print("Accessing the characters of the string:")

print("Positive Indexing:")
print("First character:",s[0])
print("Second character:",s[1])
print("Third character:",s[2])
print("Fourth character:",s[3])

print("Negative Indexing:")
print("Fourth character:",s[-1])
print("Third character:",s[-2])
print("Second character:",s[-3])
print("First character:",s[-4])

#-----------------------------------------


#2.Slicing 

s="WELCOME"
print("Slicing:")
print(s[2:5:1])
print(s[0:4:2])
print(s[1:6])
print(s[:5])
print(s[4:])

#-----------------------------------------


#3.Stride

s="FANTASY"
print("String after striding:")
print(s[::3])
print(s[::2])
print(s[::5])

#----------------------------------------


#4.Reversing using loop

org_str="WELCOME"
a=len(org_str)
print("The original String is", org_str)
print("The reverse of the given String is", )
for i in range(a-1,-1,-1):
    rev_str = org_str[i]
    print( rev_str,    end=" ")

#-----------------------------------------


#5.Reversing using Stride operator 


s="PYTHON"
rev=s[::-1]
print("Reverse of the sring:", rev)

#----------------------------------------

