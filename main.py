"""
Simple text processor for writers with some extensions
like statistics and synonym finder in the 1.0 version

Author: Denis 'Des Kitten' Trebushnikov
Test version with Tkinter, Pyside will be later... probably
"""

import tkinter as tk


def open_file():
    fhand = open('text.txt', "r")
    txt = ""
    for line in fhand.readlines():
        txt += str(line)
    return txt


class Window:
    def __init__(self, master):
        self.master = master

        # LABEL FRAME
        self.top_frame = tk.Frame(self.master)
        self.top_frame.pack(expand=None, fill=tk.BOTH, side=tk.TOP)

        # LABEL
        self.label_var = tk.StringVar()
        self.label_var.set("Textention -- the software for writers. Some features will come soon.")
        self.label = tk.Label(self.top_frame, textvariable=self.label_var)
        self.label.pack()

        # FOR WORD COUNT STATISTICS
        self.left_frame = tk.Frame(self.master)
        self.left_frame.pack(expand=None, fill=tk.Y, side=tk.LEFT)

        # TEXT WINDOW / next split horiz by prev and current draft
        self.right_frame = tk.Frame(self.master)
        self.right_frame.pack(expand=True, fill=tk.BOTH, side=tk.RIGHT)

        # ENABLE THE SCROLLBAR AT TEXT WINDOW
        self.scrolly = tk.Scrollbar(self.right_frame)
        self.scrolly.pack(side=tk.RIGHT, fill=tk.Y)

        # TEXT WINDOW / undo(ctrl+z) work for ENG keyboard only
        self.text = tk.Text(self.right_frame, wrap=tk.WORD, undo=True, yscrollcommand=self.scrolly.set)
        self.text.pack(expand=True, fill=tk.BOTH)
        self.scrolly.config(command=self.text.yview)

        # BUTTONS FOR TESTING LOGIC
        self.load_btn = tk.Button(self.left_frame, text="Save", command=self.save_txt, width=7)
        self.load_btn.pack(side=tk.TOP, anchor=tk.NW, padx=5, pady=5)

        self.load_btn = tk.Button(self.left_frame, text="Delete", command=self.clear_all, width=7)
        self.load_btn.pack(side=tk.TOP, anchor=tk.NW, padx=5, pady=5)

        self.load_btn = tk.Button(self.left_frame, text="Load", command=self.load_txt, width=7)
        self.load_btn.pack(side=tk.TOP, anchor=tk.NW, padx=5, pady=5)

    # BUTTONS FUNCTIONALITY
    def save_txt(self):
        """
        save the value to write in file...
        from the 1st line start from 1char to the END without '\n' char
        """
        print(self.text.get("1.0", "end - 1c"))
        w_txt = self.text.get("1.0", "end - 1c")
        w_fhand = open("text.txt", "w")
        w_fhand.writelines(w_txt)
        w_fhand.close()

    def clear_all(self):
        self.text.delete("1.0", "end")

    def load_txt(self):
        """
        load the txt from the txt file into Text widget
        """
        self.text.insert("1.0", open_file() + '\n')


root = tk.Tk()
window = Window(root)
root.title("Textension version 0.Agatha.Tk.1")
if __name__ == "__main__":
    root.mainloop()
