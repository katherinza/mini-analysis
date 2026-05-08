import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import warnings
from IPython.display import display

conn = sqlite3.connect("tgu_practice_db.db")
matplotlib.rcParams["font.family"] = "DejaVu Sans"
matplotlib.rcParams["figure.dpi"]  = 110
warnings.filterwarnings("ignore")

def sql(query):
    """Выполняет SQL-запрос → возвращает pandas DataFrame."""
    return pd.read_sql_query(query, conn)

print("Структура таблицы Track:")
display(sql("""select * from country"""))
