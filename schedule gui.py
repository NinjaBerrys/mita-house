from guizero import App, Box, Text, CheckBox, Combo, PushButton, TextBox, Drawing

app = App(bg="green", width=1134, height=565)

top_box = Box(app, layout="grid")
schedule_button = PushButton(top_box, text="schedule", grid=[0, 0])
note_taking_button = PushButton(top_box, text="note taking", grid=[1, 0])
calendar_button = PushButton(top_box, text="calendar", grid=[2, 0])
sign_in_button = PushButton(top_box, text="sign in", grid=[3, 0])

top_and_middle_dividing_line = Drawing(app, width="fill", align="top")
top_and_middle_dividing_line.line(0, 10, 2000, 10, color="black", width=1)

content_box = Box(app, layout="grid", align="top", width='fill')
input_activity_box = TextBox(content_box, text="input activity", grid=[0, 0])
duration_options = ["0h:15m", "0h:30m", "0h:45m", "1h:00m", "1h:15m", "1h:30m", "1h:45m", "2h:00m", "2h:15m",
                    "2h"":30m", "2h:45m", "3h:00m"]
duration_box = Combo(content_box, options=duration_options, grid=[1, 0])
insert_button = PushButton(content_box, text="insert", grid=[2, 0])

schedule_box = Box(app, layout="grid", width="fill", grid=[0, 1])
schedule_box.bg = "red"

activity_1_box = Box(schedule_box, layout="grid", grid=[0, 0])
activity_1_name = Text(activity_1_box, text="activity 1", grid=[0, 0])
activity_1_duration = Text(activity_1_box, text="1h:15m", grid=[0, 1])
activity_1_grab_area = Box(activity_1_box, grid=[0, 2])
activity_1_delete = Text(activity_1_box, text="delete", grid=[1, 2])

activity_2_box = Box(schedule_box, layout="grid", grid=[1, 0])
activity_2_name = Text(activity_2_box, text="activity 2", grid=[0, 0])
activity_2_duration = Text(activity_2_box, text="1h:30m", grid=[0, 1])
activity_2_grab_area = Box(activity_2_box, grid=[0, 2])
activity_2_delete = Text(activity_2_box, text="delete", grid=[1, 2])

activity_3_box = Box(schedule_box, layout="grid", grid=[2, 0])
activity_3_name = Text(activity_3_box, text="activity 3", grid=[0, 0])
activity_3_duration = Text(activity_3_box, text="0h:30m", grid=[0, 1])
activity_3_grab_area = Box(activity_3_box, grid=[0, 2])
activity_3_delete = Text(activity_3_box, text="delete", grid=[1, 2])

bottom_box = Box(app, align="bottom", width="fill", layout="auto")
bottom_box.bg = "Blue2"
schedule_stats = Text(bottom_box, text="your schedule is 3h:15m long with 3 separate activities", grid=[0, 0])
timer_checkbox = CheckBox(bottom_box, text="timer", grid=[1, 0])
start_button = PushButton(bottom_box, text="start", grid=[2, 0], align="right")
app.display()
