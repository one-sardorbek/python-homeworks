
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(university_data):
    student_enrollments = []
    tuition_fees = []
    for university in university_data:
        student_enrollments.append(university[1])
        tuition_fees.append(university[2])
    return student_enrollments, tuition_fees

def mean(data):
    return sum(data) / len(data)

def median(data):
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        middle1 = sorted_data[n // 2 - 1]
        middle2 = sorted_data[n // 2]
        return (middle1 + middle2) / 2


enrollments, tuitions = enrollment_stats(universities)


total_students = sum(enrollments)
total_tuition = sum(tuitions)


mean_students = mean(enrollments)
mean_tuition = mean(tuitions)


median_students = median(enrollments)
median_tuition = median(tuitions)


print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print()
print(f"Student mean: {mean_students:,.2f}")
print(f"Student median: {median_students:,}")
print()
print(f"Tuition mean: $ {mean_tuition:,.2f}")
print(f"Tuition median: $ {median_tuition:,}")
print("******************************")