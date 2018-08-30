"""
Forked from ePaperLibrary for Waveshare e-Paper 2.7" Raspberry HAT
Github: https://github.com/lyoko17220/ePaperLibrary

Developed by: Nitis Monburinon (2018)
"""

import epaper

def main():
    ep = epaper.EPScreen('landscape')
    #ep.show("images/arigatou.bmp")
    ep.show("images/iot_boys.bmp")
    ep.print("IOT BOYS",font="big")
    ep.update_screen()

main()
