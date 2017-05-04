#!/usr/bin/python
# This module removes lines from text copied to clipboard
# suitable for pasting formatted text into a spreadsheet

# read in text from clipboard
import pyperclip as clip
from_clip = clip.paste()
to_copy = from_clip.replace("\n", " ")
to_clip = to_copy.capitalize()
clip.copy(to_clip)
# print to_clip
