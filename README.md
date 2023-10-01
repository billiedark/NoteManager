# Документация к Note Manager

### Описание:
Программа "Note Manager" представляет собой простой менеджер заметок с использованием базы данных SQLite. Пользователи могут добавлять, просматривать, искать и удалять заметки через консольный интерфейс.

### Структура проекта:
Проект состоит из двух основных модулей: database.py и ui.py. Модуль database.py содержит класс NoteDatabase для управления заметками в базе данных, а модуль ui.py содержит класс NoteManagerUI для взаимодействия с пользователем.

### Требования:
- Python 3.x
- Библиотека sqlite3 (стандартная библиотека Python)
- Библиотека colorama для цветового оформления текста (установить с помощью pip install colorama)

### Запуск программы:
Установите необходимые зависимости, выполнив команду: `pip install colorama`
Запустите программу, выполнив команду: `python main.py`
После запуска, следуйте инструкциям в консоли для выполнения различных операций.

### Основные операции:

##### Добавление новой заметки:
- Выберите "1" в меню и введите заголовок и содержание заметки.

##### Просмотр списка всех заметок:
- Выберите "2" в меню.

##### Поиск заметки:
- Выберите "3" в меню и введите ключевое слово для поиска.

##### Удаление заметки:
- Выберите "4" в меню и введите ID заметки для удаления.

##### Выход из программы:
- Выберите "5" в меню.

### Тестирование программы:
Программа может быть протестирована с использованием стандартных средств Python для тестирования, таких как unittest или pytest. Создайте тестовые сценарии для каждого метода, проверяя их корректность и обработку ошибок.

### Пример тестирования (используя unittest):
```python
import unittest
from database import NoteDatabase

class TestNoteDatabase(unittest.TestCase):
    def setUp(self):
        self.note_db = NoteDatabase(':memory:')  # Используем временную базу данных для тестирования

    def test_add_note(self):
        self.note_db.add_note("Test Title", "Test Content")
        notes = self.note_db.get_all_notes()
        self.assertEqual(len(notes), 1)

    def test_search_notes(self):
        self.note_db.add_note("Test Note 1", "Content 1")
        self.note_db.add_note("Test Note 2", "Content 2")
        result = self.note_db.search_notes("Test")
        self.assertEqual(len(result), 2)

    def test_delete_note(self):
        self.note_db.add_note("Note to Delete", "Delete me")
        notes_before = self.note_db.get_all_notes()
        self.note_db.delete_note(1)
        notes_after = self.note_db.get_all_notes()
        self.assertEqual(len(notes_before) - 1, len(notes_after))

if __name__ == '__main__':
    unittest.main()

```
