from guizero import App, Waffle

app = App()
x=7
y=10
my_waffle = Waffle(app,height=13,width=13)
my_waffle.pixel(x,y).color = "red"
my_waffle[x,y].dotty = True

app.display()