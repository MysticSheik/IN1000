#          (__)
#          (oo)
#   /-------\/
#  / |     ||
# +  ||----||
#    ~~    ~~
from ezgraphics import GraphicsWindow

win = GraphicsWindow()
can = win.canvas()

teller = 0
x_pos = 10
storrelse = 35

while (teller < 9):
    can.drawOval(x_pos, 100, storrelse, storrelse)
    x_pos += 35
    storrelse += 5
    teller += 1

win.wait()
