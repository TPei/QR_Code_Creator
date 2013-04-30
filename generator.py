def qr_downloader(url_path, file_path):
	""" Downloads a QR Code targeted at a certain URL and downloads it to a given directory using Google's chart API"""
	try:
		# saves target_url 
		target_url = url_path

		# saves file_name and adds file_ending .png
		file_name = file_path
		if len(file_name) == 0:
			file_name = "untitled_qr"
		file_ending = ".png"
		file = file_name + file_ending

		# qr_codes are downloaded through Google's chart API
		url = 'https://chart.googleapis.com/chart?chs=500x500&cht=qr&chl='+target_url
		
		# read file from given url
		qr_code = urlopen(url).read()
		
		# open file for writing, 
		# will create a new file if one doesn't already exist
		# overwrites the file if it exists (maybe not the best idea???)
		qr_file = open(file, "w")

		# write (save) image to file
		qr_file.write(qr_code)

		# close file after writing
		qr_file.close()
		
		return "Datei erfolgreich gespeichert"
	except urllib2.URLError:
		# url read error
		return "Fehler bei der Kommunikation mit dem Server. \n Bitte ueberpruefen Sie Ihre Internetverbindung \noder probieren Sie es zu einem \nspaeteren Zeitpunkt erneut."
	except IOError:
		# IOError (opening or saving file)
		return "Datei ("+ file +") konnte nicht gespeichert werden oder Pfad existiert nicht."
	except EOFError:
		# EOFError, error concerning raw_input()
		return "Fehler bei der Dateneingabe"
	except BaseException:
		# all other exceptions
		return "Unbekannter Fehler"
	
root = Tk()
root.wm_title('QR Code Generator')
app = App(root)
root.mainloop()