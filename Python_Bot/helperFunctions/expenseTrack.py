import sqlite3
import datetime
from sqlite3 import Error

def connect():
    sqliteConnection = sqlite3.connect('expenses.db')
    cursor = sqliteConnection.cursor()

    # creating table
    table = """ CREATE TABLE IF NOT EXISTS Expenses
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                DATE TEXT,
                TITLE TEXT,
                EXPENSE_TYPE TEXT,
                AMOUNT REAL,
                OPENING_BALANCE REAL);"""
    cursor.execute(table)
    
    print("Table created")
    # sqliteConnection.close()
    return sqliteConnection



def add_expenses(sqliteConnection, data):
    try:
        command = "INSERT INTO Expenses (DATE, TITLE, EXPENSE_TYPE, AMOUNT, OPENING_BALANCE)  VALUES (:DATE, :TITLE, :EXPENSE_TYPE, :AMOUNT, :OPENING_BALANCE)"
        cursor = sqliteConnection.cursor()
        cursor.execute(command, data)
        sqliteConnection.commit()
    except Exception as e:
        print(e)
        cursor.rollback()
        return "Error adding expense"
    finally:
        cursor.close()
    
def view_expenses(sqliteConnection):
    rows = None
    try:
        command = "SELECT * FROM Expenses"
        viewCursor = sqliteConnection.cursor()
        viewCursor.execute(command)
        rows = viewCursor.fetchall()
    except Exception as e:      
        print(e)  
        viewCursor.rollback()
        rows = "Error fetching expenses"
    finally:
        viewCursor.close()
    return rows
