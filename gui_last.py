from tkinter import *
from tkinter import filedialog
import customtkinter
from FileScanner import start_scan


def run_scan():
    # Ask the user to choose a folder
    folder_path = filedialog.askdirectory(title="Select Folder to Scan")
    if folder_path:
        print(f"Scanning folder: {folder_path}")
        start_scan(folder_path)
        print("Scan completed!")

#Set the theme and color options
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

#root = Tl()
root = customtkinter.CTk()

root.title("mamriot.com")
root.iconbitmap("C:\\Users\\Cyber_Mamriot\\Desktop\\mamriot26\\LOL\\035a98_5ad0c97f57d241e1ae923d6940a2439e~mv2.ico")

root.geometry('800x400')

my_button = customtkinter.CTkButton(
    root,
    text="Check virus!",
    fg_color="#ff69b4",  # bright pink
    hover_color="#ff85c1",  # slightly lighter pink when hovering
    command=run_scan
)
my_button.pack(pady=80)

root.mainloop()