
import csv

def process_csv(filename):
    employees = []
    seen_ids = set()
    total = 0
    duplicates = 0
    invalid = 0

    with open(filename, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += 1

            try:
                emp_id = int(row["employee_id"])
                name = row["name"].strip()
                department = row["department"].strip()
                salary = float(row["salary"])

                if emp_id <= 0 or not name or not department or salary < 0:
                    raise ValueError

                if emp_id in seen_ids:
                    duplicates += 1
                    continue

                seen_ids.add(emp_id)

                employees.append({
                    "employee_id": emp_id,
                    "name": name,
                    "department": department,
                    "salary": salary
                })

            except (ValueError, TypeError, KeyError):
                invalid += 1

    stats = {
        "total": total,
        "cleaned": len(employees),
        "duplicates": duplicates,
        "invalid": invalid
    }

    return employees, stats

