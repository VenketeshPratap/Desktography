import tkinter as tk
from subprocess import Popen, PIPE
import webbrowser

def run_game():
    process = Popen(['python', 'Balloon Popper\\Balloon.py'], stdout=PIPE, stderr=PIPE, text=True)
    stdout, stderr = process.communicate()
    if stderr:
        print("Error:", stderr)
    else:
        print(stdout)

def run_keyboard():
    webbrowser.open('Keyboard\\css3d_keyboard.html')
    
def run_calc():
    webbrowser.open('Calculator\\index.html')

def main():
    app = tk.Tk()
    app.title("Desktopography Showcase")

    # Set the background color and window size
#    ......
    # Create a label for the title
    # .....
    # Create buttons with custom styles
#    .....
    button_keyboard = tk.Button(app, text="Keyboard", command=run_keyboard, bg="#2196F3", fg="white", font=("Bauhaus 93", 34))
    button_keyboard.pack(pady=20)

    button_calc = tk.Button(app, text="Calculator", command=run_calc, bg="#f44336", fg="white", font=("Bauhaus 93", 34))
    button_calc.pack(pady=20)

    app.mainloop()