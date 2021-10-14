from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('hi bb wassup?')

my_face = ImageTk.PhotoImage(Image.open("C:\Users\Pichau\Downloads\MVIMG_20211006_223221.jpg"))

my_label = Label(image = my_face)
my_label.grid(row=0,column=0,columnspan=3)


def back():
    global my_label
    global forward
    global back

    my_label.grid_forget()



def forward():
    global my_label
    global forward
    global back


button_quit = Button(root, text="Exit Program", command=root.quit)
button_next = Button(root, text= '>>',command= next)
button_back = Button(root,text='<<' , command= lambda: forward())



button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_next.grid(row=1,column=2)


root.mainloop()