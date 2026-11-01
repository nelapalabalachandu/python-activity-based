m1 = int(input("Enter first subject marks: "))
m2 = int(input("Enter second subject marks: "))
m3 = int(input("Enter third subject marks: "))

total = m1 + m2 + m3
average = total / 3

print("Total Marks:", total)
print("Average Marks:", average)

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")
