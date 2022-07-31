from guizero import App, Window, PushButton


def open_window():
    app.hide()
    window.show()


app = App()
window = Window(app)

button = PushButton(app, command=open_window)

app.display()
