# Assignment 1 — Student Result Management System

This project unit-tests `calculate_final_result(student_id)` while its database/UI dependencies are unavailable.

## Requirement and formula

`FinalMark = 0.10 × Attendance + 0.30 × CT + 0.60 × FinalExam`

## Driver and stubs

- **Unit under test:** `calculate_final_result()` in `src/result_system.py`.
- **Test driver:** `main()` in `src/test_driver.py`; it calls the unit, supplies cases, and compares expected with actual output.
- **Test stubs:** `MarksStub.get_attendance()`, `get_ct_marks()`, and `get_final_exam_marks()`; they return controlled marks in place of the unfinished Student Information System and Examination Database.

## Test cases

| ID | Attendance | CT | Final exam | Expected final mark | Purpose |
|---|---:|---:|---:|---:|---|
| TC1 | 90 | 80 | 85 | 84.0 | Normal case |
| TC2 | 100 | 100 | 100 | 100.0 | Maximum values |
| TC3 | 0 | 0 | 0 | 0.0 | Minimum values |
| TC4 | 90 | 50 | 40 | 48.0 | Low performance |
| TC5 | 75 | 70 | 60 | 64.5 | Typical case |

> Note: applying the supplied formula to TC4 yields **48.0**, not 54.0. The code and expected value use the formula consistently.

## Run in VS Code

1. Open this folder in VS Code: **File → Open Folder…** → `ast`.
2. Open **Terminal → New Terminal**.
3. Run:

```bash
cd /Users/momshadabdullah/Documents/ChatGPT/ast
python3 src/test_driver.py
```

4. Take a screenshot showing the full terminal table and the `Summary: 5/5 test cases passed` line. For the report, also show the Explorer with `src/result_system.py` and `src/test_driver.py` visible.

## Why Spiral model

The Spiral model is appropriate because this result system has integration risk: the UI and database modules are unfinished. Each loop can identify risks (incorrect weighting, unavailable data, invalid marks), build a small prototype or stub, test it, review the result, and plan the next loop. The final loops replace the stubs with real database modules and integrate the user interface.

## GitHub commands

The repository is already initialized locally. After creating the GitHub repository at `https://github.com/MomshadTech/Assignment1`, run:

```bash
git add .
git commit -m "Add student result driver and stubs"
git branch -M main
git remote add origin https://github.com/MomshadTech/Assignment1.git
git push -u origin main
```

If `origin` already exists, replace the `git remote add` command with:

```bash
git remote set-url origin https://github.com/MomshadTech/Assignment1.git
```
