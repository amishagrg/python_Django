from typing import List, Optional
from src.models.students import Student
from src.config import settings
from src.utils.file_utils import load_json, save_json


class StudentService:
    def __init__(self, storage_path: Optional[str] = None):
        self.file_path = settings.STUDENTS_FILE
        # lazy-load students into memory
        self._students: List[Student] = self._load_students()

    def _load_students(self) -> List[Student]:
        raw = load_json(self.file_path, [])
        return [Student.from_dict(d) for d in raw]

    def _persist(self):
        save_json(self.file_path, [s.to_dict() for s in self._students])

    def add_student(self, name: str, age: int, gender: str, grade: str) -> Student:
        student = Student.create(name, age, gender, grade)
        self._students.append(student)
        self._persist()
        return student

    def list_students(self) -> List[Student]:
        return list(self._students)

    def find_by_id(self, student_id: str) -> Optional[Student]:
        for s in self._students:
            if s.id == student_id:
                return s
        return None

    def search_by_name(self, name_query: str) -> List[Student]:
        q = name_query.strip().lower()
        return [s for s in self._students if q in s.name.lower()]

    def update_student(self, student_id: str, **fields) -> Optional[Student]:
        s = self.find_by_id(student_id)
        if not s:
            return None

        # only update provided fields
        if "name" in fields and fields["name"] is not None:
            s.name = fields["name"].strip()

        if "age" in fields and fields["age"] is not None:
            s.age = int(fields["age"])

        if "gender" in fields and fields["gender"] is not None:
            s.gender = fields["gender"].strip()

        if "grade" in fields and fields["grade"] is not None:
            s.grade = fields["grade"].strip()

        self._persist()
        return s

    def delete_student(self, student_id: str) -> bool:
        before = len(self._students)
        self._students = [s for s in self._students if s.id != student_id]
        changed = len(self._students) != before
        if changed:
            self._persist()
        return changed

    def export_backup(self, backup_path=None) -> None:
        import shutil
        from src.config import settings

        bp = backup_path or settings.BACKUP_FILE
        bp.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy
