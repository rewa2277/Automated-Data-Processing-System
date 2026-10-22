
import csv
import os
from database import connect_database


def department_report():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT department,
               COUNT(*),
               ROUND(AVG(salary), 2),
               SUM(salary)
        FROM employees
        GROUP BY department
        ORDER BY department
    """)

    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    return rows


def above_average_report():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT employee_id, name, department, salary
        FROM employees
        WHERE salary > (
            SELECT AVG(salary) FROM employees
        )
        ORDER BY salary DESC
    """)

    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    return rows


def export_csv():
    os.makedirs("output", exist_ok=True)

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT employee_id, name, department, salary
        FROM employees
        ORDER BY employee_id
    """)

    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    with open(
        "output/cleaned_employees.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow([
            "employee_id", "name", "department", "salary"
        ])
        writer.writerows(rows)

    return len(rows)
