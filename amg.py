"""
AMG - Advanced Map Generator

Version: Prototype 0
Build: 00005
"""

from PIL import Image

input = [
    '...5...',
    '......5',
]

h = len(input)
w = len(input[0])

if not all(len(line) == w for line in input):
    raise Exception("All rows aren't equal in size.")

canvas = Image.new('RGBA', ((w+2)*50, (h+2)*50), (0, 0, 0, 0))

for y in range(h):
    for x in range(w):
        if input[y][x] == '5':
            canvas.alpha_composite(Image.open('demo.png'), ((x+1)*50, (y+1)*50))

canvas.save('./test.png', 'PNG')
