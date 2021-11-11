import random
from tkinter import *
import tkinter

from tkinter import ttk

def cleaning_and_setting(password):
    keyword.delete(0,"end")
    keyword.insert(0, password)
    return password

def create_input_frame(container):
    
    frame = ttk.Frame(container)

    entries = []

    frame.columnconfigure(0, weight=2)
    frame.columnconfigure(0, weight=3)
    text_bar= StringVar()
    global keyword

    ttk.Label(frame,text='password').grid(column=0,row=0, sticky=tkinter.W)
    keyword = ttk.Entry(frame, width=50, textvariable= text_bar)
    entries.append(keyword)
    print(text_bar)
    keyword.focus()
    keyword.grid(column= 0, row= 1, sticky= tkinter.W)
    
    def special_word():
        password = keyword.get()
        # characters to check if the password entered have, so it can be changed
        chars1 = set('is')
        chars2 = set('a.')
        chars3 = set('ec')

        if any((i in chars1)for i in password):
                            
            password = password.replace('i','!').replace('s','$')
            password = cleaning_and_setting(password)
            return password

        elif any((i in chars2)for i in password):

            password = password.replace('.','*').replace('a','@')
            password = cleaning_and_setting(password)
            return password

        elif any((i in chars3)for i in password):
                            
            password = password.replace('e','&').replace('c','ç')
            password = cleaning_and_setting(password)
            return password

        else:
            pass
        
        return password

    def vowel_numbers():
        password = keyword.get()
        password = password.replace("a","4").replace("e","3").replace('i','1').replace('o','0').replace('u','5')
        print(password)
        password = cleaning_and_setting(password)
        return password

    # Return fucntion

    def return_function(text_bar):
        keyword.delete(0,"end")
        return keyword.insert(0, entries[0])
        

     # Change for Numbers checkbox
    change_number = tkinter.StringVar()
    change_number_check = ttk.Checkbutton(
        frame,
        text='Change for Numbers',
        variable=change_number,
        command= vowel_numbers)
    change_number_check.grid(column=0, row=2, sticky=tkinter.W)

    # Special Character checkbox
    special_character = tkinter.StringVar()
    special_character_check = ttk.Checkbutton(
        frame,
        variable=special_character,
        text='Special Character',
        command=special_word)
    special_character_check.grid(column=0, row=3, sticky=tkinter.W)

    # Return checkbox
    return_box = tkinter.StringVar()
    return_box_check = ttk.Checkbutton(
        frame,
        variable=return_box,
        text='Return',
        command= lambda: return_function(text_bar))
    return_box_check.grid(column=1, row=2,sticky=tkinter.W)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=5)

    return frame


def create_button_frame(container):
    frame = ttk.Frame(container)




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


    

    root.mainloop()


if __name__ == "__main__":
    create_main_window()