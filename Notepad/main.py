import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button
from tkinter.filedialog import asksaveasfile, asksaveasfilename


class SimpleNotepad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("Bob's notepad")

        self.text_area: Text = Text(self.root, wrap="word")
        self.text_area.pack(expand=True, fill="both")

        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        self.save_button: Button = Button(
            self.button_frame, text="Save", command=self.save_file
        )
        self.save_button.pack(side=tk.LEFT)

        self.load_button: Button = Button(
            self.button_frame, text="Load", command=self.load_file
        )
        self.load_button.pack(side=tk.LEFT)

    def save_file(self) -> None:
        file_path: str = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")]
        )
        with open(file_path, "w") as file:
            file.write(self.text_area.get(1.0, tk.END))

        print(f"File saved to: {file_path}")

    def load_file(self) -> None:
        file_path: str = filedialog.askopenfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")]
        )
        with open(file_path, "r") as file:
            content: str = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.INSERT, content)

        print(f"File loaded to: {file_path}")

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()


if __name__ == "__main__":
    main()
