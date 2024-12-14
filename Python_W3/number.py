#There are three numeric types in Python:
#int
#float
#complex
#Variables of numeric types are created when you assign a value to them:
#Example:-

x = 1

y = 2.8

z = 1j

print(type(x))
print(type(y))
print(type(z))

#Int
#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length

x = 1
y = 121887692453
z = -2456889

print(type(z))
print(type(y))
print(type(z))

#Float
#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 2.5
y = 1.122
z = -35.966

print(type(x))
print(type(y))
print(type(z))

#Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 35e9
y = 12e4
z = -87.e885

print(type(x))
print(type(y))
print(type(z))


#Complex
#Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j 
z = -3j

print(type(x))
print(type(y))
print(type(z))

#Type Conversion
#You can convert from one type to another with the int(), float(), and complex() methods:

x = 2
y = 5.3
z = 1j

#Convert from int to float :-
a = float(x)

#Convert from float to int :-
b = int(y)

#Convert from int  to complex :-
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


#Random Number
#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
#Import the random module, and display a random number between 1 and 9:

import random

print(random.randrange(1,5))