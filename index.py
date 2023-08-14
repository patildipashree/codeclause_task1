from tkinter import Button, Entry, Frame, Label, LabelFrame, Tk
import string
from secrets import choice
from tkinter.constants import END

UPPERCASE = list(string.ascii_uppercase)
LOWERCASE = list(string.ascii_lowercase)
NUMBER = list(string.digits)
SYMBOLS = ['@', '#', '$', '%', '&', '_']
class PasswordGenerator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Random Password Generator")
        self.window.geometry("500x500")
        self.window.configure(bg='skyblue')
        # Label Frame
        self.label_frame = LabelFrame(
            self.window, text="Enter the number of characters")
        self.label_frame.pack(pady=50)
        # Entry box for number of characters
        self.length_entry_box = Entry(self.label_frame, width=40)
        self.length_entry_box.pack(padx=40, pady=40)
        # Declaring feedback if no length is found
        self.feedback = Label(self.window)
        # Entry box for password
        self.password_entry_box = Entry(
            self.window, text="", width=30)
        self.password_entry_box.pack(pady=30)
        # Frame for buttons
        self.button_frame = Frame(self.window)
        self.button_frame.pack(pady=30)
        # Generate Password Button
        generate_btn = Button(
            self.button_frame, text="Generate Password", command=self.generate_random_password)
        generate_btn.grid(row=0, column=0, padx=20)
        # Copy Password Button
        copy_btn = Button(self.button_frame,
                          text="Copy Password", command=self.copy_password)
        copy_btn.grid(row=0, column=1, padx=20)
        
    def generate_random_password(self):
        self.password_entry_box.delete(0, END)
        try:
            password_length = int(self.length_entry_box.get())
            self.feedback.destroy()  # Destroy feedback if length is there
            data = UPPERCASE+LOWERCASE+NUMBER + SYMBOLS
            password = ''.join(choice(data) for _ in range(password_length))
            self.password_entry_box.insert(0, password)
        except ValueError:
            self.feedback = Label(self.window, fg="red",
                                  text="Please enter number of characters")
            self.feedback.place(x=150, y=120)
            
    def copy_password(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.password_entry_box.get())
        
if __name__ == '__main__':
    PasswordGenerator().window.mainloop()