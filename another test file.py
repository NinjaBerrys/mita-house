from guizero import App, Slider, TextBox


def slider_changed(slier_vlue):
    textbox.value = slier_vlue


app = App()
slider = Slider(app, command=slider_changed)
textbox = TextBox(app)
app.display()
