from guizero import App, Picture, PushButton


def change_image():
    gif1 = Picture(app, image="img/KeyUnlinedDevilfish-mobile.gif")


app = App()
gif1 = Picture(app, image="img/egg.gif")

button = PushButton(app, text="Press me", command=change_image)

app.display()
