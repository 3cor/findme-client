"""
Forked from ePaperLibrary for Waveshare e-Paper 2.7" Raspberry HAT
Github: https://github.com/lyoko17220/ePaperLibrary

Developed by: Nitis Monburinon (2018)
"""

import epaper
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", help="Text to show on the E-paper display.")
args = parser.parse_args()
text = args.text

def main():
    ep = epaper.EPScreen('landscape')
    ep.print(text,type="big")
    ep.update_screen()

main()
