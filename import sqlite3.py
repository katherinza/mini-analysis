import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import warnings

DB_FILE = "tgu_practice_db.db"

matplotlib.rcParams["font.family"] = "DejaVu Sans"
matplotlib.rcParams["figure.dpi"]  = 110
warnings.filterwarnings("ignore")

conn = sqlite3.connect(DB_FILE)

def sql(query):
    """Выполняет SQL-запрос → возвращает pandas DataFrame."""
    return pd.read_sql_query(query, conn)

print("Подключение к базе данных установлено")
print(f"   SQLite : {sqlite3.sqlite_version}")
print(f"   pandas : {pd.__version__}")