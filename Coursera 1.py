                                    

                                   # Coursera

# What is the output of this:
print("hello Mike".find("Mike"))

x =1/100
print(x)


str(1+1)

                                     # Tuples

Tuple1 = ("name",2,1.5)
print(Tuple1[0:2])

A = (1,2,3,4,5)                    #WHY......as 4 is excluded
print(A[1:4])


# Tuples are immutable means we cannot change them

# Tuple nesting

NT = (1,2,("name",1.4),"hello",(1,1.5,"Hello world"))
print(NT[2])

print(NT[2][0])

print(NT[4][2][2])

A[0] = (5)             # gives error as in tupple we cannot change


# LIST:
    
L = [1,2,("name",1.4),"hello"]

L.extend(["world",25])                # extend : it add two new elements 
print(L)

L.append(["world",25])                # append: It add only one element to list
print(L)

L[3] = "world"       
print(L)                     # it will replace hello by world


# convert string to list by using split 

A = "hard rock".split()             # separate by space
print(A)

# using delimiter

A = "hard,rock".split(",")             # separate by comma
print(A)

# List:clone

A = ["apple", "banana"]
B= A
A[0] = "pineapple"
print(B)                       # by changing A , B will  change
print(A)

# so,

A = ["apple", "banana"]
B= A[:]
print(B)

A[0] = "pineapple"
print(B)                       # by changing A , B will not change
print(A)

# Question:
print([1,2.3] + [1,1,1])


# SET

A = {1,2,3,1,2,3}                  # sets do not keep duplicate items
print(A)

# coverting list to sets

A_list = ["apple", "banana",1,"apple", "banana", 1]

A_set = set(A_list)

print(A_set)

type(A_set)

# add is used to add a element in set

A_set.add("pea")
print(A_set)

"pea" in A_set

"orange" in A_set

# intersection is used as &:
    
B_set = {"orange", "pea", "potato", 3.5}

C_set = A_set & B_set
print(C_set)

A_set.union(B_set)

D_set = {"pea"}

D_set.issubset(B_set)


# enumerate function:
    
A = ['a', 'b', 's']
for i, x in enumerate(A):
    print(i,x)













