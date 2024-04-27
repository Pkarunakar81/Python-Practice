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













