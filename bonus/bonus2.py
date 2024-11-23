user_input = input("Please enter the student name: ")

with open('names.txt','a') as file:
    file.write(user_input + '\n')
