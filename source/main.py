from database import NoteDatabase
from ui import NoteManagerUI


def main():
    note_db = NoteDatabase()
    ui = NoteManagerUI(note_db)

    while True:
        ui.show_menu()


if __name__ == "__main__":
    main()
