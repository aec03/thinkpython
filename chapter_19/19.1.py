from swampy.Gui import *

def make_label():
    g.la(text='Nice Job!')

def make_button():
    g.bu(text='Press me.', command=make_label)

def make_circle():
    canvas.circle([0,0], 100, fill='black')


g = Gui()
g.title('Gui')
canvas = g.ca(width=500, height=500)
canvas.config(bg='red')

button = g.bu(text='Press me.', command=make_circle)

g.mainloop()