import PySimpleGUI as sg

layout = [
    [sg.Text("Hello!")],
    [sg.Text("Input name:", key="update")],
    [sg.Input(tooltip="Input here", key="Name")],
    [sg.Button("Submit"), sg.Button("Exit")]
]

# Create the Window
window = sg.Window('Hello World!', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    print(f"Events: {event}\nValues: {values}")
    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == "Submit":
        window["update"].update(window["update"].get() + values["Name"])

window.close()