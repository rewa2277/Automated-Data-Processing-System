
import mysql.connector

from processor import process_csv
from database import (
    create_database,
    save_employees,
    get_all_employees
)
from reports import department_report, above_average_report, export_csv


def main():
    create_database()
    print("MySQL connected successfully!")

    while True:
        print("\n--- AUTOMATED DATA PROCESSING SYSTEM ---")
        print("1. Import and clean CSV")
        print("2. View all employees")
        print("3. Department-wise report")
        print("4. Above-average salary report")
        print("5. Export cleaned data")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                employees, stats = process_csv("employees.csv")

                if not employees:
                    print("No valid records found.")
                    continue

                save_employees(employees)

                print("Import completed!")
                print("Total rows:", stats["total"])
                print("Cleaned records:", stats["cleaned"])
                print("Duplicates skipped:", stats["duplicates"])
                print("Invalid rows skipped:", stats["invalid"])

            elif choice == "2":
                for employee in get_all_employees():
                    print(employee)

            elif choice == "3":
                for row in department_report():
                    print(row)

            elif choice == "4":
                for row in above_average_report():
                    print(row)

            elif choice == "5":
                count = export_csv()
                print("Exported", count, "records to output/cleaned_employees.csv")

            elif choice == "6":
                print("Thank you!")
                break

            else:
                print("Please enter a number from 1 to 6.")

        except (ValueError, OSError, mysql.connector.Error) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
