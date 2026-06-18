students = {}

for i in range(3):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nStudent Records")
print("----------------")

total = 0

for name, marks in students.items():
    print(name, ":", marks)
    total += marks

average = total / len(students)

print("----------------")
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
