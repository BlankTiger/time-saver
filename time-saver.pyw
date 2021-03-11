import os
import sys
import PIL.Image
from PIL import ImageOps
from PyPDF4 import PdfFileMerger
from zipfile import ZipFile
from os.path import basename
from tkinter import *


def convertToPDF(path, file_name="lista"):

    pdf_merger = PdfFileMerger()
    for file in os.listdir(path):

        if os.path.splitext(file)[1].lower() == ".pdf":
            pdf_merger.append(f"{path}\\{file}")
    with open(f"{path}\\{file_name}.pdf", "wb") as fileobj:
        pdf_merger.write(fileobj)
        pdf_merger.close()

    for file in os.listdir(path):

        if os.path.splitext(file)[1].lower() == ".pdf" and file != f"{file_name}.pdf":
            os.remove(f"{path}\\{file}")
    return

def packIntoZIP(path, file_name="lista"):

    with ZipFile(f"{path}\\{file_name}.zip", 'w') as zip:
        for file in os.listdir(path):
            if "compressed" in file:
                zip.write(f"{path}\\{file}", basename(f"{path}\\{file}"))
    for file in os.listdir(path):

        if "compressed" in file and os.path.splitext(file)[1].lower() == ".jpg":
            os.remove(f"{path}\\{file}")
    return

def compressImage(picture, path, quality_value, verbose=False, pack_into_pdf=False):

    picture_path = os.path.join(path, picture)
    compressed = PIL.Image.open(picture_path)
    compressed = ImageOps.exif_transpose(compressed)
    if(pack_into_pdf):
        compressed.save(f"{path}\\compressed_{picture}.pdf", "PDF", optimize=True, quality=quality_value)
    else:
        compressed.save(f"{path}\\compressed_{picture}", "JPEG", optimize=True, quality=quality_value)

    compressed.close()
    return


def timeSaver(file_name="lista", pack_into_pdf=False, pack_into_zip=False, verbose=False, path=os.getcwd(), formats=('.jpg', '.jpeg'), quality=30):


    for file in os.listdir(path):

        if os.path.splitext(file)[1].lower() in formats:
            print(f"compressing {file}")
            compressImage(file, path, quality, verbose, pack_into_pdf)
    if(pack_into_pdf):
        convertToPDF(path, file_name)
    elif(pack_into_zip):
        packIntoZIP(path, file_name)


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Time saver")
        self.pack(fill=BOTH, expand=1)
        quit_button = Button(self, text="Quit", command=self.client_exit)
        compress_button = Button(self, text="Compress", command=lambda: self.compressImages(path_box.get(), int(quality_box.get())))
        pack_to_pdf_button = Button(self, text="Pack into PDF", command=lambda: self.compressToPDF(path_box.get(), file_name_box.get(), int(quality_box.get())))
        pack_to_zip_button = Button(self, text="Pack into ZIP", command=lambda: self.packIntoZIP(path_box.get(), file_name_box.get(), int(quality_box.get())))
        file_name_label = Label(self, text="Enter file name")
        file_name = StringVar(self)
        file_name.set("lista")
        file_name_box = Entry(self, width=15, justify=CENTER, textvariable = file_name)
        
        path_label = Label(self, text="Enter the path to files")
        path = StringVar(self)
        path.set(os.getcwd())
        path_box = Entry(self, width=30, justify=CENTER, textvariable = path)
        
        quality_label = Label(self, text="Enter quality (1-100)")
        quality = StringVar(self)
        quality.set(30)
        quality_box = Entry(self, width=10, justify=CENTER, textvariable = quality)
        
        self.master.update()
        file_name_label.place(relx=0.2, rely=0.2, anchor=CENTER)
        file_name_box.place(relx=0.2, rely=0.3, anchor=CENTER)
        path_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        path_box.place(relx=0.5, rely=0.3, anchor=CENTER)
        quality_label.place(relx=0.8, rely=0.2, anchor=CENTER)
        quality_box.place(relx=0.8, rely=0.3, anchor=CENTER)
        compress_button.place(relx=0.2, rely=0.5, anchor=CENTER)
        pack_to_pdf_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        pack_to_zip_button.place(relx=0.8, rely=0.5, anchor=CENTER)
        quit_button.place(relx=0.5, rely=0.9, anchor=CENTER)
        

    def compressImages(self, path=os.getcwd(), quality=30):
        if quality > 100:
            quality = 100
        elif quality < 1:
            quality = 1
        timeSaver(path=f'{path}', quality=quality)

    def compressToPDF(self, path=os.getcwd(), file_name="lista", quality=30):
        if quality > 100:
            quality = 100
        elif quality < 1:
            quality = 1
        timeSaver(file_name, True, False, path=f'{path}', quality=quality)
    
    def packIntoZIP(self, path=os.getcwd(), file_name="lista", quality=30):
        if quality > 100:
            quality = 100
        elif quality < 1:
            quality = 1
        timeSaver(file_name, False, True, path=f'{path}', quality=quality)

    def client_exit(self):
        sys.exit()

root = Tk()
root.geometry("600x200")
app = Window(root)
root.mainloop()