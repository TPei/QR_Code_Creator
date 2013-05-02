# import url opener
from urllib2 import urlopen 
import urllib2
import tkFileDialog

# imports Tkinter for GUIs
from Tkinter import *
from generator import qr_downloader


class App:
	
    def __init__(self, master):
    	""" 
    	Creates a window with two input fields that ask for a URL and file path
    	and saves a qr code pointing to the url in the given folder with the given name
    	"""
    	
    	# initializes frame and layout
        frame = Frame(master)
        frame.pack()
        
        # add two labels
        Label(frame, text='Erzeugt einen QR Code \nzur Angegebenen Adresse').grid(row=0, column=0)
        Label(frame, text='\nZiel URL fuer QR Code angeben \n(z.B.: http://www.google.de): ').grid(row=1, column=0)
        
        # add an entry field for the url
        self.url_var = StringVar()
        Entry(frame, textvariable=self.url_var).grid(row=2, column=0)
        
        # label and entry field for file path
        Label(frame, text='\nSpeicherort waehlen:').grid(row=3, column=0)
        self.file_name_var = StringVar()
        #Entry(frame, textvariable=self.file_name_var).grid(row=4, column=0)
        #Label(frame, text='.png').grid(row=4, column=1)
        button = Button(frame, text='Speicherort waehlen', command=self.pick_directory)
        button.grid(row=4, columnspan=1)
        
        # submit button
        button = Button(frame, text='QR Code Generieren', command=self.generate)
        button.grid(row=5, columnspan=1)
        
        # field where the success/error message will be displayed
        self.result_var = StringVar()
        Label(frame, textvariable=self.result_var).grid(row=6, column=0)
    
    def pick_directory(self):
    	"""creates a pick directory and give file name dialogue"""
    	myFormats = [
		    #('Windows Bitmap','*.bmp'),
		    ('Portable Network Graphics','*.png'),
		    #('JPEG / JFIF','*.jpg'),
	    	#('CompuServer GIF','*.gif'),
	    	]
    	self.file_name_var.set(tkFileDialog.asksaveasfilename(parent=root,filetypes=myFormats ,title="Bild speichern unter..."))
    
    def generate(self):
    	""" calls qr downloader functions and prints status message """
    	transfer_url = self.url_var.get()
    	transfer_file = self.file_name_var.get()
    	
    	self.result_var.set(qr_downloader(transfer_url, transfer_file))
    

if __name__ == '__main__':
	root = Tk()
	root.wm_title('QR Code Generator')
	app = App(root)
	root.mainloop()