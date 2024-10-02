# Sets##################################
# Sets are unordered collections of unique elements
# Sets are mutable
# Sets are defined by curly braces {}
#example of sets
set1 = {1, 2, 3, 4, 5}  # set of integers
set2 = {'apple', 'banana', 'cherry'}  # set of strings
set3 = {1, 2, 3, 'apple', 'banana'}  # mixed set
set4 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}  # duplicate elements are removed
# print(set1)
# print(set2)
# print(set3)
# print(set4)

# #access elements in a set
# # print(set1[0]) # error: 'set' object does not support indexing
# for element in set1:
#     print(element)
# print(1 in set1) # Output: True
# print(6 in set1) # Output: False
# print(len(set1)) # Output: 5
# print(3 in set3)
# print("apple" in set3) # Output: True

# # add elements to a set
# set1.add(6)
# print(set1)
# set2.add('orange')
# print(set2)
# set3.add('pineapple '  'orange '  'mango ')
# print(set3)

# #remove elements from a set
# set1.remove(3)
# print(set1)
# set2.discard('banana')
# print(set2)

# #check if an element is in a set
# print(3 in set1) # Output: False
# print('banana' in set2) # Output: False

# #find the length of a set
# print(len(set1)) # Output: 5
# print(len(set2))
# print(len(set3))
# print(len(set4))

# #clear a set
# set1.clear()
# print(set1) # Output: set()
# id_numbers = {927270, 965371, 7188371, 10937710, 4371936}
# #remove first element from set
# id_numbers.pop()
# print(id_numbers) # Output: {7188371, 927270, 965371, 10937710}
# # add a few more elements to the set using the add method
# #sets do not print in order of insertion
# id_numbers.add(191762)
# print(id_numbers) # Output: {191762, 7188371, 927270, 965371, 10937710}

#tuples##################################
# Tuples are ordered collections of elements
# Tuples are immutable
# Tuples are defined by parentheses ()
#example of tuples
# tuple1 = (1, 2, 3, 4, 5)  # tuple of integers
# tuple2 = ('apple', 'banana', 'cherry')  # tuple of strings
# tuple3 = (1, 2, 3, 'apple', 'banana')  # mixed tuple
# tuple4 = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)  # duplicate elements are allowed


# #access elements in a tuple
# print(tuple1[0]) # Output: 1
# print(tuple2[1]) # Output: 'banana'
# print(tuple3[2]) # Output: '3'
# print(tuple4) # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# #find the length of a tuple
# print(len(tuple1)) # Output: 5
# print(len(tuple2)) # Output: 3
# print(len(tuple3)) # Output: 5
# print(len(tuple4)) # Output: 10

# #count the number of occurrences of an element in a tuple
# print(tuple4.count(3)) # Output: 2
# print(tuple4.count(6)) # Output: 0

# #find the index of an element in a tuple
# print(tuple1.index(3)) # Output: 2
# print(tuple2.index('banana')) # Output: 1

# #convert a tuple to a list
# print(list(tuple1)) # Output: [1, 2, 3, 4, 5]

# #convert a list to a tuple
# print(tuple(list(tuple1))) # Output: (1, 2, 3, 4, 5)







#######################tuples challenge#####################
# Challenge: Count the number of occurrences of the character 'v' in the text below.
# The text is converted to a tuple of characters and the target characters are 'v' and 'V'.
# The result is output to the console.
#queue the videos(2)
text = """Voilà! In view, a humble vaudevillian veteran, cast vicariously as both victim and villain by the vicissitudes of Fate.
This visage, no mere veneer of vanity, is a vestige of the vox populi, now vacant, vanished. However, this valorous visitation
of a by-gone vexation stands vivified, and has vowed to vanquish these venal and virulent vermin vanguarding vice and
vouchsafing the violently vicious and voracious violation of volition.


The only verdict is vengeance; a vendetta, held as a votive, not in vain, for the value and veracity of such shall one day
vindicate the vigilant and the virtuous.


Verily, this vichyssoise of verbiage veers most verbose, so let me simply add that it is my very good honor to meet you
and you may call me V."""


# Convert the text to a tuple of characters
print(tuple(text))

tuple1 = (list(text))

# Tuple to store the target characters
occurance = tuple1.count("v")
occurance2 = tuple1.count("V")


# Count occurrences of 'v' or 'V' by filtering the text_tuple
total = (occurance + occurance2)




# Output the result
print(total)



# dictionarys Accessing a Value from a Nested List###############################
#Suppose we have a dictionary containing multiple lists as values, and you want to access a specific element from one of these lists.
# Define the dictionary


sample_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# get length of the list
print(sample_list[0]) # Output: [1, 2, 3]
print(sample_list[1]) # Output: [4, 5, 6]
print(sample_list[2]) # Output: [7, 8, 9]
#Extract the 8 out of the list
print(sample_list[2][1]) # Output: 8
print(sample_list[1][2])
print(sample_list[0][2])
print(sample_list[2][0])

print(len(sample_list)) # Output: 3
#this is called a nested list
# Extract and print the second element from the first list


sample_list_of_fruit = {"fruits": ["apple", "banana", "cherry"]}
# Extract and print the second fruit from the list
print(sample_list_of_fruit["fruits"][1]) # Output: 'banana'
print(sample_list_of_fruit["fruits"][0])
print(sample_list_of_fruit["fruits"][2])

sample_list_of_lists = {"lists": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]}
# Extract and print the third element from the second list
print(sample_list_of_lists["lists"][1][2]) # Output: 6
print(sample_list_of_lists["lists"][2][2]) # Output: 9
print(sample_list_of_lists["lists"][0][2]) # Output: 3



sample_list_of_dicts = {"dicts": [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 35}]}
# Extract and print the age of the second person
print(sample_list_of_dicts["dicts"][1]["age"]) # Output: 30
#get the name of the third person
print(sample_list_of_dicts["dicts"][2]["name"]) # Output: 'Charlie'





data = {
    "fruits": {"tropical": ["mango", "pineapple", "banana"], "berries": ["strawberry", "blueberry", "raspberry"]},
    "prices": {"mango": 1.5, "pineapple": 2.5, "banana": 0.5}
}


# Extract and print the second item from the 'tropical' list
print(data["fruits"]["tropical"][1])  # Output: 'pineapple'




# Define the dictionary
info = {
    "team": {"coach": {"name": "John Doe", "age": 45}, "players": ["Alice", "Bob", "Charlie"]},
    "location": "New York"
}


# Extract and print the coach's name
print(info["team"]["coach"]["name"])  # Output: 'John Doe'




# Define the dictionary
company = {
    "departments": {
        "HR": {
            "employees": ["Emma", "Oliver", "Sophia"],
            "budget": 50000
        },
        "Engineering": {
            "employees": ["Liam", "Noah", "Ethan"],
            "budget": 120000
        }
    }
}


# Extract and print the second employee from the 'Engineering' department
print(company["departments"]["Engineering"]["employees"][1])  # Output: 'Noah'


# Define the dictionary
school = {
    "class": {
        "name": "Math 101",
        "students": {"student1": "A", "student2": "B", "student3": "C"}
    }
}


# Update the grade of student2
school["class"]["students"]["student2"] = "A+"


# Print the updated dictionary
print(school)


# Define the dictionary
product_inventory = {
    "warehouse1": {
        "products": ["apples", "oranges", "bananas"],
        "quantities": [50, 30, 20]
    },
    "warehouse2": {
        "products": ["grapes", "pears", "peaches"],
        "quantities": [60, 40, 30]
    }
}


# Find the total number of oranges in warehouse1
orange_quantity = product_inventory["warehouse1"]["quantities"][1]
print(f"Total oranges in warehouse1: {orange_quantity}")  # Output: 30




# Define the dictionary
cities = {
    "USA": {
        "New York": {"population": 8000000, "mayor": "John"},
        "Los Angeles": {"population": 4000000, "mayor": "Mike"}
    },
    "Canada": {
        "Toronto": {"population": 2700000, "mayor": "Jane"},
        "Vancouver": {"population": 630000, "mayor": "Emily"}
    }
}


# Extract and print the population of Los Angeles
la_population = cities["USA"]["Los Angeles"]["population"]
print(f"Population of Los Angeles: {la_population}")  # Output: 4000000


