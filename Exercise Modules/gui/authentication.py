import tkinter as tk
from canvas import app
from utilities import clean_screen
from products import render_prod
from pathlib import Path
import json

def login(username, password):
    file_path = Path(__file__).parent / "db" / "user.txt"
    
    with open(file_path, "r") as file:
        data = file.readlines()
        for line in data:
            name, pwd = line.strip().split(", ")
            if username == name and password == pwd:
                with open("Exercise Modules/gui/db/current_user.txt", "w") as file:
                    file.write(username)
                render_prod()
                return
        
        render_login_screen(error="Invalid user name or password")
        
        

def render_login_screen(error=None):
    clean_screen()
    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app)
    password.grid(row=1, column=0)
    
    tk.Button(
        app,
        text = "Enter",
        bg="green",
        fg="black",
        command=lambda: login(username.get(), password.get()),
    ).grid(row=2, column=0)
    
    if error:
        tk.Label(app, text=error).grid(row=3, column=0)

def register(**user):
    # TODO validations
    users_path = Path(__file__).parent / "db" / "users.txt"
    user_cred = Path(__file__).parent / "db" / "user.txt"
    user.update({"products": []})
    with open(user_cred, "a+") as file:
        users = [line.split(", ")[0] for line in file]
        if user["username"] in users:
            register_screen(error="User already exits in database")
            return
        file.write(f"{user["username"]}, {user["password"]}\n")
    
    with open(users_path, "a") as file:
        file.write(json.dumps(user) + "\n")
        print()
    
    render_login_screen()
 

def register_screen(error=None):
    clean_screen()
    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app)
    password.grid(row=1, column=0)
    first_name = tk.Entry(app)
    first_name.grid(row=2, column=0)
    last_name = tk.Entry(app)
    last_name.grid(row=3, column=0)
    
    tk.Button(
    app,
    text = "Register",
    bg="green",
    fg="black",
    command=lambda: register(username=username.get(), password=password.get(), first_name=first_name.get(),last_name=last_name.get()),
    ).grid(row=4, column=0)
    
    tk.Label(app, text=error).grid(row=5, column=0)

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
            fg="black",
            command=register_screen
        ).grid(row=0, column=1)
    