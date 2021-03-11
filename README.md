# Inspiration
App inspired by the need to save time during tests, and exams. Allows to not waste time on compression and packaging of photos, when there is a need for fast delivery of them. Written completely in python.

# Installation
Two options here, if you're running windows you can just run time-saver.exe anywhere you want and it should work! It's compiled from time-saver.pyw with pyinstaller. If you want to do it yourself, you can just run `pyinstaller --onefile time-saver.pyw`. Second option is to just run `pip install -r requirements.txt`, and open time-saver.pyw afterwards.

# Current features
- compression of jpeg images in the current directory
- packing compressed images into pdf/zip
- ability to easily change file name
- ability to easily change path to the pictures

# Current dependencies
- Pillow
- PyPDF4