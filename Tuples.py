#Tuples

Tuples are almost exactly the same as lists. They differ in just two ways.

1: The syntax for creating them uses parentheses instead of square brackets

t = (1, 2, 3)

2: They cannot be modified (they are immutable).


t[0] = 100#TypeError: 'tuple' object does not support item assignment

Tuples are often used for functions that have multiple return values.


#For example, the as_integer_ratio() method of float objects returns a numerator and a denominator in the form of a tuple:

x = 0.125
x.as_integer_ratio()

print(x.as_integer_ratio())#(1, 8)

#These multiple return values can be individually assigned as follows:

numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)

#Trick™ for swapping two variables!

a = 1
b = 0
a, b = b, a


