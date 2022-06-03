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
folder_box = Box(content_box, grid=[0, 0], align="top", border=True, width=200, height=325)
file_box = Box(content_box, layout="grid", grid=[1, 0], border=True, align="top", height=325)
note_box = Box(content_box, width=646, height=325, grid=[2, 0], border=True, align="top")
stats_box = Box(app)

folder_1_box = Box(folder_box, grid=[0, 0], width=200, height=62, border=True)
folder_2_box = Box(folder_box, grid=[0, 1], width=200, height=62, border=True)
folder_3_box = Box(folder_box, grid=[0, 2], width=200, height=62, border=True)
folder_1_text = Text(folder_1_box, text="folder 1", size=50)
folder_2_text = Text(folder_2_box, text="folder 2", size=50)
folder_3_text = Text(folder_3_box, text="folder 3", size=50)

file_1_box = Box(file_box, grid=[0, 0], width=150, height=50, border=True)
file_2_box = Box(file_box, grid=[0, 1], width=150, height=50, border=True)
file_3_box = Box(file_box, grid=[0, 2], width=150, height=50, border=True)
file_1_text = Text(file_1_box, text="file 1", size=50)
file_2_text = Text(file_2_box, text="file 2", size=50)
file_3_text = Text(file_3_box, text="file 3", size=50)

note_taking_box = TextBox(note_box, text="Born in a World of Strife", width=646)
statistics_box = Text(stats_box, text="words = 0\ntime working : 4h:30m")

app.display()
