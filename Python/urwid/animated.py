#!/usr/bin/env python3
''' A simple python text animation with urwid '''

import urwid


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    color = nc.__next__()
    map1 = urwid.AttrMap(text, color)
    fill = urwid.Filler(map1)

def next_color():
    i = 0
    while True:
        color = 'color{}'.format(i)
        i += 1
        if i > 15: 
            i = 0
        yield color

color = 'color1'
nc = next_color()

palette = [
        ('color0', 'black', 'default'),
        ('color1', 'dark red', 'default'),
        ('color2', 'dark green', 'default'),
        ('color3', 'brown', 'default'),
        ('color4', 'dark blue', 'default'),
        ('color5', 'dark magenta', 'default'),
        ('color6', 'dark cyan', 'default'),
        ('color7', 'light gray', 'default'),
        ('color8', 'dark gray', 'default'),
        ('color9', 'light red', 'default'),
        ('color10', 'light green', 'default'),
        ('color11', 'yellow', 'default'),
        ('color12', 'light blue', 'default'),
        ('color13', 'light magenta', 'default'),
        ('color14', 'light cyan', 'default'),
        ('color15', 'white', 'default'),
        ]


text = urwid.Text('hello curses')
map1 = urwid.AttrMap(text, color)
fill = urwid.Filler(map1)
loop = urwid.MainLoop(fill, palette, unhandled_input=exit_on_q)

loop.run()
