students_count = int(input())
students = {}

for i in range(students_count):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for name, grade in students.items():
    avg = sum(grade) / len(grade)
    formmated_grades = ' '.join(f'{g:.2f}' for g in grade)
    print(f'{name} -> {formmated_grades} (avg: {avg:.2f})')