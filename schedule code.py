from guizero import App, Box, Text, CheckBox, Combo, PushButton, TextBox, Drawing

schedule_list = []


def set_activity():
    activity = input_activity_box.value
    print(activity)
    return activity


def create_activity():
    subject = set_activity()
    time = set_duration()
    activity = [subject, time]
    schedule_list.append(activity)
    print(schedule_list)


def duration_to_time(duration):
    duration = duration.split(":")
    duration


app = App(bg="grey")
content_box = Box(app, layout="grid", align="top", width='fill')
input_activity_box = TextBox(content_box, text="", grid=[0, 0], command=set_activity)
duration_options = ["0h:15m", "0h:30m", "0h:45m", "1h:00m", "1h:15m", "1h:30m", "1h:45m", "2h:00m", "2h:15m",
                    "2h"":30m", "2h:45m", "3h:00m"]
duration_box = Combo(content_box, options=duration_options, grid=[1, 0], command=duration_to_time)
insert_button = PushButton(content_box, text="insert", grid=[2, 0], command=create_activity)

app.display()
