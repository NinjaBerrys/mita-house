from guizero import App, Box, Text, CheckBox, Combo, PushButton, TextBox, Drawing

app = App(bg="green", width=1134, height=565)

top_box = Box(app, layout="grid")
schedule_button = PushButton(top_box, text="schedule", grid=[0, 0])
note_taking_button = PushButton(top_box, text="note taking", grid=[1, 0])
calendar_button = PushButton(top_box, text="calendar", grid=[2, 0])
sign_in_button = PushButton(top_box, text="sign in", grid=[3, 0])

# top_and_middle_dividing_line = Drawing(app, width="fill", align="top")
# top_and_middle_dividing_line.line(0, 10, 2000, 10, color="black", width=1)

content_box = Box(app, layout="grid", align="top", width="fill", height="fill", border=True)
folder_box = Box(content_box, grid=[0, 0], align="top", border=True)
file_box = Box(content_box, layout="grid", grid=[1, 0], border=True, align="top", height=325)
note_box = Box(content_box, width=646, height=325, grid=[2, 0], border=True, align="top")
stats_box = Box(app)

folder_1_pushbutton = PushButton(folder_box, grid=[0, 0], text="folder 1")
folder_2_pushbutton = PushButton(folder_box, grid=[0, 1], text="folder 2")
folder_3_pushbutton = PushButton(folder_box, grid=[0, 2], text="folder 3")

file_1_pushbutton = PushButton(file_box, grid=[0, 0], text="file 1")
file_2_pushbutton = PushButton(file_box, grid=[0, 1], text="file 2")
file_3_pushbutton = PushButton(file_box, grid=[0, 2], text="file 3")

note_taking_box = TextBox(note_box, text="Born in a World of Strife", width=646)
statistics_box = Text(stats_box, text="words = 0\ntime working : 4h:30m")

app.display()
