# Invigilation Allocation Script

## Overview

This script allocates educators for exam invigilation based on provided teacher data and exam timetable. It ensures that:

1. Teachers do not invigilate exams for the subjects they teach, wherever possible.
2. There's at least one teacher for every 30 students in an exam venue.
3. Teachers who have a subject examined are not allocated for invigilation for the next 2 days, allowing for marking.

## Prerequisites

- Python 3.7 or higher.
- CSV files containing teacher details (`teachers.csv`) and exam timetable (`exams.csv`).

## Files Structure

1. **teachers.csv**: Contains teacher details. Format:

    ```
    name,subjects,grades
    YD,technology and physical sciences,7 8 10
    DG,physical sciences,8 9 11 12
    ...
    ```

    - `name`: Name of the teacher.
    - `subjects`: Subjects taught by the teacher. Multiple subjects separated by "and".
    - `grades`: Space-separated list of grades the teacher teaches.

2. **exams.csv**: Contains the exam timetable. Format:

    ```
    Date,Time,Subject,Grade,Venue,Learners
    2023-11-10,09:00,Math,10,Room A,28
    2023-11-10,14:00,History,11,Room B,40
    ...
    ```

    - `Date`: Date of the exam.
    - `Time`: Time of the exam.
    - `Subject`: Subject of the exam.
    - `Grade`: Grade level of the exam.
    - `Venue`: Venue of the exam.
    - `Learners`: Number of learners taking the exam.

## Running the Script

1. Ensure you have the CSV files (`teachers.csv` and `exams.csv`) in the same directory as the script.
2. Run the script using Python:

    ```bash
    python invigilation.py
    ```

3. The script will print the allocation of teachers for each exam session, followed by the tally of invigilations for each teacher.

## License

This project is released under the MIT License.
