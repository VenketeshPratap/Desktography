import tkinter as tk
from subprocess import Popen, PIPE

def run_code():
    process = Popen(['python', 'Testing\\Code.py'], stdout=PIPE, stderr=PIPE, text=True)
    stdout, stderr = process.communicate()
    if stderr:
        print("Error:", stderr)
    else:
        print(stdout)

app = tk.Tk()
app.title("Desktopography")

# Set the background color and window size


# Create a label for the title


# Create buttons with custom styles


app.mainloop()