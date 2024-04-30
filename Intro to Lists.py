#Intro to Lists
flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"
 print(flowers.split(","))
 
 
print(type(flowers))
print(flowers)
#To create a list, you need to use square brackets ([, ]) and separate each item with a comma
flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list))
print(flowers_list)
print(len(flowers_list))
print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])

# The list has length ten, so we refer to final entry with 9
print("Last entry:", flowers_list[9])
#Slicing

to pull the first x entries, you use [:x], and
to pull the last y entries, you use [-y:].

print("First three entries:", flowers_list[:3])
print("Final two entries:", flowers_list[-2:])

#Removing items

flowers_list.remove("globe thistle")
print(flowers_list)

#Adding items
flowers_list.append("snapdragon")
print(flowers_list)

Lists are not just for strings
So far, we have only worked with lists where each item in the list is a string. 
But lists can have items with any data type, including booleans, integers, and floats.
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
we can also get the minimum with min() and the maximum with max().
print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))
To add every item in the list, use sum().

print("Total books sold in one week:", sum(hardcover_sales))
#we take the sum from the first five days
print("Average books sold in first five days:", sum(hardcover_sales[:5])/5)

#Lists

primes = [2, 3, 5, 7]
We can even make a list of lists:
    
    hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

A list can contain a mix of different types of variables:
    
my_favourite_things = [32, 'raindrops on roses', help]
# (Yes, Python's help function is *definitely* one of my favourite things)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

#Indexing
planets[0]
planets[-1]
#Slicing
planets[0:3]
planets[1:-1]
#Changing lists
#Lists are "mutable", meaning they can be modified "in place".
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets[3] = 'Malacandra'
planets
['Mercury',
 'Venus',
 'Earth',
 'Malacandra',
 'Jupiter',
 'Saturn',
 'Uranus',
 'Neptune']
 
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# That was silly. Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]
['Mur', 'Vee', 'Ur', 'Malacandra', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
#List functions
len(planets)
sorted(planets)#returns a sorted version of a list:
sum(primes)
max(primes)
#Interlude: objects objects carry some things around with them. You access that stuff using Python's dot syntax.
x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)
x.bit_length
x.bit_length()
#List methods

#list.append modifies a list by adding an item to the end:
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets.append('Pluto')
help(planets.append)
print(planets)
#list.pop removes and returns the last element of a list:
planets.pop() 
print(planets)
#Searching lists   We can get its index using the list.index method.
print(planets.index('Earth'))
#print(planets.index('Pluto'))#ValueError: 'Pluto' is not in list

#To avoid unpleasant surprises like this, 
#we can use the in operator to determine whether a list contains a particular value:

print("Earth" in planets)
print("Pluto" in planets)
print(planets)










