
#loops

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line
 #iterate over the elements of a tuple
 
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print(product)

#loop through each character in a string

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')  
        
#range()
#range() is a function that returns a sequence of numbers. It turns out to be very useful for writing loops.


for i in range(5):
    print("Doing important work. i =", i)

#while loops
#The other type of loop in Python is a while loop, which iterates until some condition is met:

i = 0
while i < 10:
    print(i, end=' ')
    i += 1 # increase the value of i by 
    
#List comprehensions

squares = [n**2 for n in range(10)]
squares
    
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#Here's how we would do the same thing without a list comprehension:

squares = []
for n in range(10):
    squares.append(n**2)
squares

#We can also add an if condition:

short_planets = [planet for planet in planets if len(planet) < 6]
short_planets

#with an if condition and applying some transformation to the loop variable:

# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
loud_short_planets

['VENUS!', 'EARTH!', 'MARS!']
#(Continuing the SQL analogy, you could think of these three lines as SELECT, FROM, and WHERE)







