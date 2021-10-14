from PIL import Image, ImageTk, ImageDraw
from tkinter import ttk, Label


on_color='#2196F3'
off_color = '#cccccc'

# off image
off_im = Image.new('RGBA', (226, 130))
draw = ImageDraw.Draw(off_im)
draw.rounded_rectangle([1, 1, 225, 129], radius=(128/2), fill=off_color)
draw.ellipse([14, 14, 114, 114], fill='white')

# on image
on_im = Image.new('RGBA', (226, 130))
draw = ImageDraw.Draw(on_im)
draw.rounded_rectangle([1, 1, 225, 129], radius=(128/2), fill=on_color)
draw.ellipse([12, 12, 116, 116], fill='white')
on_im = on_im.transpose(Image.ROTATE_180)

# set up application styles
style = ttk.Style()
style.theme_use('clam')

# set the background white
style.configure('white.TFrame', background='white')
window = ttk.Frame(style.master, style='white.TFrame', padding=20)
window.pack(fill='both', expand='yes')

# save reference to images
toggle_off = ImageTk.PhotoImage(off_im.resize((32, 20), Image.LANCZOS))
toggle_on = ImageTk.PhotoImage(on_im.resize((32, 20), Image.LANCZOS))

# create a new image element
style.element_create('rounded.Toolbutton.label', 'image', toggle_on, ('!selected', toggle_off))

# set the new layout
style.layout('rounded.Toolbutton', [
    ('Toolbutton.border', {'sticky': 'nswe', 'children': [
        ('Toolbutton.padding', {'sticky': 'nswe', 'children': [
            ('rounded.Toolbutton.label', {'sticky': 'nswe'})]})]})])

# configure style settings
style.configure('rounded.Toolbutton', relief='flat', borderwidth=0)
style.map('rounded.Toolbutton',
          background=[
              ('selected', 'white'),
              ('!selected', 'white')])


#function for the toggle
def hi():
    myLabel =  Label(window, text = "hello sunshine!")
    myLabel.pack()

    

# demo the new widget
ttk.Checkbutton(window, style='rounded.Toolbutton',command=hi).pack()
window.mainloop()
ttk.Checkbutton(window, style='rounded.Toolbutton',command=).pack()
window.mainloop()
ttk.Checkbutton(window, style='rounded.Toolbutton',command=).pack()
window.mainloop()
