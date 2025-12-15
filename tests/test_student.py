import tempfile
from pathlib import Path
from src.services.student_service import StudentService
from src.config import settings


def test_add_and_delete(tmp_path: Path):
    # point the settings to a temporary file for testing
    data_dir = tmp_path / "data"
    data_dir.mkdir()

    students_file = data_dir / "students.json"

    # create an empty students file
    students_file.write_text("[]")

    # monkeypatch the settings to use this temp path
    settings.STUDENTS_FILE = students_file

    svc = StudentService()

    # Add a student
    s = svc.add_student("Alice", 20, "F", "A")
    assert s.name == "Alice"

    # Ensure student exists
    all_students = svc.list_students()
    assert any(st.id == s.id for st in all_students)

    # Delete student
    deleted = svc.delete_student(s.id)
    assert deleted is True

    # Ensure list is empty again
    assert svc.list_students() == []
