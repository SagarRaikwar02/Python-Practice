#Many Values to Multiple Variables:-
x , y , z = "Orange" , "Banana" , "Kiwi"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Oragne"
print(x)
print(y)
print(z)

# How to unpack a list or tuple
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple","banana","oragne","kiwi"]
x , y , _, _ = fruits

print(x)
print(y)
# print(z)
# print(k)

# You can also use the + operator to output multiple variables:

x = "python"
y = "is an "
z = "awsome programming lanuage"

print (x+y+z)

# Global Variables
#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.
#Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
    print("Python is " + x )

myfunc()


#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
    y = "Sexy"
    print("Pyton is so " + y) 

myfunc()

print("Python is " + x)


#The global Keyword
#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.
#If you use the global keyword, the variable belongs to the global scope:

a = "Mustang"

def myfunc():
    global a
    b = "Range Rover"
    print("A Wonderfull car " + a)

myfunc()

print ("This is a " + a)