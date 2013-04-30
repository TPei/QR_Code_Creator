# import url opener
from urllib2 import urlopen 
import urllib2

def qr_downloader():
	""" Downloads a QR Code targeted at a certain URL and downloads it to a given directory using Google's chart API"""
	try:
		# intro
		print
		print "Erzeugt einen QR-Code zur angegebenen Adresse."

		# aks for targe_url 
		target_url = raw_input("Ziel URL fuer den QR-Code angeben (z.B.: http://www.google.de): ")

		# ask for filename or even filepath and adds file_ending .png
		print
		print "Bitte Dateiname oder /Unterordner/Dateiname angeben."
		file_name = raw_input("Dateiname: ")
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
		
		print
		print "Datei erfolgreich gespeichert"
	except urllib2.URLError:
		# url read error
		print 
		print "Fehler bei der Kommunikation mit dem Server."
		print "Bitte ueberpruefen Sie Ihre Internetverbindung oder probieren Sie es zu einem spaeteren Zeitpunkt erneut."
	except IOError:
		# IOError (opening or saving file)
		print
		print "Datei ("+ file +") konnte nicht gespeichert werden oder Pfad existiert nicht."
	except EOFError:
		# EOFError, error concerning raw_input()
		print
		print "Fehler bei der Dateneingabe"
	except BaseException:
		# all other exceptions
		print
		print "Unbekannter Fehler"
	
qr_downloader()