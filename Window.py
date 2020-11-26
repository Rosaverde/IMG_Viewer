from tkinter.ttk import Frame, Style, Button, Combobox
from tkinter import BOTH, Tk, W, E, S, N, filedialog, Canvas, NW, messagebox
from PIL import Image, ImageTk, ImageFilter

max_h = 800
max_w = 1000


class Window(Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.start()

    def use_filter(self):
        filter_type = self.fcbox.get()
        if filter_type == 'BLUR':
            self.im = self.im.filter(ImageFilter.BLUR)
        elif filter_type == 'CONTOUR':
            self.im = self.im.filter(ImageFilter.CONTOUR)
        else:
            self.im = self.im.filter(ImageFilter.EMBOSS)
        self.reload_image()

    def reload_image(self):
        wi, he = self.im.size
        factor_wi = 1
        factor_he = 1
        if wi > max_w:
            factor_wi = max_w/wi
        if he > max_h:
            factor_he = max_h/he
        if factor_he >= factor_wi:
            factor = factor_wi
        else:
            factor = factor_he

        size = int(wi*factor), int(he*factor)
        print(size)
        self.image = ImageTk.PhotoImage(self.im.resize(size))
        self.canvas.create_image(0, 0, image=self.image, anchor=NW)

    def load_image(self):
        path = filedialog.askopenfilename(initialdir='/', title='Select file', filetypes=(('jpeg.files', '*.jpg'), ('all files', '*.*')))
        try:
            self.im = Image.open(path)
            self.scbtn.config(state='normal')
            self.sbtn.config(state='normal')
            self.fbtn.config(state='normal')
            self.bbtn.config(state='normal')
            self.original_image = self.im
            self.reload_image()
        except FileNotFoundError:
            messagebox.showerror('Error', 'File does not exist!')
        except OSError:
            messagebox.showerror('Error', 'Provide a graphic file')

    def scale(self):
        w, h = self.im.size
        factor = float(self.scbox.get())
        size = int(w*factor), int(h*factor)
        self.im = self.im.resize(size)
        self.reload_image()

    def restore_image(self):
        self.im = self.original_image
        self.reload_image()

    def save_image(self):
        path = filedialog.asksaveasfilename(initialdir='/', title='Select file', defaultextension='.jpg', filetypes=(('jpeg.files', '*.jpg'), ('all files', '*.*')))
        self.im.save(path)

    def start(self):
        self.parent.title("IMG Viewer")
        self.style = Style()
        self.style.theme_use("winnative")
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(1, weight=1)

        opbtn = Button(self, text="Open", command=self.load_image)
        opbtn.grid(row=0, column=0, sticky=W)

        self.sbtn = Button(self, text="Save", command=self.save_image)
        self.sbtn.grid(row=0, column=1, sticky=W)
        self.sbtn.config(state='disabled')

        self.scbox = Combobox(self, values='0.1 0.2 0.3 0.4')
        self.scbox.current(0)
        self.scbox.grid(row=1, column=1, padx=3, pady=4, sticky=W)

        self.fcbox = Combobox(self, values='BLUR CONTOUR EMBOSS')
        self.fcbox.current(0)
        self.fcbox.grid(row=2, column=1, padx=3, pady=4, sticky=W)

        self.scbtn = Button(self, text='Scale', command=self.scale)
        self.scbtn.grid(row=1, column=0, padx=3, pady=4, sticky=W)
        self.scbtn.config(state='disabled')

        self.fbtn = Button(self, text='Filter', command=self.use_filter)
        self.fbtn.grid(row=2, column=0, padx=3, pady=4, sticky=W)
        self.fbtn.config(state='disabled')

        self.canvas = Canvas(self, width=max_w, height=max_h)
        self.canvas.grid(row=3, column=0, padx=3, pady=4, sticky=E+W+S+N, columnspan=3)

        self.bbtn = Button(self, text='Reverse', command=self.restore_image)
        self.bbtn.grid(row=2, column=2, padx=3, pady=4, sticky=W + N)
        self.bbtn.config(state='disabled')


def main():
    gui = Tk()
    gui.geometry("1000x700")
    Window(gui)
    gui.mainloop()


if __name__ == '__main__':
    main()