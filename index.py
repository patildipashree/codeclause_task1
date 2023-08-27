import random  
import tkinter as tk                     
from tkinter import *                    
from tkinter import messagebox as mb    
  
def generate_password(length):   
    list_of_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()/"  
    selected_characters = random.sample(list_of_characters, length)  
    pass_string = "".join(selected_characters)  
    pass_label.config(text = pass_string)  
 
    print("The Password is :", pass_string, "\n")  
  
def select():   
    len = length.get()  
    if len != 0:  
        generate_password(len)   
    else:  
        mb.showerror("Invalid Selection", "Length of Password is not defined.")  
  
def get_length():     
    print("Selected Length of Password :", length.get(), "characters")  
  
def set():  
    length.set(0)  
    pass_label.config(text = "")  
  
# main function  
if __name__ == "__main__":   
    main_root = Tk()   
    main_root.title("Random Password Generator")  
    main_root.geometry("500x500")  
    main_root.config(bg = "#E6E6FA")  
  
    #  some frames  
    heading_frame = Frame(main_root, bg = "#AA96DA")  
    radiobutton_frame = Frame(main_root, bg = "#E6E6FA")  
    button_frame = Frame(main_root, bg = "#E6E6FA")  
    result_frame = Frame(main_root, bg = "#E6E6FA")  
  
    heading_frame.pack(fill = "both")  
    radiobutton_frame.pack(pady = 10)  
    button_frame.pack(pady = 10)  
    result_frame.pack(pady = 10)  
   
    heading = Label(  
        heading_frame,  
        text = "Random Password Generator",  
        font = ("Times New Roman", "50"),  
        bg = "#AA96DA",  
        fg = "#000"  
        )  
  
    subheading = Label(  
        heading_frame,  
        text = "Select the Length of the Password :",  
        font = ("Times New Roman", "25"),  
        bg = "#F0A07C",  
        fg = "#000"  
        )  
        
    heading.pack(pady = 30)  
    subheading.pack(fill = "both")  
    length = IntVar()  
    length.set(0)  
  
    radiobuttonOne = Radiobutton(  
        radiobutton_frame,  
        text = '4 Characters',  
        variable = length,  
        value = 4,  
        font = ("Times New Roman", "18"),  
        bg = "#E6E6FA",  
        command = get_length  
        )  

    radiobuttonTwo = Radiobutton(  
        radiobutton_frame,  
        text = '5 Characters',  
        variable = length,  
        value = 5,  
        font = ("Times New Roman", "18"),  
        bg = "#E6E6FA",  
        command = get_length  
        )  
    
    radiobuttonThree = Radiobutton(  
        radiobutton_frame,  
        text = '6 Characters',  
        variable = length,  
        value = 6,  
        font = ("Times New Roman", "18"),  
        bg = "#E6E6FA",  
        command = get_length  
        )  
      
    radiobuttonFour = Radiobutton(  
        radiobutton_frame,  
        text = '7 Characters',  
        variable = length,  
        value = 7,  
        font = ("Times New Roman", "18"),  
        bg = "#E6E6FA",  
        command = get_length  
        )  
    
    radiobuttonFive = Radiobutton(  
        radiobutton_frame,  
        text = '8 Characters',  
        variable = length,  
        value = 8,  
        font = ("Times New Roman", "18"),  
        bg = "#E6E6FA",  
        command = get_length  
        )  
 
    radiobuttonSix = Radiobutton(  
        radiobutton_frame,  
        text = '9 Characters',  
        variable = length,  
        value = 9,  
        font = ("Times New Roman", "18"),  
        bg = "#E6E6FA",  
        command = get_length  
        )  
   
    radiobuttonSeven = Radiobutton(  
        radiobutton_frame,  
        text = '10 Characters',  
        variable = length,  
        value = 10,  
        font = ("Times New Roman", "18"),  
        bg = "#E6E6FA",  
        command = get_length  
        )  
    
    radiobuttonEight = Radiobutton(  
        radiobutton_frame,  
        text = '12 Characters',  
        variable = length,  
        value = 12,  
        font = ("Times New Roman", "18"),  
        bg = "#E6E6FA",  
        command = get_length  
        ) 
    
    radiobuttonNine = Radiobutton(  
        radiobutton_frame,  
        text = '14 Characters',  
        variable = length,  
        value = 14,  
        font = ("Times New Roman", "18"),  
        bg = "#E6E6FA",  
        command = get_length  
        ) 
    
    radiobuttonTen = Radiobutton(  
        radiobutton_frame,  
        text = '16 Characters',  
        variable = length,  
        value = 16,  
        font = ("Times New Roman", "18"),  
        bg = "#E6E6FA",  
        command = get_length  
        ) 
  
    radiobuttonOne.grid(row = 0, column = 0, padx = 10, pady = 2, sticky = W)  
    radiobuttonTwo.grid(row = 0, column = 1, padx = 10, pady = 2, sticky = W)  
    radiobuttonThree.grid(row = 1, column = 0, padx = 10, pady = 2, sticky = W)  
    radiobuttonFour.grid(row = 1, column = 1, padx = 10, pady = 2, sticky = W)  
    radiobuttonFive.grid(row = 2, column = 0, padx = 10, pady = 2, sticky = W)  
    radiobuttonSix.grid(row = 2, column = 1, padx = 10, pady = 2, sticky = W)  
    radiobuttonSeven.grid(row = 3, column = 0, padx = 10, pady = 2, sticky = W)  
    radiobuttonEight.grid(row = 3, column = 1, padx = 10, pady = 2, sticky = W)  
    radiobuttonNine.grid(row = 4, column = 0, padx = 10, pady = 2, sticky = W) 
    radiobuttonTen.grid(row = 4, column = 1, padx = 10, pady = 2, sticky = W)  
  
    get_pass = Button(  
        button_frame,  
        text = "Get Password",  
        font = ("Times New Roman", "18"),  
        width = 20,  
        bg = "#32CD32",  
        fg = "#000",  
        relief = GROOVE,  
        command = select  
        )  

    clear_all = Button(  
        button_frame,  
        text = "Reset All",  
        font = ("Times New Roman", "18"),  
        width = 20,  
        bg = "#FF0000",  
        fg = "#000",  
        relief = GROOVE,  
        command = set  
        )  
  
    get_pass.grid(row = 0, column = 0, padx = 10, pady = 5)  
    clear_all.grid(row = 0, column = 1, padx = 10, pady = 5)  
  
    pass_label = Label(  
        result_frame,  
        text = "",  
        font = ("Times New Roman", "18", "bold"),  
        bg = "#E6E6FA",  
        fg = "#000"  
        )  
   
    pass_label.pack()  
    main_root.mainloop() 

