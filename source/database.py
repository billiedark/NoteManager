import sqlite3


class NoteDatabase:
    def __init__(self, db_path='notes.db'):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL
                )
            ''')

    def add_note(self, title, content):
        if not title or not content:
            raise ValueError("Title and content cannot be empty.")

        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
            connection.commit()

    def get_all_notes(self):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM notes')
            return cursor.fetchall()

    def search_notes(self, keyword):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM notes WHERE title LIKE ? OR content LIKE ?', (f'%{keyword}%', f'%{keyword}%'))
            return cursor.fetchall()

    def delete_note(self, note_id):
        try:
            note_id = int(note_id)
        except ValueError:
            raise ValueError("Invalid note ID. Please enter a valid integer ID.")

        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT id FROM notes WHERE id = ?', (note_id,))
            result = cursor.fetchone()

            if not result:
                raise ValueError(f"Note with ID {note_id} does not exist.")

            cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
            connection.commit()
