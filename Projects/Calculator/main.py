from tkinter import *
from tkinter import ttk


def display(arg):
  global values
  values += arg
  value.set(values)
  
def calculate():
  global values
  try:
    result = eval(values)
    value.set(result)
    if str(result).endswith(".0") :
      result = int(result) 
    values = str(result)
  except:
    value.set("Operação inválida")
    values = ""
  
def clear_screen():
  global values
  values = ""
  value.set("")


# Colors
black = "#201e26"
gray = "#e6e6e6"
gray2 = "#4f4e57"
orange= "#ff9705"
white = "#ffffff"

# Window and frames
window = Tk()
window.title("Calculator")
window.geometry("290x350")
window.config(bg=black)

frame_display = Frame(window, width=290, height=70)
frame_display.grid(row=0, column=0)

frame_body = Frame(window, width=290, height=285)
frame_body.grid(row=1, column=0)

# Variables
value = StringVar()
values = ""

# Labels
app_label = Label(frame_display, textvariable=value, width=20, height=3, anchor="e",justify=RIGHT, font=("Ivi 18"), bg=gray2, fg=white, relief=FLAT, padx=5)
app_label.place(x=0, y=0)

# Buttons
clear = Button(frame_body, command = clear_screen, text="C", width=13, height=2, bg=gray, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
clear.place(x=3, y=3)
mod = Button(frame_body, command = lambda: display("%"), text="%", width=6, height=2, bg=gray, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
mod.place(x=145, y=3)
div = Button(frame_body, command = lambda: display("/"), text="/", width=6, height=2, fg=white, bg=orange, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
div.place(x=217, y=3)


seven = Button(frame_body, command = lambda: display("7"), text="7", width=6, height=2, bg=gray, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
seven.place(x=3, y=58)
eight = Button(frame_body, command = lambda: display("8"), text="8", width=6, height=2, bg=gray, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
eight.place(x=74, y=58)
nine = Button(frame_body, command = lambda: display("9"), text="9", width=6, height=2, bg=gray, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
nine.place(x=145, y=58)
multi = Button(frame_body, command = lambda: display("*"), text="*", width=6, height=2, fg=white, bg=orange, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
multi.place(x=217, y=58)


four = Button(frame_body, command = lambda: display("4"), text="4", width=6, height=2, bg=gray, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
four.place(x=3, y=113)
five = Button(frame_body, command = lambda: display("5"), text="5", width=6, height=2, bg=gray, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
five.place(x=74, y=113)
six = Button(frame_body, command = lambda: display("6"), text="6", width=6, height=2, bg=gray, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
six.place(x=145, y=113)
sub = Button(frame_body, command = lambda: display("-"), text="-", width=6, height=2, fg=white, bg=orange, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
sub.place(x=217, y=113)


one = Button(frame_body, command = lambda: display("1"), text="1", width=6, height=2, bg=gray, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
one.place(x=3, y=168)
two = Button(frame_body, command = lambda: display("2"), text="2", width=6, height=2, bg=gray, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
two.place(x=74, y=168)
three = Button(frame_body, command = lambda: display("3"), text="3", width=6, height=2, bg=gray, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
three.place(x=145, y=168)
sum = Button(frame_body, command = lambda: display("+"), text="+", width=6, height=2, fg=white, bg=orange, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
sum.place(x=217, y=168)


zero = Button(frame_body, command = lambda: display("0"), text="0", width=13, height=2, bg=gray, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
zero.place(x=3, y=223)
dot = Button(frame_body, command = lambda: display("."), text=".", width=6, height=2, bg=gray, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
dot.place(x=145, y=223)
equal = Button(frame_body, command = calculate, text="=", width=6, height=2, fg=white, bg=orange, font=("Ivy 13 bold"), relief=RAISED, overrelief=RIDGE)
equal.place(x=217, y=223)


window.mainloop()