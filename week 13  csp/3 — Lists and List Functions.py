# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
# Lists are part of the collections family in Python family
#Creating a list
my_list=[1, 2, 3, 4, 5]
print(my_list) # [1, 2, 3, 4, 5]
print(len(my_list)) # 5
print(type(my_list)) # <class ' list'>
print(my_list[0]) #1
print(my_list[1:4]) # [2, 3, 4]
print(my_list[1:]) # [2,3, 4, 5]
print(my_list[:-1]) # [1, 2, 3, 4]
#reserve the list
print(my_list[::-1]) # 5, 4, 3 ,2 ,1]
# Modifying a list
my_list.append(6) # adds 6 to the end of the list
print(my_list) # [1, 2, 3, 4, 5]
# add 7 and 8 to the end of the list
my_list.extend([7, 8])
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]
# remove the last item
my_list.pop()
print(my_list) # [1, 2, 4, 5, 6, 7]
# remove the item at index 2
my_list.pop(2)
print(my_list) # [1, 2, 4, 5, 6, 7]
# reverse the list
my_list.reverse()
print(my_list) # [ 7, 6 , 5, 4, 2, 1]
# remove to remove a specific value
my_list.remove(4)
print(my_list) # [7, 6,5 2, 1]
# remove the last item using negative index
# add 50 more to the end of the list
new_list = list(range(12, 120))
print(new_list)
my_list.append(new_list)
print(my_list)
my_list.extend(new_list)
print(len(my_list))
#print every 3rd item in the list
print(my_list[ : : 3])
# print every 3rd item in the list
del my_list [ : : 3]
print(len(my_list))
print(my_list)

# list functions
 # . append() - adds an item to the end of the list
 # .extend() - adds multiple items to the end of the list
 #. pop() - removes and returns an item at a given index
 # ( default is the last item)
 # ,remove() - removes the first occurence of a specific value
 # . sorts() - sorts the list in ascending order
 #. reserve()- reserves the order of the list


# Examples:

print(my_list[ : : 3])
new_list = list(range(12, 220))
print(new_list)
my_list.append(new_list)
print(my_list)

# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.