from dataclasses import dataclass, asdict
from uuid import UUID, uuid4
from typing import Optional
@dataclass
class Student:
    id: str
    name: str
    age: int
    gender: str
    grade: str
    @classmethod
    def create(cls, name: str, age: int, gender: str, grade: str)-> "Student":
        return cls(id=str(uuid4()), name=name.strip(), age=age,
        gender=gender.strip(), grade=grade.strip())
    def to_dict(self)-> dict:
        return asdict(self)
    @classmethod
    def from_dict(cls, data: dict)-> "Student":
 # simple validation could be added her
        return cls(
            id=data["id"],
            name=data.get("name", ""),
            age=int(data.get("age", 0)),
            gender=data.get("gender", ""),
            grade=data.get("grade", ""),
            )