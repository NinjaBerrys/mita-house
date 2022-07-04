from guizero import App, Box, Text, CheckBox, Combo, PushButton, TextBox, Drawing
import re

schedule_list = []
x = 0


def set_activity():
    activity = input_activity_box.value
    return activity


def insert_activity():
    subject = set_activity()
    time_values = duration_to_time()
    activity = [subject]
    activity.extend(time_values)
    schedule_list.append(activity)
    print(schedule_list)
    for index, x in enumerate(schedule_list):
        activity_1_box = Box(schedule_box, layout="grid", grid=[index, 0])
        activity_1_name = Text(activity_1_box, text=x[0], grid=[0, 0])
        activity_1_duration = Text(activity_1_box, text="{}h:{}m".format(x[1],x[2]), grid=[0, 1])
        activity_1_grab_area = Box(activity_1_box, grid=[0, 2])
        activity_1_delete = Text(activity_1_box, text="delete", grid=[1, 2])
        app.update()


def duration_to_time():
    duration = duration_box.value.split(":")
    duration_in_hours = re.sub("\D", "", duration[0])
    duration_in_minutes = re.sub("\D", "", duration[1])
    time_values = [duration_in_hours, duration_in_minutes]
    return time_values


app = App(bg="grey")
content_box = Box(app, layout="grid", align="top", width='fill')
input_activity_box = TextBox(content_box, text="", grid=[0, 0], command=set_activity)
duration_options = ["0h:15m", "0h:30m", "0h:45m", "1h:00m", "1h:15m", "1h:30m", "1h:45m", "2h:00m", "2h:15m",
                    "2h"":30m", "2h:45m", "3h:00m"]
duration_box = Combo(content_box, options=duration_options, grid=[1, 0], command=duration_to_time)
insert_button = PushButton(content_box, text="insert", grid=[2, 0], command=insert_activity)

schedule_box = Box(app, layout="grid", )
schedule_box.bg = "red"

app.display()
