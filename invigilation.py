import csv
from datetime import datetime, timedelta

# Functions
def is_teacher_available(teacher, date):
    return date > teacher['unavailable_until']

def invigilation_cost(teacher, exam_subject, date):
    if not is_teacher_available(teacher, date):
        return float('inf')
    cost = 0
    if exam_subject in teacher['subjects'].split(' and '):
        cost += 10
    cost += teacher['invigilation_count']
    return cost

# Read teacher data from CSV
with open('teachers.csv', mode='r', encoding='utf-8-sig') as file:
    csvFile = csv.DictReader(file)
    teachers = [row for row in csvFile]

# Initialize additional teacher info
for teacher in teachers:
    teacher['unavailable_until'] = datetime(2000, 1, 1).date()
    teacher['invigilation_count'] = 0

# Read exam timetable from CSV
with open('exams.csv', mode='r', encoding='utf-8-sig') as file:
    csvFile = csv.DictReader(file)
    exams = [row for row in csvFile]

# Allocate teachers to exams
allocation = {}

for exam in exams:
    date = datetime.strptime(exam['Date'], "%Y-%m-%d").date()
    required_teachers = -(-int(exam['Students']) // 30)
    allocated_teachers = []

    while len(allocated_teachers) < required_teachers:
        available_teachers = [teacher for teacher in teachers if is_teacher_available(teacher, date)]
        if not available_teachers:
            break

        available_teachers.sort(key=lambda t: invigilation_cost(t, exam['Subject'], date))
        best_teacher = available_teachers.pop(0)

        allocated_teachers.append(best_teacher['name'])
        best_teacher['invigilation_count'] += 1

        if exam['Subject'] in best_teacher['subjects'].split(' and '):
            best_teacher['unavailable_until'] = date + timedelta(days=2)

    allocation[(exam['Date'], exam['Time'], exam['Venue'])] = allocated_teachers

# Output allocations
for key, value in allocation.items():
    print(f"On {key[0]} at {key[1]} in {key[2]}, the allocated teachers are: {', '.join(value)}")

# Output teacher invigilation count
print("\nNumber of invigilations for each teacher:")
for teacher in teachers:
    print(f"{teacher['name']}: {teacher['invigilation_count']} times")
