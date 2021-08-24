                                    

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



# enumerates:
    
squares = ["red", 'yellow', 'green']

for i, square in enumerate(squares):
    print(i,square)


# while loop:
    
# squares = ['orange', 'orange', 'purple', 'pink', 'orange']

# newsquares = []

# i = 0

# while(squares[i] == 'orange'):
#     newsquares.append(squares[i])
    
# print(newsquares)


# sorted vs sort function:
    
L = [5,3,2]
sorted(L)


print(L)                   # it does not change the L value


L = [5,3,2]
L.sort()

print(L)                    # It changes the L value


# Functions:
    
def add1(a):
    b = a + 1
    return b

c = add1(8)
c = add1(10)
print(c)                     # old values are not taken into consideration



def printstuff(stuff):
    
    for i, s in enumerate(stuff):
        
        print("Album", i, "rating is",s)
    

album_rating = [10.0, 25, 11]
printstuff(album_rating)


#

def addDC(x):
    x = x + "DC"
    print(x)
    return x

addDC("AC ")


# object and classes:
    
import matplotlib.pyplot as plt

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
      
RedCircle = Circle(10, 'red')

dir(RedCircle)
RedCircle.radius
RedCircle.radius = 1
RedCircle.radius
RedCircle.drawCircle()



x=5
while(x!=2):
  print(x)
  x=x-1


class Points(object):
  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p1=Points("A","B")
p1.print_point()


class Points(object):

  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p2=Points(1,2)

p2.x='A'

p2.print_point()
























