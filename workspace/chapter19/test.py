from swampy.Gui import *

g = Gui()
g.title('Gui')

button = g.bu(text='Press me.')
label = g.la(text = 'Press the button.')
def make_label():
    g.la(text='Thank you.')
    
button2 = g.bu(text='No , press me!', command=make_label)

canvas = g.ca(width=500, height = 500)
canvas.config(bg="red")
item= canvas.circle([30,0], 60, fill="green")
g.mainloop()