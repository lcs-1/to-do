password = input("Please enter the password: ")

if len(password)>=8 and any(char.upper() for char in password) and any(char.isalpha() for char in password):
    print(f"Your password is {password}")
else:
    print("Password does not meet the requirements please try again!")