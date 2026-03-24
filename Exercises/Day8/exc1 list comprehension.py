names = ["john smith", "jay santi", "eva kuki"]
#capitalize all the names and surnames
names = [name.title() for name in names]
# print the updated list
print(names)
# result should be ['John Smith', 'Jay Santi', 'Eva Kuki']

#next exercise
usernames = ["john 1990", "alberta1970", "magnola2000"]
length_usernames = [len(username) for username in usernames]
print(length_usernames)

#next exercise
user_entries = ['10', '19.1', '20']
user_entries = [float(number) for number in user_entries]
print(user_entries)

#next exercise
numbers = [10, 20, 30]
numbers = [number * 2 for number in numbers]
print(numbers)

#Exercise 47:
#Sum of Numbers
#Extend the given code so it prints out the sum of the numbers. Note that the numbers are currently string types.
#The output of your code should be as below:#
#		49.1
# Define the initial list of user entries as strings
user_entries = ['10', '19.1', '20']

# Use list comprehension to convert each item to a float
user_entries = [float(item) for item in user_entries]

# Print the sum of the numbers
print(sum(user_entries))