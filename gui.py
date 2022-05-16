from tkinter import *

root = Tk()
root.geometry("1133x564")

top_frame = Frame(root)
top_frame.grid(row=0, column=0)

schedule_button = Button(top_frame, text="schedule")
schedule_button.grid(row=0, column=0)

note_taking_button = Button(top_frame, text="note taking")
note_taking_button.grid(row=0, column=1)

calendar_button = Button(top_frame, text="calendar")
calendar_button.grid(row=0, column=2)

sign_in_button = Button(top_frame, text="sign in")
sign_in_button.grid(row=0, column=3)

content_frame = Frame(root)
content_frame.grid(row=1, column=0)



root.mainloop()
