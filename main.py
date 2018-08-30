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
	ep.print("Cats are similar in anatomy to the other felids, with a strong flexible body, quick reflexes, sharp retractable claws and teeth adapted to killing small prey. Cat senses fit a crepuscular and predatory ecological niche.",font="big")
	ep.update_screen()

hello()
