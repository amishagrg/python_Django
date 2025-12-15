from typing import List
from src.models.students import Student


def average_age(students: List[Student]) -> float:
    if not students:
        return 0.0
    return sum(s.age for s in students) / len(students)


def count_by_gender(students: List[Student]) -> dict:
    counts = {}
    for s in students:
        g = s.gender.lower()
        counts[g] = counts.get(g, 0) + 1
    return counts
