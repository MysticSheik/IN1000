# Oppgave 3.1
from ezgraphics import GraphicsWindow

diameter = 75
radius = diameter / 2

win = GraphicsWindow()
canvas = win.canvas()

canvas.setFill("red")
canvas.setColor("red")
canvas.drawOval(canvas.width() / 2 - radius, canvas.height() / 2 - radius, 75, 75)

win.wait()
