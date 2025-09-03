class TextEditor:
    def __init__(self):
        self.document = ""
        self.undo_stack = []
        self.redo_stack = []

    def make_change(self, change):
        self.undo_stack.append(self.document)
        self.document += change
        self.redo_stack.clear()
        print("\nChange made.")
        self.display_state()

    def undo_action(self):
        if self.undo_stack:
            self.redo_stack.append(self.document)
            self.document = self.undo_stack.pop()
            print("\nUndo performed.")
        else:
            print("\nNo more actions to undo.")
        self.display_state()

    def redo_action(self):
        if self.redo_stack:
            self.undo_stack.append(self.document)
            self.document = self.redo_stack.pop()
            print("\nRedo performed.")
        else:
            print("\nNo more actions to redo.")
        self.display_state()

    def display_state(self):
        print("Current Document State: '" + self.document + "'")

    def run_editor(self):
        while True:
            print("\n--- MENU ---")
            print("1. Make a Change")
            print("2. Undo")
            print("3. Redo")
            print("4. Display Document State")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                change = input("Enter text to add: ")
                self.make_change(change)
            elif choice == '2':
                self.undo_action()
            elif choice == '3':
                self.redo_action()
            elif choice == '4':
                self.display_state()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")

# Run the editor
editor = TextEditor()
editor.run_editor()

