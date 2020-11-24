from tkinter.ttk import Frame, Style, Label, Button, Combobox
from tkinter import BOTH, Tk, W, E, S, N, filedialog, Canvas, NW
from PIL import Image, ImageTk

max_h=500
max_w=1000

class Window(Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent=parent
        self.start()


    def reload_image(self):
        self.image=ImageTk.PhotoImage(self.im)
        self.canvas.create_image(0,0, image=self.image, anchor=NW)

    def load_image(self):
        path=filedialog.askopenfilename(initialdir='/', title='Select file', filetypes=(('jpeg.files','*.jpg'),('all files','*.*')))
        self.im=Image.open(path)
        self.scbtn.config(state='normal')
        self.sbtn.config(state='normal')
        self.fbtn.config(state='normal')
        self.bbtn.config(state='normal')
        self.orginal_image=self.im
        self.reload_image()

    def save_image(self):
        path=filedialog.asksaveasfilename(initialdir='/', title='Select file', defaultextension='.jpg', filetypes=(('jpeg.files','*.jpg'),('all files','*.*')) )
        self.im.save(path)

    def start(self):
        self.parent.title("IMG Viewer")
        self.style=Style()
        self.style.theme_use("winnative")
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(1, weight=1)
        #label=Label(self, text="Label:")
        #label.grid(sticky=W, pady=4, padx=5, row=1)

        opbtn=Button(self, text="Open", command=self.load_image)
        opbtn.grid(row=0, column=0, sticky=W)

        self.sbtn=Button(self, text="Save", command=self.save_image)
        self.sbtn.grid(row=0, column=1, sticky=W)
        self.sbtn.config(state='disabled')

        self.scbox=Combobox(self, values='0.1 0.2 0.3 0.4')
        self.scbox.grid(row=1, column=1, padx=3, pady=4, sticky=W)

        self.fcbox=Combobox(self, values='BLUR CONTOUR EMBOSS')
        self.fcbox.grid(row=2, column=1, padx=3, pady=4, sticky=W)

        self.scbtn=Button(self, text='Scale')
        self.scbtn.grid(row=1, column=0, padx=3, pady=4, sticky=W)
        self.scbtn.config(state='disabled')

        self.fbtn=Button(self, text='Filter')
        self.fbtn.grid(row=2, column=0, padx=3, pady=4, sticky=W)
        self.fbtn.config(state='disabled')

        self.canvas=Canvas(self, width=max_w, height=max_h)
        self.canvas.grid(row=3, column=0, padx=3, pady=4, sticky=E+W+S+N, columnspan=3)

        self.bbtn=Button(self, text='Reverse')
        self.bbtn.grid(row=2, column=2, padx=3, pady=4, sticky=W + N)
        self.bbtn.config(state='disabled')



def main():
    gui=Tk()
    gui.geometry("1000x700")


    app=Window(gui)
    gui.mainloop()

if __name__ == '__main__':
    main()