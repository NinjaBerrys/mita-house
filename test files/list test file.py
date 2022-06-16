schedule_list = []


def set_activity():
    subject = input("activity")
    # print(subject)
    return subject


def set_duration():
    time = input("duration")
    # print(time)
    return time


def create_activity():
    subject = set_activity()
    time = set_duration()
    activity = [subject,time]
    print(activity)


create_activity()
