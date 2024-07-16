import PySimpleGUI as sg

values = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
table = sg.Table(
    values=values,
    auto_size_columns=False,
)
layout = [
    [sg.Push(), sg.Text("2048!", font=("Times New Roman", 30), text_color="Black"), sg.Push()],
    [sg.Push(), sg.Text("Score:"), sg.Text("0", key="score")],
    [table]
]

# Create the Window
window = sg.Window('Hello World!', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    print(f"Events: {event}\nValues: {values}")
    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED:
        break

    if event == "Submit":
        window["update"].update(window["update"].get() + values["Name"])

window.close()