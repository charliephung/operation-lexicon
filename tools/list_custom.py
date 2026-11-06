#!/usr/bin/env python3
"""List every image in assets/custom/ so the game's "Custom" mode can use any filenames.
Usage: python3 tools/list_custom.py"""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, 'assets', 'custom')
EXT = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.svg', '.avif')
files = sorted((f for f in os.listdir(DIR) if f.lower().endswith(EXT)),
               key=lambda f: (len(f), f.lower()))
with open(os.path.join(DIR, 'list.js'), 'w') as out:
    out.write('// Made by tools/list_custom.py. Re-run it after adding or removing pictures.\n')
    out.write('var CUSTOM_PICS = ' + json.dumps(files, indent=0) + ';\n')
print(f'{len(files)} pictures listed in assets/custom/list.js')
