from bonus.convert8 import convert
import parses8

user_input = input("Enter the dimension in feet inches: ")
f,i = parses8.parse(user_input)
result = convert(f, i)

if result>1:
    print("You are eligible for the ride")
else:
    print("You aren't eligible for the ride")