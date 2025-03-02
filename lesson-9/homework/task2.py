import csv
from collections import defaultdict

# Step 1: Read data from grades.csv
grades_data = []
filename = "grades.csv"

with open(filename, mode="r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Grade"] = int(row["Grade"])  # Convert grade to integer
        grades_data.append(row)

# Step 2: Calculate average grades for each subject
subject_grades = defaultdict(list)

for entry in grades_data:
    subject_grades[entry["Subject"]].append(entry["Grade"])

average_grades = {subject: sum(grades) / len(grades) for subject, grades in subject_grades.items()}

# Step 3: Write average grades to a new CSV file
output_filename = "average_grades.csv"

with open(output_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])  # Header row
    for subject, avg in average_grades.items():
        writer.writerow([subject, round(avg, 2)])  # Writing rounded average grades

print(f"Average grades saved to {output_filename}.")
