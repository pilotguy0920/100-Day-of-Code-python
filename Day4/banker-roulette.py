import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Count number of people in list
number_of_people = len(names)
# Generate a random number from the number of people in the list
random_selection = random.randint(0, number_of_people - 1)
person_paying = names[random_selection]

print(person_paying + " is going to buy the meal today!")
