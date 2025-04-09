import tkinter
# def button():

win = tkinter.Tk()
win.geometry('400x400')
btn = tkinter.Button(win, text = 'btn', background='white')
btn.config(width = 5, height= 2)
btn.config(text = "button")
# btn.config(command = parking())
btn.pack()

win.mainloop()