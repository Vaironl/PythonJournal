import sqlite3
from datetime import date


def add_new_entry(entry_note_title, entry_note_text):
    journal_values = (current_date, entry_note_title, entry_note_text,)
    cursor.execute('INSERT INTO journal VALUES (?,?,?)', journal_values)
    connection.commit()


def display_all_entries():
    all_entries = cursor.execute('SELECT * FROM journal').fetchall()

    print("=====All entries displayed here======")
    for entry in all_entries:
        print(entry)

    print(current_date)


if __name__ == "__main__":
    journal_database = "journal.db"
    current_date = date.today().strftime("%m/%d/%Y")
    connection = sqlite3.connect(journal_database)
    cursor = connection.cursor()
    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS journal
                 (date text, title text, journaltext text)''')

    display_all_entries()
    connection.close()
