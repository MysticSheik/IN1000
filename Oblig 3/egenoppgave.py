# Egenoppgave:
# Skriv et program som tar imot koordinater samt høyde og bredde fra
# bruker, legger disse etter hverandre i en lister og deretter bruker
# innholdet i listen til å tegne opp en form med EzGraphics.
from ezgraphics import GraphicsWindow

win = GraphicsWindow()
canvas = win.canvas()

data = []
data.append(int(input("Skriv inn en x-koordinat: ")))
data.append(int(input("Skriv inn en y-koordinat: ")))
data.append(int(input("Skriv inn en bredde: ")))
data.append(int(input("Skriv inn en høyde: ")))

canvas.drawRectangle(data[0], data[1], data[2], data[3])

win.wait()
