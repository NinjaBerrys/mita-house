from guizero import PushButton, App, Box, TextBox, Window

x = 0


def make_new_window():
    Window(app)


app = App(bg="red")
content_box = Box(app, align="top", width='fill')
button = PushButton(content_box, text="make new window", command=make_new_window)

app.display()
