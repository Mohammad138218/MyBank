import sqlite3

from kivy.app import App

import os

from kivy.app import App


def get_database_path():

    app = App.get_running_app()

    if app:

        return os.path.join(
            app.user_data_dir,
            "bank.db"
        )

    else:

        return "bank.db"
    
DATABASE_NAME = "bank.db"

def connect():

    return sqlite3.connect(
        get_database_path()
    )


def create_database():

    connection = connect()

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        bank TEXT NOT NULL,

        type TEXT NOT NULL,

        amount INTEGER NOT NULL,

        description TEXT,

        date TEXT

    )
    """)

    connection.commit()
    connection.close()


def add_transaction(bank, transaction_type, amount, description, date):

    connection = connect()

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO transactions
    (bank,type,amount,description,date)

    VALUES(?,?,?,?,?)
    """,
    (
        bank,
        transaction_type,
        amount,
        description,
        date
    ))

    connection.commit()
    connection.close()


def get_report(bank):

    connection = connect()

    cursor = connection.cursor()

    cursor.execute("""
    SELECT type,SUM(amount)

    FROM transactions

    WHERE bank=?

    GROUP BY type
    """,
    (bank,))

    result = cursor.fetchall()

    connection.close()

    return result


def get_all_transactions(bank):

    connection = connect()

    cursor = connection.cursor()

    cursor.execute("""
    SELECT
        id,
        type,
        amount,
        description,
        date

    FROM transactions

    WHERE bank=?

    ORDER BY id DESC
    """,
    (bank,))

    rows = cursor.fetchall()

    connection.close()

    return rows


def get_transaction(transaction_id):

    connection = connect()

    cursor = connection.cursor()

    cursor.execute("""
    SELECT *

    FROM transactions

    WHERE id=?
    """,
    (transaction_id,))

    row = cursor.fetchone()

    connection.close()

    return row


def update_transaction(transaction_id,
                       transaction_type,
                       amount,
                       description):

        connection = connect()

        cursor = connection.cursor()

        cursor.execute("""

        UPDATE transactions

        SET

            type=?,

            amount=?,

            description=?

        WHERE id=?

        """,
        (

            transaction_type,

            amount,

            description,

            transaction_id

        ))

        connection.commit()

        connection.close()


def delete_transaction(transaction_id):

    connection = connect()

    cursor = connection.cursor()

    cursor.execute("""
    DELETE FROM transactions

    WHERE id=?
    """,
    (transaction_id,))

    connection.commit()
    connection.close()