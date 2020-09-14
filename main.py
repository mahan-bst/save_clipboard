from PIL import ImageGrab
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
import sys
import time
import os
im = ImageGrab.grabclipboard()
Tk().withdraw()
if len(sys.argv) == 1:
    path = asksaveasfilename(defaultextension='.png',
                             filetypes=[('images', '*.png')],
                             title='where save screen shot',
                             initialfile='screenShot.png')
else:
    path = sys.argv[1]
    path = os.path.join(path, str(time.time())+'.png')
if im is not None and path != '':
    im.save(path, 'PNG')
    messagebox.showinfo("done!", "your image saved :)")
elif path == '':
    messagebox.showerror("cancel", "you cancel operation!")
else:
    messagebox.showerror("image doesn't exist", 'i cant find image in your clipboard!')
