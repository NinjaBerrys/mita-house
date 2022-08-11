import re  # imports re module
from guizero import *  # imports guizero

import_list = []
schedule_list = []
y = []
x = 0


def set_activity():
    activity = input_activity_box.value
    return activity


def insert_activity():
    def save_schedule_list():
        with open("load_file", "w") as save_file:
            for task in schedule_list:
                save_file.write("%s\n" % task)
            print("done")

    def reset():
        schedule_list.remove(event)
        activity_1_box.destroy()
        print(schedule_list)
        app.update()

    subject = set_activity()
    time_values = duration_to_time()
    activity = [subject]
    activity.extend(time_values)
    schedule_list.append(activity)
    print(schedule_list)
    # for activities in schedule_list:
    #     hours = activities[1]
    PushButton(stats_box, text="save", command=save_schedule_list)
    for index, event in enumerate(schedule_list):
        activity_1_box = Box(schedule_box, layout="grid", grid=[index, 0])
        Text(activity_1_box, text=event[0], grid=[0, 0])
        Text(activity_1_box, text="{}h:{}m".format(event[1], event[2]), grid=[0, 1])
        Box(activity_1_box, grid=[0, 2])
        PushButton(activity_1_box, text="delete", grid=[1, 2], command=reset)

        stats_text.value = "your schedule is {}h:{}m long with {} separate activities".format(event[1], event[2],
                                                                                              len(schedule_list))
        app.update()
    return schedule_list


def duration_to_time():
    duration = duration_box.value.split(":")
    duration_in_hours = re.sub("\D", "", duration[0])
    duration_in_minutes = re.sub("\D", "", duration[1])
    time_values = [duration_in_hours, duration_in_minutes]
    return time_values


def load_schedule_file():
    def save_schedule_list():
        with open("save_file", "w") as save_file:
            for task in schedule_list:
                save_file.write("%s\n" % task)
            print("done")

    with open("load_file", "r") as load_file:
        for line in load_file:
            pursuit = line[:-1]
            pursuit.replace('"', "")
            list(pursuit)
            import_list.append(pursuit)
        for i in import_list:
            y.append(eval(i))
        print(y)
    PushButton(stats_box, text="save", command=save_schedule_list)
    for index, event in enumerate(y):
        activity_1_box = Box(schedule_box, layout="grid", grid=[index, 0])
        Text(activity_1_box, text=event[0], grid=[0, 0])
        Text(activity_1_box, text="{}h:{}m".format(event[1], event[2]), grid=[0, 1])
        Box(activity_1_box, grid=[0, 2])

        stats_text.value = "your schedule is {}h:{}m long with {} separate activities".format(event[1], event[2],
                                                                                              len(y))
        app.update()


app = App(bg="grey")
content_box = Box(app, layout="grid", align="top", width='fill')
input_activity_box = TextBox(content_box, text="", grid=[0, 0], command=set_activity)
duration_options = ["0h:15m", "0h:30m", "0h:45m", "1h:00m", "1h:15m", "1h:30m", "1h:45m", "2h:00m", "2h:15m",
                    "2h"":30m", "2h:45m", "3h:00m"]
duration_box = Combo(content_box, options=duration_options, grid=[1, 0], command=duration_to_time)
insert_button = PushButton(content_box, text="insert", grid=[2, 0], command=insert_activity)
load_button = PushButton(content_box, text='load', grid=[3, 0], command=load_schedule_file)

schedule_box = Box(app, layout="grid", )
schedule_box.bg = "red"

stats_box = Box(app)
stats_box.bg = "green"
stats_text = Text(stats_box, text="your schedule is 0h:0m long with 0 activities")

app.display()
