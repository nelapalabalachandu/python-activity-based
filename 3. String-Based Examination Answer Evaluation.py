answer_key = ["A", "B", "C", "D", "A"]
student_answers = []

for i in range(5):
    answer = input("Enter answer for question " + str(i + 1) + ": ")
    student_answers.append(answer.upper())

correct = 0
wrong = 0
unanswered = 0

for i in range(5):
    if student_answers[i] == "":
        unanswered += 1
    elif student_answers[i] == answer_key[i]:
        correct += 1
    else:
        wrong += 1

print("Correct Answers:", correct)
print("Wrong Answers:", wrong)
print("Unanswered Questions:", unanswered)
print("Total Marks:", correct)
