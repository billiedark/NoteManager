from colorama import init

init(autoreset=True)


class NoteManagerUI:
    def __init__(self, note_database):
        self.note_database = note_database

    def show_menu(self):
        print("\nNote Manager Menu:")
        print("1. Add a new note")
        print("2. View all notes")
        print("3. Search for a note")
        print("4. Delete a note")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            self.add_note_prompt()
        elif choice == '2':
            self.display_notes(self.note_database.get_all_notes())
        elif choice == '3':
            self.search_notes_prompt()
        elif choice == '4':
            self.delete_note_prompt()
        elif choice == '5':
            exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    def add_note_prompt(self):
        print("\033c")

        print("\nAdd a New Note:")
        title = input("Enter the title: ")
        content = input("Enter the content: ")
        self.note_database.add_note(title, content)
        print("Note added successfully!")

    def display_notes(self, notes):
        print("\033c")

        print("\nAll Notes:")
        if not notes:
            print("No notes available.")
        else:
            for note in notes:
                print(f"ID: {note[0]}, Title: {note[1]}")
                print(f"Content: {note[2]}\n")

    def search_notes_prompt(self):
        print("\033c")

        keyword = input("Enter a keyword to search for: ")
        notes = self.note_database.search_notes(keyword)
        self.display_notes(notes)

    def delete_note_prompt(self):
        note_id = input("Enter the ID of the note to delete: ")
        try:
            note_id = int(note_id)
            self.note_database.delete_note(note_id)
            print(f"Note with ID {note_id} deleted successfully!")
        except ValueError:
            print("Invalid input. Please enter a valid note ID.")
