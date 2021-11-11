import tkinter
from tkinter import ttk
from tkinter.constants import INSERT
import pyperclip
import random

class password:
            def __init__(self,password,lenght, master):
                self.password = password
                self.length = lenght


            def vowel_numbers():
                password = keyword.get()
                password = password.replace("a","4").replace("e","3").replace('i','1').replace('o','0').replace('u','5')
                return keyword.insert(0,password)

            def special_word(password):
                # characters to check if the password entered have, so it can be changed
                chars1 = set('is')
                chars2 = set('a.')
                chars3 = set('ec')

                if any((i in chars1)for i in password):
                            
                    password = password.replace('i','!').replace('s','$')
                    return password

                elif any((i in chars2)for i in password):
                            
                    password = password.replace('.','*').replace('a','@')
                    return password

                elif any((i in chars3)for i in password):
                            
                    password = password.replace('e','&').replace('c','ç')
                    return password

                else:
                    pass

                return password

            def captalization(password):
                return password[0].upper()

            def password_generator(length):
                length = 8
                pass_data = "qwertyuiopasdfgjklzxcvbnm1234567890[];',./!@#$%^&*()_+:<>?"
                password = "".join(random.sample(pass_data, length))
                return keyword.insert(0,password)

            def pronouceble_password(length):
                with open(f"{length}code.txt") as file:
                    word = file.readline()
                    





def copy_code():
    pyperclip.copy(text_bar)
    spam = pyperclip.paste()
    return spam

def create_input_frame(container):

    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=2)
    frame.columnconfigure(0, weight=3)

    # Find what
    global text_bar 
    text_bar = str()
    global keyword

    ttk.Label(frame, text='Password').grid(column=0, row=0, sticky=tkinter.W)
    keyword = ttk.Entry(frame, width=50,textvariable= text_bar)
    text_bar = text_bar
    keyword.focus()
    keyword.grid(column=0, row=1, sticky=tkinter.W)
    
   

    # Match Case checkbox
    match_case = tkinter.StringVar()
    match_case_check = ttk.Checkbutton(
        frame,
        text='Change for Numbers',
        variable=match_case,
        command=lambda: password.vowel_numbers(text_bar))
    match_case_check.grid(column=0, row=2, sticky=tkinter.W)

    # Wrap Around checkbox
    wrap_around = tkinter.StringVar()
    wrap_around_check = ttk.Checkbutton(
        frame,
        variable=wrap_around,
        text='Wrap around',
        command=lambda: print(wrap_around.get()))
    wrap_around_check.grid(column=0, row=3, sticky=tkinter.W)


    

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=5)

    return frame


def create_button_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Find Next').grid(column=0, row=0)
    ttk.Button(frame, text='copy', command= lambda: copy_code()).grid(column=0, row=1)
    ttk.Button(frame, text='Random',command= lambda: password.password_generator).grid(column=0, row=2)
    ttk.Button(frame, text='Cancel').grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=3)

    return frame


def create_main_window():

    # root window
    root = tkinter.Tk()
    root.title('Replace')
    root.geometry('450x150')
    root.resizable(0, 0)
   
    #function for the clipboard
    



    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=2)

    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)

    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0)

    root.mainloop()


if __name__ == "__main__":
    create_main_window()