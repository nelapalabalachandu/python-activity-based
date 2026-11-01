basic_salary = float(input("Enter basic salary: "))

hra = basic_salary * 0.10
da = basic_salary * 0.05

gross_salary = basic_salary + hra + da

print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross_salary)
