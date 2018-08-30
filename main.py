"""
Forked from ePaperLibrary for Waveshare e-Paper 2.7" Raspberry HAT
Github: https://github.com/lyoko17220/ePaperLibrary

Developed by: Nitis Monburinon (2018)
"""

import epaper

def hello():
	ep = epaper.EPScreen('landscape')
	#ep.set_title("To Jiw")

	# using the default font, each line can contain only 24 characters
	#ep.add_text((0,25),"Boon is fat.")
	#ep.add_text((0,50),"But Jiw is fatter.")
	ep.print("As I told you many times, you should be in the lab. And were supposed to meet me at nine every morning!")
	ep.update_screen()

hello()
