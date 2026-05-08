import os

DB_FILE = "tgu_practice_db.db"

if os.path.exists(DB_FILE):
    print(f"База данных найдена: {DB_FILE}  ({os.path.getsize(DB_FILE)//1024} KB)")
else:
    print(f"БД не найдена: {DB_FILE}")