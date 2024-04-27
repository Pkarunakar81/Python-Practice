#Int
x = 14
print(x)
print(type(x))

#Floats
nearly_pi = 3.141592653589793238462643383279502884197169399375105820974944
print(nearly_pi)
print(type(nearly_pi))

#Round to 5 decimal places
almost_pi = 22/7
rounded_pi = round(almost_pi, 5)
print(rounded_pi)
print(type(rounded_pi))

#Booleans
z_one = True
print(z_one)
print(type(z_one))


z_three = (1 < 2)
print(z_three)
print(type(z_three))

#Strings

w = "Hello, Python!"
print(w)
print(type(w))

#If you put a number in quotation marks, it has a string data type.

my_number = "1.12321"
print(my_number)
print(type(my_number))

also_my_number = float(my_number)#If we have a string that is convertible to a float, we can use float().
new_string = "abc" + "def"#concatenating 

#we can't multiply two strings,but you can multiply a string by an integer. 
#This again results in a string that's just the original string concatenated with itself a specified number of times.

newest_string = "abc" * 3

will_not_work = "abc" * 3.#we cannot multiply a string by a float!.
print(newest_string)
print(type(newest_string))


print(int(1.2321))
#print(int(1.747))
#print(int(-3.94535))
#print(int(-2.19774))

1
1
-3
-2

#print(3 * True)
#print(-3.1 * True)
#print(type("abc" * False))
#print(len("abc" * False))
3
-3.1
<class 'str'>
0

print(False + False)#0
print(True + False)#1
print(False + True)#1
print(True + True)#2
print(False + True + True + True)#3



