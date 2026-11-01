total_classes = int(input("Enter total classes: "))
attended_classes = int(input("Enter attended classes: "))

if total_classes <= 0 or attended_classes < 0 or attended_classes > total_classes:
    print("Invalid input")
else:
    attendance = attended_classes / total_classes * 100
    print("Attendance Percentage:", attendance)

    if attendance >= 75:
        print("Eligible for examination")
    else:
        print("Not eligible for examination")

