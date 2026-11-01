marks = []

for i in range(3):
    mark = int(input("Enter subject marks: "))
    marks.append(mark)

total = sum(marks)
average = total / 3

print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 75:
    print("Excellent Performance")
elif average >= 50:
    print("Good Performance")
else:
    print("Needs Improvement")
