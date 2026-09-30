# Digital Clock
import tkinter as tk
from time import strftime
root = tk.Tk()                              # 1. Create window
root.title("Digital Clock")                 # 2. Give it a name
label = tk.Label(root, font=('calibri',20,'bold'), bg='pink', fg='white')
label.pack()                                # 3. Show label
def time():                                 # 4. Make clock
    label.config(text="Hello Manu\n The time is " + strftime('%H:%M:%S %p\n%A, %B %d, %Y'))
    label.after(1000, time)                 # 5. Update every second
time(); root.mainloop()                     # 6. Start clock