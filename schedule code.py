import re  # imports re module
from guizero import *  # imports guizero

schedule_list = []  # creates the list called schedule_list
import_list = []  # creates the list called import_list
y = []  # creates the list called y because I didn't know what to name it


def set_activity():  # defines the function set_activity
    activity = input_activity_box.value  # creates the variable activity called activity and sets its value to the
    # value inside of input_activity_box
    return activity  # returns the variable activity


def insert_activity():  # defines the function insert_activity
    def save_schedule_list():  # defines the function save_schedule_list inside of insert_activity
        with open("load_file", "w") as save_file:  # creates load_file
            for task in schedule_list:  # for every task in schedule list write it inside of load_file
                save_file.write("%s\n" % task)
            save_file.close()  # closes load_file

    def delete():  # defines the function delete
        schedule_list.remove(event)  # removes the item from schedule_list list
        activity_1_box.destroy()  # destroys the box in which all the activities are in
        app.update()  # updates the app so that the change is visible

    subject = set_activity()  # creates the subject variable and makes it equal to the result of the set_activity
    # function
    time_values = duration_to_time()  # creates the time_values variable and makes it equal to the result of the
    # duration_to_time function
    activity = [subject]  # creates list called activity with subject inside
    activity.extend(time_values)  # appends time values to the end of activity
    schedule_list.append(activity)  # appends the activity list into the schedule_list list
    PushButton(stats_box, text="save", command=save_schedule_list)  # creates button which saves schedule_list
    for index, event in enumerate(schedule_list):  # enumerates the list (assigns an index to each of the items)
        activity_1_box = Box(schedule_box, layout="grid", grid=[index, 0])  # creates a box inside the schedule_box
        # box for the task to be put inside and places the box index away from the left edge of the schedule_box box
        Text(activity_1_box, text=event[0], grid=[0, 0])  # shows the name of the activity
        Text(activity_1_box, text="{}h:{}m".format(event[1], event[2]),
             grid=[0, 1])  # shows the duration of the activity
        PushButton(activity_1_box, text="delete", grid=[1, 2],
                   command=delete)  # creates a button for the delete function

        stats_text.value = "you have scheduled {} separate activities".format(len(schedule_list))  # shows the amount
        # of activities the user has made
        app.update()  # updates the app so that changes are visible


def duration_to_time():  # defines the duration_to_time function
    duration = duration_box.value.split(":")  # calls the value of duration_box and splits it in half from the ':'
    # into a list consisting of the hours and minutes in string representation
    duration_in_hours = re.sub("\D", "", duration[0])  # removes all non number characters to the hour item
    duration_in_minutes = re.sub("\D", "",
                                 duration[1])  # removes all non number characters to the minute item
    time_values = [duration_in_hours, duration_in_minutes]  # creates a list featuring duration_in_hours and
    # duration_in_minutes
    return time_values  # returns the time_values list


def load_schedule_file():  # defines the load_schedule_file function
    def save_schedule_list():  # defines the save_schedule_list function inside the load_schedule_file function
        with open("load_file", "w") as save_file:  # creates load_file
            for task in y:  # for every task in y write it inside of load_file
                save_file.write("%s\n" % task)
            save_file.close()  # closes load_file

    def delete():  # defines the function delete
        schedule_list.remove(event)  # removes the item from schedule_list list
        activity_1_box.destroy()  # destroys the box in which all the activities are in
        app.update()  # updates the app so that the change is visible

    with open("load_file", "r") as load_file:  # opens the load_file in read mode as load_file
        for line in load_file:
            pursuit = line[:-1]  # removes linebreak
            import_list.append(pursuit)  # appends pursuit to import_list list
        for i in import_list:
            y.append(eval(i))  # look inside test files/string to list test file.py for more information
    PushButton(stats_box, text="save", command=save_schedule_list)  # creates button which saves y
    for index, event in enumerate(y):  # enumerates the list (assigns an index to each of the items)
        activity_1_box = Box(schedule_box, layout="grid", grid=[index, 0])  # creates a box inside the schedule_box
        # box for the task to be put inside and places the box index away from the left edge of the schedule_box box
        Text(activity_1_box, text=event[0], grid=[0, 0])  # shows the name of the activity
        Text(activity_1_box, text="{}h:{}m".format(event[1], event[2]), grid=[0, 1])  # shows the duration of the
        # activity
        PushButton(activity_1_box, text="delete", grid=[1, 2], command=delete)  # creates a button for the delete
        # function

        stats_text.value = "you have scheduled {} separate activities".format(len(y))  # shows the amount
        # of activities the user has made
        app.update()  # updates the app so that changes are visible


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
