"""Student Result Management System: unit under test plus dependency interface."""

from typing import Protocol


class MarksProvider(Protocol):
    """Dependencies needed by calculate_final_result."""

    def get_attendance(self, student_id: str) -> float: ...
    def get_ct_marks(self, student_id: str) -> float: ...
    def get_final_exam_marks(self, student_id: str) -> float: ...


def calculate_final_result(student_id: str, provider: MarksProvider) -> float:
    """Return 10% attendance + 30% CT + 60% final-exam marks."""
    attendance = provider.get_attendance(student_id)
    ct_marks = provider.get_ct_marks(student_id)
    final_exam = provider.get_final_exam_marks(student_id)

    for label, mark in (("Attendance", attendance), ("CT", ct_marks), ("Final exam", final_exam)):
        if not 0 <= mark <= 100:
            raise ValueError(f"{label} must be between 0 and 100; received {mark}")

    return round(0.10 * attendance + 0.30 * ct_marks + 0.60 * final_exam, 1)
