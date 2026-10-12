import tkinter as tk
from canvas import app
from utilities import clean_screen

def render_login_screen():
    clean_screen()
    
def render_main_screen():
    tk.Button(
        app,
        text="Login",
        bg="green",
        fg="white",
        command=render_login_screen
    ).grid(row=0, column=0)
    
    tk.Button(
            app,
            text="Register",
            bg="yellow",
            fg="black"
            
        ).grid(row=0, column=1)