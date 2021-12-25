#!/usr/bin/env python3 
'''Parse valid code and apply syntax highlighting to it.'''

import curses


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

    editor.clear()
    for i in range(16):
        editor.addstr(i, 4, f'This is colour number { i }', colours[i])

    editor.getch()

    # Ok let's parse our code
    token, previous, _next = None, None, None
    is_multline_comment = False
    is_comment = False
    is_string = False

    for i in range(len(code)):
        token = code[i]
        if i > 0: previous = code[i - 1]
        if i < len(code) - 1: _next = code[i + 1]




if __name__ == '__main__':
    curses.wrapper(main)
