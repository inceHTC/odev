from tkinter import Label, Tk
import time
window = Tk()
window.geometry("490x180")
window.resizable(1,1)

text= ("Roboto", 80, 'bold')
background = "#0F0F0F"
foreground= "#f1f1f1"
border = 30

label = Label(window, font=text, bg=background, fg=foreground, bd=border)
label.grid(row=0, column=1)

def digitalClock():
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live)
   label.after(200, digitalClock)

digitalClock()
window.mainloop()
