
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Python\Budget-Tracker\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("500x400")
window.configure(bg = "#F7EEDD")

expenses = 1400

def submit_handler():
    global expenses
    new_expense_amt = float(entry_2.get())
    expenses += new_expense_amt
    canvas.itemconfig(tagOrId=expenses_text, text=f"${expenses}")

canvas = Canvas(
    window,
    bg = "#F7EEDD",
    height = 400,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    500.0,
    70.0,
    fill="#008DDA",
    outline="")

canvas.create_text(
    21.0,
    6.0,
    anchor="nw",
    text="Budget Tracker",
    fill="#FFFFFF",
    font=("JacquesFrancois Regular", 45 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    117.0,
    105.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    243.0,
    175.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    369.0,
    105.0,
    image=image_image_3
)

canvas.create_text(
    30.0,
    84.0,
    anchor="nw",
    text="Income",
    fill="#000000",
    font=("JacquesFrancois Regular", 15 * -1)
)

canvas.create_text(
    30.0,
    154.0,
    anchor="nw",
    text="Balance",
    fill="#000000",
    font=("JacquesFrancois Regular", 15 * -1)
)

canvas.create_text(
    282.0,
    84.0,
    anchor="nw",
    text="Expenses",
    fill="#000000",
    font=("JacquesFrancois Regular", 15 * -1)
)

canvas.create_text(
    29.0,
    101.0,
    anchor="nw",
    text="$40000",
    fill="#000000",
    font=("IstokWeb Regular", 20 * -1)
)

canvas.create_text(
    29.0,
    171.0,
    anchor="nw",
    text="$10000",
    fill="#000000",
    font=("IstokWeb Regular", 20 * -1)
)

expenses_text = canvas.create_text(
    281.0,
    101.0,
    anchor="nw",
    text="$4000",
    fill="#000000",
    font=("IstokWeb Regular", 20 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    395.0,
    306.0,
    image=image_image_4
)

canvas.create_text(
    24.0,
    212.0,
    anchor="nw",
    text="Add Expenses",
    fill="#000000",
    font=("JockeyOne Regular", 15 * -1)
)

canvas.create_text(
    23.0,
    238.0,
    anchor="nw",
    text="Name",
    fill="#000000",
    font=("JejuGothic", 13 * -1)
)

canvas.create_text(
    24.0,
    287.0,
    anchor="nw",
    text="Amount($)",
    fill="#000000",
    font=("JejuGothic", 13 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    118.5,
    270.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C3C3C3",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=36.0,
    y=258.0,
    width=165.0,
    height=22.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    119.5,
    319.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C3C3C3",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=37.0,
    y=307.0,
    width=165.0,
    height=22.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=submit_handler,
    relief="flat"
)
button_1.place(
    x=29.0,
    y=351.0,
    width=244.0,
    height=30.0
)
window.resizable(False, False)
window.mainloop()