import json

with open("bonus/unique_questions.json","r") as file:
    content = file.read()

data = json.loads(content)
print(data)

score = 0

for i,question in enumerate(data):
    print(question["Question"])
    for index,alternaive in enumerate((question["alternatives"]),start=1):
        print(index,'-',alternaive)
    user_choice = int(input("Choose the correct answer: "))
    question["user_choice"] = user_choice
    if question["user_choice"] == question["correct answer"]:
        score+=1
        print(f"Your choice is {question["user_choice"]} and its correct!")
    else:
        print(f"Your choice is {question["user_choice"]} and the correct answer is {question["correct answer"]}")
    print(f"Your score is {score}/{i+1}")