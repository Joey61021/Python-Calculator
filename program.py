import math
import re
from tkinter import *

author = "Joey"
version = '1.0.0'
program = "Calculator"

base = Tk()
base.resizable(0, 0)
base.geometry("520x725")  # Adjust as needed
base.title(f'{program} {version}')
base.configure(bg="black")

bg_col = "#121212"

input_value = StringVar()

button_images = []
constants = [{'expression': 'e', 'value': math.e},
             {'expression': 'pi', 'value': math.pi},
             {'expression': 'sin', 'value': 'math.sin'},
             {'expression': 'cos', 'value': 'math.cos'},
             {'expression': 'tan', 'value': 'math.tan'},
             {'expression': 'log', 'value': 'math.log10'}]
buttons = [[{'img': '7', 'action': '7'}, {'img': '8', 'action': '8'}, {'img': '9', 'action': '9'}, {'img': 'c', 'action': 'clear'}, {'img': 'del', 'action': 'del'}],
           [{'img': '4', 'action': '4'}, {'img': '5', 'action': '5'}, {'img': '6', 'action': '6'}, {'img': 'x', 'action': '*'}, {'img': 'div', 'action': '/'}],
           [{'img': '1', 'action': '1'}, {'img': '2', 'action': '2'}, {'img': '3', 'action': '3'}, {'img': '+', 'action': '+'}, {'img': '-', 'action': '-'}],
           [{'img': '0', 'action': '0'}, {'img': '(', 'action': '('}, {'img': ')', 'action': ')'}, {'img': 'decimal', 'action': '.'}, {'img': '=', 'action': 'equals'}],
           [{'img': 'sin', 'action': 'sin('}, {'img': 'cos', 'action': 'cos('}, {'img': 'tan', 'action': 'tan('}, {'img': 'log', 'action': 'log('}],
           [{'img': 'pi', 'action': 'pi'}, {'img': 'e', 'action': 'e'}, {'img': 'pwr', 'action': '**'}, {'img': 'abs', 'action': 'abs('}]]


def convert_constants(value):
    for constant in constants:
        if constant['expression'] in value:
            value = re.sub(r'(?<=\d)' + constant['expression'], '*' + constant['expression'], value)
            value = value.replace(constant['expression'], str(constant['value']))
    return value


def click_button(value):
    if value == 'equals':
        if not input_value.get():  # No input
            return
        try:
            result = eval(convert_constants(input_value.get()))

            # TODO
            # input_value.set(str("{:.2e}".format(result)) if len(str(result)) > 10 else result)

            input_value.set(result)
        except Exception as err:  # noqa
            print(err)
            input_value.set("Error")
        return

    if value == 'clear':
        input_value.set('')
        return

    if value == 'del':
        input_value.set(input_value.get()[:-1])
        return

    input_value.set(input_value.get() + str(value))


def load_ui():
    input_frame = Frame(base, width=335, height=75, bg="black", highlightbackground="black", highlightcolor="black")
    input_frame.pack(side=TOP)

    input_label = Label(input_frame, font=('arial', 45), textvariable=input_value, bg="black", fg="white")
    input_label.pack(ipady=15)

    frame = Frame(base, width=312, height=272.5, bg=bg_col)
    frame.pack()

    for row in range(0, len(buttons)):
        for col in range(0, len(buttons[row])):
            try:
                img = PhotoImage(file=rf'assets\{buttons[row][col]["img"]}.png').subsample(3, 3)
                button_images.append(img)

                Button(frame, text="", image=img, bd=0, bg=bg_col, cursor="hand2",
                       command=lambda action=buttons[row][col]['action']: click_button(action)).grid(row=row, column=col, padx=1, pady=1)
            except Exception:  # noqa
                continue


if __name__ == '__main__':
    print(f'{program} {version} by {author} has started')

    load_ui()
    base.mainloop()
