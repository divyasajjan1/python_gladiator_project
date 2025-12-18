# python_gladiator_project
Players analysis using python and DB connections (postgres/sqlite)
# Marvel & DC Teams Project

This project demonstrates how to store, manage, and query data for fictional sports teams: **Team Marvel** and **Team DC**. It showcases both **Python object-oriented programming** and **database implementation** using **SQLite** and **PostgreSQL**.

---

## Project Overview

- Two teams: **Marvel** and **DC**, each with 5 players.
- Each player has the following attributes:
  - Name
  - Height (cm)
  - Weight (kg)
  - Games Played
- The project includes Python scripts to:
  - Store the data using classes (without a database)
  - Perform queries such as:
    - Probability of selection from teams
    - Filter players by weight, height, and games played
    - Identify players with high total stats
- Database scripts for:
  - SQLite (`Marvel_DC_SQliteDB.py`)
  - PostgreSQL (`Marvel_DC_postgres.py`)

---

## Files

| File | Description |
|------|-------------|
| `Marvel_DC_project.py` | Python OOP implementation of team data and queries |
| `Marvel_DC_SQliteDB.py` | SQLite database implementation |
| `Marvel_DC_postgres.py` | PostgreSQL database implementation |
| `marvel_dc.db` | Sample SQLite database file |
| `Python Gladiator Project.docx` | Project notes / documentation |

---

## Features

- Object-oriented approach to store and query team data
- SQL queries for filtering and analyzing players
- Database implementations in SQLite and PostgreSQL
- Can handle dynamically provided data for future extensions

---

## How to Run

1. **Python Scripts**
   - Requires Python 3.x
   - Run using:
     ```bash
     python Marvel_DC_project.py
     ```

2. **SQLite**
   - Requires `sqlite3` module (built-in in Python)
   - Run `Marvel_DC_SQliteDB.py` to create database and run queries.

3. **PostgreSQL**
   - Requires `psycopg2` module
   - Update database credentials in `Marvel_DC_postgres.py`
   - Run script to create tables, insert data, and execute queries.

---

## Technologies Used

- Python 3
- SQLite
- PostgreSQL
- SQL queries for data analysis
