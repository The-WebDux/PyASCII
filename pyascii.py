#!/usr/bin/python3
# Coded by - WebDux -
import pyfiglet
import argparse
fonts = ["banner", "big", "block", "bubble", "circle", "digital", "emboss", "emboss2", "future", "ivrit", "lean", "letter", "mini", "mnemonic", "pagga", "script", "shadow", "slant", "small", "smblock", "smbraille", "smscript", "smshadow", "smslant", "standard"]


parser = argparse.ArgumentParser(description='text to ASCII art')
parser.add_argument('-t','--text', type=str, nargs='+', action='append')
args = parser.parse_args()


try:
	for textargs in args.text:
		for textarg in textargs:
			for font in fonts:
		 		print(pyfiglet.figlet_format(textarg, font=font))
				print("FONT:", font,"\n_____________\n")
except TypeError:
	print("[ERROR] Give me argument: -t youe_text")
