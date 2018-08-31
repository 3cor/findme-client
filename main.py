"""
Forked from ePaperLibrary for Waveshare e-Paper 2.7" Raspberry HAT
Github: https://github.com/lyoko17220/ePaperLibrary

Developed by: Nitis Monburinon (2018)
"""

import epaper

def main():
    ep = epaper.EPScreen('landscape')
    #ep.show("images/arigatou.bmp")
    #ep.show("images/iot_boys.bmp")
    ep.print("E Ink (electronic ink) is a popular type of electronic paper display technology",font="big")
    ep.print(",characterized by high visibility and contrast.",pos=(0,90),font="normal")
    ep.update_screen()

main()
