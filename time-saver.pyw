from tkinter import *
import os

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Time saver")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Quit", command=self.client_exit)
        compressButton = Button(self, text="Compress", command=self.compressImages)
        packToPDFButton = Button(self, text="Pack into PDF", command=self.compressToPDF)
        packToZIPButton = Button(self, text="Pack into ZIP", command=self.packIntoZIP)
        self.master.update()
        compressButton.place(relx=0.2, rely=0.5, anchor=CENTER)
        packToPDFButton.place(relx=0.5, rely=0.5, anchor=CENTER)
        packToZIPButton.place(relx=0.8, rely=0.5, anchor=CENTER)
        quitButton.place(relx=0.5, rely=0.9, anchor=CENTER)
        

    def compressImages(self):
        os.system("timero.py")

    def compressToPDF(self):
        os.system("timero.py --pdf")
    
    def packIntoZIP(self):
        os.system("timero.py --zip")

    def client_exit(self):
        exit()

root = Tk()
root.geometry("400x200")
app = Window(root)
root.mainloop()