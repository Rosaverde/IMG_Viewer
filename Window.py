from tkinter.ttk import Frame, Style, Label, Button
from tkinter import BOTH, Tk, W, E, S, N, filedialog

class Window(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.start()

    def start(self):
        self.parent.title("IMG Viewer")
        self.style=Style()
        self.style.theme_use("winnative")
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(1, weight=1)
        label=Label(self, text="Label:")
        label.grid(sticky=W, pady=4, padx=5)

        opbtn=Button(self, text="Open")
        opbtn.grid(row=1, column=3)

        self.sbtn=Button(self, text="Save")
        self.sbtn.grid(row=2, column=3)
        self.sbtn.config(state='disabled')

def main():
    gui=Tk()
    gui.geometry("1000x700")
    #gui.filename=filedialog.askopenfilename(initialdir='/', title='Select file', filetypes=(('jpeg.files','*.jpg'),('all files','*.*')))
    #gui.filename=filedialog.asksaveasfilename(initialdir='/', title='Select file', filetypes=(('jpeg.files','*.jpg'),('all files','*.*')))
    app=Window(gui)
    gui.mainloop()

if __name__ == '__main__':
    main()