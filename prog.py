import tkinter as tk

def clicked():
    print("I am not at the bottom")

main_window = tk.Tk()
main_window.title("Rectangle")
main_window.geometry('250x300')

click_button = tk.Button(main_window, text="I am at top", command=clicked)
click_button.pack(side="top")

main_window.mainloop()