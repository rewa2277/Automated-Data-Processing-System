# Automated Data Processing & Relational Query System

## Overview
A Python and MySQL project that automates employee data cleaning, database storage, SQL reporting, and CSV export.

## Technologies Used
- Python
- MySQL
- SQL
- CSV
- Git and GitHub

## Features
- Reads employee records from a CSV file.
- Validates and cleans employee data.
- Identifies duplicate employee IDs and invalid records.
- Stores valid records in a MySQL database.
- Generates department-wise salary reports.
- Identifies employees earning above the average salary.
- Exports cleaned records to a CSV file.

## Requirements
- Python 3
- MySQL Server
- mysql-connector-python

## Installation
Install the required Python package:

```bash
python -m pip install mysql-connector-python
```

Create the MySQL database connection configuration and set the `MYSQL_PASSWORD` environment variable before running the application.

## Run the Project

```bash
python main.py
```

Follow the menu displayed in the terminal to import data, view records, generate reports, and export cleaned data.

## Learning Outcomes
This project demonstrates Python file handling, data validation, exception handling, MySQL connectivity, SQL queries, and modular programming.