
# User Inputs
# Activity 1
# Using Python:
# Write a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
name=input("Enter your name: ")
age=int(input("Enter your age: "))
#calculate age
year_100=100+(2026-age)
print(f"{name} will turn 100 in year {year_100}")