#!/usr/bin/python
"""
This module removes lines from text copied to clipboard suitable for pasting formatted text into a spreadsheet

install pyperclip from pip with:
pip install pyperclip
"""

import pyperclip as clip
from_clip = clip.paste() # read in text from clipboard
to_copy = from_clip.replace("\n", " ")
to_clip = to_copy.capitalize()
clip.copy(to_clip) # write to clipboard
