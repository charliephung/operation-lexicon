# Your own card pictures ("Custom" mode)

Put your images in this folder, then choose **Custom** under Controls in the game.

Two ways to name them:

1. **Numbered (no extra step):** `1.jpg`, `2.jpg`, `3.png` … The game finds them by itself.
   Supported: .jpg .jpeg .png .webp
2. **Any names:** run `python3 tools/list_custom.py` from the project folder after adding or
   removing files. It writes `list.js`, and the game uses that list instead.

You need at least 25 pictures. Cards are dealt without repeats until every picture has been used.
The card label (shown on hover and in "Revealed cards") comes from the file name.

Only use pictures you have the right to use.
