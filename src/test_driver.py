"""Test driver and test stubs for calculate_final_result()."""

from dataclasses import dataclass
from result_system import calculate_final_result


@dataclass(frozen=True)
class StudentMarks:
    attendance: float
    ct: float
    final_exam: float


class MarksStub:
    """Stub: replaces unfinished student-information/exam database modules."""

    def __init__(self, marks_by_student: dict[str, StudentMarks]):
        self.marks_by_student = marks_by_student

    def _marks_for(self, student_id: str) -> StudentMarks:
        return self.marks_by_student[student_id]

    def get_attendance(self, student_id: str) -> float:
        return self._marks_for(student_id).attendance

    def get_ct_marks(self, student_id: str) -> float:
        return self._marks_for(student_id).ct

    def get_final_exam_marks(self, student_id: str) -> float:
        return self._marks_for(student_id).final_exam


def main() -> None:
    """Driver: calls the unit under test and compares actual/expected results."""
    cases = {
        "TC1 Normal case": ("S101", StudentMarks(90, 80, 85), 84.0),
        "TC2 Maximum values": ("S102", StudentMarks(100, 100, 100), 100.0),
        "TC3 Minimum values": ("S103", StudentMarks(0, 0, 0), 0.0),
        "TC4 Low performance": ("S104", StudentMarks(90, 50, 40), 48.0),
        "TC5 Typical case": ("S105", StudentMarks(75, 70, 60), 64.5),
    }
    print("Student Result Management System — Driver + Stub Unit Test")
    print("-" * 68)
    print(f"{'Case':<23} {'Student':<8} {'Expected':>9} {'Actual':>8}  Result")
    print("-" * 68)
    passed = 0
    for name, (student_id, marks, expected) in cases.items():
        actual = calculate_final_result(student_id, MarksStub({student_id: marks}))
        status = "PASS" if actual == expected else "FAIL"
        passed += status == "PASS"
        print(f"{name:<23} {student_id:<8} {expected:>9.1f} {actual:>8.1f}  {status}")
    print("-" * 68)
    print(f"Summary: {passed}/{len(cases)} test cases passed")


if __name__ == "__main__":
    main()
