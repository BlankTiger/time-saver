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
        quit_button = Button(self, text="Quit", command=self.client_exit)
        compress_button = Button(self, text="Compress", command=lambda: self.compressImages(path_box.get()))
        pack_to_pdf_button = Button(self, text="Pack into PDF", command=lambda: self.compressToPDF(path_box.get(), file_name_box.get()))
        pack_to_zip_button = Button(self, text="Pack into ZIP", command=lambda: self.packIntoZIP(path_box.get(), file_name_box.get()))
        file_name_label = Label(self, text="Enter file name")
        file_name = StringVar(self)
        file_name.set("lista")
        file_name_box = Entry(self, width=15, justify=CENTER, textvariable = file_name)
        
        path_label = Label(self, text="Enter the path to files")
        path = StringVar(self)
        path.set(os.getcwd())
        path_box = Entry(self, width=30, justify=CENTER, textvariable = path)
        
        self.master.update()
        file_name_label.place(relx=0.3, rely=0.2, anchor=CENTER)
        file_name_box.place(relx=0.3, rely=0.3, anchor=CENTER)
        path_label.place(relx=0.7, rely=0.2, anchor=CENTER)
        path_box.place(relx=0.7, rely=0.3, anchor=CENTER)
        compress_button.place(relx=0.2, rely=0.5, anchor=CENTER)
        pack_to_pdf_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        pack_to_zip_button.place(relx=0.8, rely=0.5, anchor=CENTER)
        quit_button.place(relx=0.5, rely=0.9, anchor=CENTER)
        

    def compressImages(self, path=os.getcwd()):
        os.system(f'timero.py --path \"{path}\"')

    def compressToPDF(self, path=os.getcwd(), file_name="lista"):
        os.system(f'timero.py --pdf --path \"{path}\" --name {file_name}')
    
    def packIntoZIP(self, path=os.getcwd(), file_name="lista"):
        os.system(f'timero.py --zip --path \"{path}\" --name {file_name}')

    def client_exit(self):
        exit()

root = Tk()
root.geometry("400x200")
app = Window(root)
root.mainloop()