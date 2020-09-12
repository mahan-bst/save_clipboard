from PIL import ImageGrab
im = ImageGrab.grabclipboard()
path = input('what path u want to save : ')
if im is not None:
    im.save(path, 'PNG')
else:
    print('your clipboard doesnt have image')