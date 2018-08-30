"""
Forked from ePaperLibrary for Waveshare e-Paper 2.7" Raspberry HAT
Github: https://github.com/lyoko17220/ePaperLibrary

Developed by: Nitis Monburinon (2018)
"""

import epaper

def main():
    ep = epaper.EPScreen('landscape')
    ep.show("arigatou.bmp")
    ep.update_screen()

main()
