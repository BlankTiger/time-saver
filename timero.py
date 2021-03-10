import os
import sys
from PIL import Image, ImageOps
from PyPDF4 import PdfFileMerger
from zipfile import ZipFile


def convertToPDF(file_name="lista"):

    pdf_merger = PdfFileMerger()
    for file in os.listdir(os.getcwd()):

        if os.path.splitext(file)[1].lower() == ".pdf":
            pdf_merger.append(file)
    with open(f"{file_name}.pdf", "wb") as fileobj:
        pdf_merger.write(fileobj)
        pdf_merger.close()

    for file in os.listdir(os.getcwd()):

        if os.path.splitext(file)[1].lower() == ".pdf" and file != f"{file_name}.pdf":
            os.remove(f"{os.getcwd()}\\{file}")
    return

def packIntoZIP(file_name="lista"):

    with ZipFile(f"{file_name}.zip", 'w') as zip:
        for file in os.listdir(os.getcwd()):
            if "compressed" in file:
                zip.write(file)
    for file in os.listdir(os.getcwd()):

        if "compressed" in file and os.path.splitext(file)[1].lower() == ".jpg":
            os.remove(f"{os.getcwd()}\\{file}")
    return

def compressImage(picture, quality_value, verbose=False, pack_into_pdf=False):

    picture_path = os.path.join(os.getcwd(), picture)
    compressed = Image.open(picture_path)
    compressed = ImageOps.exif_transpose(compressed)
    if(pack_into_pdf):
        compressed.save(f"compressed_{picture}.pdf", "PDF", optimize=True, quality=quality_value)
    else:
        compressed.save(f"compressed_{picture}", "JPEG", optimize=True, quality=quality_value)

    compressed.close()
    return


def main():

    verbose = False
    pack_into_pdf = False
    pack_into_zip = False
    file_name = "lista"
    cwd = os.getcwd()
    formats = ('.jpg', '.jpeg')
    quality = 30

    if(len(sys.argv) > 1):
        if "-v" in sys.argv:
            verbose = True
        if "--pdf" in sys.argv:
            pack_into_pdf = True
        elif "--zip" in sys.argv:
            pack_into_zip = True
        if "--name" in sys.argv:
            file_name = sys.argv[sys.argv.index("--name")+1]

    for file in os.listdir(cwd):

        if os.path.splitext(file)[1].lower() in formats:
            print(f"compressing {file}")
            compressImage(file, quality, verbose, pack_into_pdf)
    if(pack_into_pdf):
        convertToPDF(file_name)
    elif(pack_into_zip):
        packIntoZIP(file_name)
    print("Done")


if __name__ == "__main__":
    main()
