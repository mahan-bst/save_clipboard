from PIL import ImageGrab
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

im = ImageGrab.grabclipboard()
Tk().withdraw()
path = asksaveasfilename(defaultextension='.png', filetypes=[('images', '*.png')], title='where save screen shot')

if im is not None:
    im.save(path, 'PNG')
else:
    print('your clipboard doesnt have image')
