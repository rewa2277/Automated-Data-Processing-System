
import mysql.connector

import os
import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": os.getenv("MYSQL_PASSWORD")
}

DATABASE_NAME = "automated_data_system"


def connect_database():
    return mysql.connector.connect(
        **DB_CONFIG,
        database=DATABASE_NAME
    )


def create_database():
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS automated_data_system"
    )

    cursor.close()
    connection.close()

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            department VARCHAR(50) NOT NULL,
            salary DECIMAL(10, 2) NOT NULL
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()


def save_employees(employees):
    connection = connect_database()
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM employees")

        sql = """
            INSERT INTO employees
            (employee_id, name, department, salary)
            VALUES (%s, %s, %s, %s)
        """

        values = [
            (
                e["employee_id"],
                e["name"],
                e["department"],
                e["salary"]
            )
            for e in employees
        ]

        cursor.executemany(sql, values)
        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()


def get_all_employees():
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

    return rows
