import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["question_text"])
    for index, choice in enumerate(question["alternatives"]):
        print(index + 1, "-", choice)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice  # adding user_choice to the dictionary

score = 0
# iterate through the updated data with persons answers
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"

    message = f"{result} {index + 1} - Your answer: {question['user_choice']}, "\
              f"Correct Answer: {question['correct_answer']}"
    print(message)

print(score, "/", len(data))
