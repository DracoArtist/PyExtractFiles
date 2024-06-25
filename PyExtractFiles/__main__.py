import tkinter as tk
from text import text
import os
import shutil


class SetUpGUI:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.geometry('700x700')
        self.window.title('Extract files')
        self.setup()
        self.window.mainloop()

    def setup(self):
        # Backgroung
        self.background = '#333333'
        self.window.configure(bg=self.background)

        # Frame to center everything
        self.frame = tk.Frame(bg=self.background)
        self.frame.pack()

        # Title bar
        self.title = tk.Label(self.frame, text="Welcome to Extract Files!", fg='#FF3399', font=("Arial", 30))
        self.title.grid(row=0, column=0, columnspan=3, sticky='news', pady=30)

        # Text bar
        self.instructions = tk.Text(
            self.frame,
            fg='#FFFFFF',
            font=("Arial")
        )
        self.instructions.insert(
            index=tk.END,
            chars=text
        )
        self.instructions.grid(row=1, column=0, columnspan=3, sticky='news', pady=20)

        # Entry bars
        self.source = tk.Label(self.frame, text="source_directory")
        self.source.grid(row=2, column=0)
        self.source_entry = tk.Entry(self.frame)
        self.source_entry.grid(row=2, column=1, columnspan=2, sticky='news')

        self.target = tk.Label(self.frame, text="target_directory")
        self.target.grid(row=3, column=0)
        self.target_entry = tk.Entry(self.frame)
        self.target_entry.grid(row=3, column=1, columnspan=2, sticky='news')

        self.default_extension = tk.StringVar(value='.pdf')
        self.file_extension_label = tk.Label(self.frame, text="file extension")
        self.file_extension_label.grid(row=4, column=0)
        self.file_extension_entry = tk.Entry(self.frame, textvariable=self.default_extension)
        self.file_extension_entry.grid(row=4, column=1, columnspan=2, sticky='news')

        # Command button
        self.button = tk.Button(self.frame, text="Extract files", command=self.extraction)
        self.button.grid(row=5, column=0, columnspan=3, sticky='news', pady=20)

    def extraction(self):
        self.source_directory = self.source_entry.get()
        self.target_directory = self.target_entry.get()
        self.file_extension = self.file_extension_entry.get()

        for root, dirs, files in os.walk(self.source_directory):
            for name in files:
                self.original_file_path = os.path.join(root, name)
                self.copied_file_path = os.path.join(self.target_directory, name)
                self.make_copy(
                )

    def make_copy(self):
        if self.copied_file_path.endswith(self.file_extension):
            shutil.copyfile(self.original_file_path, self.copied_file_path)


def main():
    SetUpGUI()


if __name__ == "__main__":
    main()

# -
