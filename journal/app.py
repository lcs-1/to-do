date = input("Enter today's date: ")
mood = input("Rate your mood out of 10: ")
user_input = input("Write down today's events and how did your day go?\n")

with open(f"{date}.txt","w") as file:
    file.write(mood + '\n\n')
    file.write(user_input)
