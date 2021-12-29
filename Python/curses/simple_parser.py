#!/usr/bin/env python3 
'''Parse valid code and apply syntax highlighting to it.'''

import curses
from js_parser import parse


def main(screen):
    # Basic settings
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    # Read the file (this can be passed as an argument in the future)
    with open('./helloWorld.js') as f:
        code = f.read()

    lines, columns = screen.getmaxyx()
    editor = curses.newwin(lines - 2, columns - 2, 1, 1)

    # Show theme colours
    colours = []
    for i in range(16):
        curses.init_pair(i + 1, i, -1)
        colours.append(curses.color_pair(i + 1))

    colours.append(curses.color_pair(0))

    editor.clear()
    for i in range(16):
        editor.addstr(i, 4, f'This is colour number { i }', colours[i])

    editor.getch()

    tokens = parse(code)

    # Show time!
    editor.clear()
    while tokens:
        t = tokens.pop(0)

        if t.name == 'bracket':
            editor.bkgdset(colours[7])
        elif t.name == 'op':
            editor.bkgdset(colours[5])
        elif t.name == 'num':
            editor.bkgdset(colours[11])
        elif t.name == 'string':
            editor.bkgdset(colours[3])
        elif t.name == 'comment':
            editor.bkgdset(colours[0])
        elif t.name == 'mlc':
            editor.bkgdset(colours[14])
        elif t.name == 'word':
            if t.type_ == 'kw':
                editor.bkgdset(colours[5])
            elif t.type_ == 'bool':
                editor.bkgdset(colours[6])
            elif t.type_ == 'ret':
                editor.bkgdset(colours[1])
            elif t.type_ == 'func':
                editor.bkgdset(colours[2])
            else:
                editor.bkgdset(colours[-1])
        elif t.name == 'generic' or t.name == 'wsp':
            editor.bkgdset(colours[-1])

        fps = 20
        for c in t.chars:
            editor.addstr(c)
            editor.refresh()
            curses.napms(1000 // fps)


    editor.getch()
    



if __name__ == '__main__':
    curses.wrapper(main)
