# Student management system

## data/ students.json
This contains stores students data in JSON format. example: []

## src/config/settings.py
defines project path

## src/ models/student.py
defines the student model using a dataclass. By using dataclass we donot need to write magic method

## src/utils/file_utils.py
handles file creation, loading and saving

## src/services/analytics.py
contains two simple analytics function
- average_age(students)
- count_by_gender(students)

## src/services/student_service.py
This is the core service layer that manages all operations

## src/main.py
This is the main menu program
What happens:-
- shows menu
- takes user input
- calls functions in StudentService
- print result

## tests/test_student.py
this file tests
- addding a student
- deleting a student
- using a temporary file
- ensuring no real data gets changed