from GlyphsApp import *

open_font = Glyphs.font

font_name = open_font.familyName
print("Font Name: " + open_font.familyName)

font_version = "%i.%03i" % (open_font.versionMajor, open_font.versionMinor)
print("Font Version: " + font_version)