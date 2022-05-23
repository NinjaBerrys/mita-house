from guizero import App, Box, Text, CheckBox, Combo, PushButton, TextBox, Drawing

app = App(bg="green")

top_box = Box(app, layout="grid")
schedule_button = PushButton(top_box, text="schedule", grid=[0, 0])
note_taking_button = PushButton(top_box, text="note taking", grid=[1, 0])
calendar_button = PushButton(top_box, text="calendar", grid=[2, 0])
sign_in_button = PushButton(top_box, text="sign in", grid=[3, 0])

top_and_middle_dividing_line = Drawing(app, width="fill", align="top")
top_and_middle_dividing_line.line(0, 10, 2000, 10, color="black", width=1)

content_box = Box(app, layout='grid', align="top", width='fill')
activity_box = TextBox(content_box, text="input activity", grid=[0, 0])
duration_box = Combo(app, options=["0h:15m", "0h:30m", "0h:45m", "1h:00m", "1h:15m", "1h:30m", "1h:45m", "2h:00m", "2h:15m", "2h"":30m", "2h:45m", "3h:00m"])

app.display()
