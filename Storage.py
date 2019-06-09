import sqlite3
from datetime import date

journal_database = "journal.db"
current_date = date.today().strftime("%m/%d/%Y")




def add_new_entry(entry_note_title, entry_note_text):
    connection = sqlite3.connect(journal_database)
    cursor = connection.cursor()
    journal_values = (current_date, entry_note_title, entry_note_text,)
    cursor.execute('INSERT INTO journal VALUES (?,?,?)', journal_values)
    connection.commit()
    connection.close()


def display_all_entries():
    connection = sqlite3.connect(journal_database)
    cursor = connection.cursor()
    all_entries = cursor.execute('SELECT * FROM journal').fetchall()
    connection.close()
    return all_entries



if __name__ == "__main__":
    None

    # current_date = date.today().strftime("%m/%d/%Y")
    # connection = sqlite3.connect(journal_database)
    # cursor = connection.cursor()
    # # Create table
    # cursor.execute('''CREATE TABLE IF NOT EXISTS journal
    #              (date text, title text, journaltext text)''')
    #
    # display_all_entries()
    # connection.close()
