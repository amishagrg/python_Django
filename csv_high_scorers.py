import csv

# opening the first csv file "students.csv" and reading the data
with open("students.csv", "r") as input_file:
    csv_reader= csv.reader(input_file)
    header_row= next(csv_reader) # to skip header row

    # to collect students who got more than 60 marks
    passed_students  = [header_row]

    for record in csv_reader:
        if len(record) < 2:    # to skip empty rows
            continue

        name= record[0]     # first column = student name
        marks= int(record[1])   # second column = marks (converting to number)

        if marks>60:
            passed_students.append([name, marks])

with open("students_high_scores.csv", "w") as f:
    csv_writer= csv.writer(f)
    csv_writer.writerows(passed_students)

