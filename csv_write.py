import csv 

# students and their respective marks
students= [
    ["Name", "Marks"],
    ["Rita", 87],
    ["Ram", 62],
    ["Sita", 91],
    ["Hari", 43],
    ["Harry", 34],
    ["Shyam", 56],
    ["Gita", 78],
    ["Nita", 45],
    ["Laxmi", 92],
    ["Mita", 50]
]

# writing data into csv file
with open("students.csv", "w") as file:
    writer= csv.writer(file)
    writer.writerows(students)
