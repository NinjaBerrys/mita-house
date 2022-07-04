from tkinter import *


class test:
    def __init__(self, root):
        self.variables = []
        for i in range(26):
            self.variables.append(StringVar())

        self.labels = []
        self.entrys = []
        for ii in range(26):
            char = str(chr(ord('A') + ii))
            self.labels.append(Label(root, text=char))
            self.labels[-1].grid(padx=0, pady=0, row=ii, column=0)
            self.entrys.append(Entry(root, textvariable=self.variables[ii]))
            self.entrys[-1].grid(padx=0, pady=0, row=ii, column=1)


root = Tk()
root.geometry("200x600+50+50")
T = test(root)
root.mainloop()
