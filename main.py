"""
Forked from ePaperLibrary for Waveshare e-Paper 2.7" Raspberry HAT
Github: https://github.com/lyoko17220/ePaperLibrary

Developed by: Nitis Monburinon (2018)
"""

import epaper
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("title", help="Title to show on the E-paper display.")
parser.add_argument("text", help="Text to show on the E-paper display.")
args = parser.parse_args()
title = args.title
text = args.text

def main():
    print("Printing: %s" % text)
    ep = epaper.EPScreen('landscape')
    ep.print(text)
    ep.set_title(title)
    ep.update_screen()

main()
