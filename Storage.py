import sqlite3
from datetime import date

journal_database = "journal.db"

current_date = date.today().strftime("%m/%d/%Y")

connection = sqlite3.connect(journal_database)

cursor = connection.cursor()

# Create table
cursor.execute('''CREATE TABLE journal
             (date text, title text, journaltext text)''')

# Insert a row of data
note_title = "My First Journal entry"
note_text = "My first journal entry's text"
journal_values = (current_date, note_title, note_text,)
cursor.execute('INSERT INTO journal VALUES (?,?,?)', journal_values)

connection.commit()

connection.close()
