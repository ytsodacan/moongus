#!/usr/bin/env python3
"""
Run this once to copy Unity textures into the dashboard folder.
Run from: /Users/sebass/Documents/Among Nobody/Among-Us-Unity-Project/
  python3 Backend/dashboard/copy_assets.py
"""
import shutil, os

BASE = os.path.dirname(os.path.abspath(__file__))
UNITY = os.path.join(BASE, '..', '..', '2019.3.15', 'Assets', 'Texture2D')
DASH  = BASE  # same folder as this script

TEXTURES = [
    'bannerLogo_AmongUs.png',
    'Player.png',
    'Lobby.png',
    'MainMenu.png',
    'logoImage.png',
    'MainScreenCrew.png',
]

for tex in TEXTURES:
    src = os.path.join(UNITY, tex)
    dst = os.path.join(DASH, tex)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f'  ✓  {tex}')
    else:
        print(f'  ✗  {tex}  (not found – skipping)')

print('\nDone! Open Backend/dashboard/index.html in a browser.')
