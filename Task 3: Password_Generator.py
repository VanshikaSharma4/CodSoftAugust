import random
import string
import PySimpleGUI as sg


upper = random.sample(string.ascii_uppercase, 2)
lower = random.sample(string.ascii_lowercase, 2)
digits = random.sample(string.digits, 2)
symbols = random.sample(string.punctuation, 2)

result = upper + lower + digits + symbols
result = random.sample(result, len(result))
result = "".join(result)
print(result)

sg.theme("LightBlue")
sg.set_options(font="verdana 15")


layout = [
    [sg.Text("Uppercase: "), sg.Push(), sg.Input(size=14, key="-UP-")],
    [sg.Text("Lowercase: "), sg.Push(), sg.Input(size=14, key="-LOW-")],
    [sg.Text("Digits: "), sg.Push(), sg.Input(size=14, key="-DIG-")],
    [sg.Text("Symbols: "), sg.Push(), sg.Input(size=14, key="-SYMB-")],
    [sg.Button("Okay"), sg.Button("Cancel"), sg.Push()],
    [
        sg.Text("Password"),
        sg.Push(),
        sg.Multiline(size=14, no_scrollbar=True, disabled=True, key="-PASS-"),
    ],
]

window = sg.Window("Password Generator", layout)
while True:
    event, values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
    if event == "Okay":
        try:
            u_upper = int(values["-UP-"])
            upper = random.sample(string.ascii_uppercase, u_upper)
            u_lower = int(values["-LOW-"])
            lower = random.sample(string.ascii_lowercase, u_lower)
            u_digits = int(values["-DIG-"])
            digits = random.sample(string.digits, u_digits)
            u_symbols = int(values["-SYMB-"])
            symbols = random.sample(string.punctuation, u_symbols)

            result = upper + lower + digits + symbols
            result = random.sample(result, len(result))
            result = "".join(result)
            window["-PASS-"].update(result)
        except ValueError:
            window["-PASS-"].update("Insert valid input!")


window.close()
