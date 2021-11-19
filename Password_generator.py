from ast import Str
import random
from tkinter import *
import tkinter
import pyperclip
from tkinter import ttk


#function to change the entry displayed
def cleaning_and_setting(password):
    keyword.delete(0,"end")
    keyword.insert(0, password)
    return password

def create_input_frame(container):

    frame = ttk.Frame(container)


    var1 = IntVar()
    
    text_bar= StringVar()
    global keyword

    '''ttk.Label(frame,text='Password').grid(column=0,row=0, sticky=tkinter.W)'''
    keyword = ttk.Entry(frame, width=30, textvariable= text_bar)

    print(text_bar)
    keyword.focus()
    keyword.grid(column= 0, row= 1,columnspan=5, sticky= tkinter.W)
    
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

    def captalization():
        password = keyword.get()
        password = password.capitalize()
        password = cleaning_and_setting(password)
        return password

    def password_generator():
        #length of the password
        length = var1.get()

        pass_data = "qwertyuiopasdfgjklzxcvbnm1234567890[];',./!@#$%^&*()_+:<>?"
        password = "".join(random.sample(pass_data, length))
        
        print(password)
        print(type(password))
        print(len(password))
        password = cleaning_and_setting(password)
        return password

    def vowel_numbers():
        password = keyword.get()
        password = password.replace("a","4").replace("e","3").replace('i','1').replace('o','0').replace('u','5')
        print(password)
        password = cleaning_and_setting(password)
        return password


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

    #Captalize the first letter
    captalize = tkinter.StringVar()
    captalize_check = ttk.Checkbutton(
        frame,
        variable= captalize,
        text="Captalize",
        command=captalization
        )
    captalize_check.grid(column=1,row=2,sticky=tkinter.W)

    #Random word with defined legnth

    random_button = ttk.Button(
        frame,
        text="Random",
        command= password_generator
    )
    random_button.grid(column=1,row=3, sticky= tkinter.W)

    
    #Combo Box for length of the password
    combo = ttk.Combobox(frame, textvariable=var1,width=10)
    combo['values'] = (8,9,10,11,12,13,"Length")
    combo.current(0)
    combo.bind('<<ComboboxSelected>>')
    combo.grid(column=1,row=1,columnspan=2,sticky=tkinter.W)

    def copy_code():
        random_password = keyword.get()
        pyperclip.copy(random_password)

    ttk.Button(frame, text='copy', command= lambda: copy_code()).grid(column=5, row=1, sticky= tkinter.W)
    

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=5)

    return frame




def create_main_window():

    # root window
    root = tkinter.Tk()
    root.title('Replace')
    root.geometry('400x130')
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