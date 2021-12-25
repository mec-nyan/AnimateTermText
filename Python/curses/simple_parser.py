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
    class Token:
        def __init__(self, name, char):
            self.name = name
            self.chars = [char]

        def put_char(self, char):
            self.chars.append(char)


    brackets = '()[]{}'
    operators = '+-*/%<>=!'
    numbers = '0123456789'
    tokens = []

    for i in range(len(code)):
        char = code[i]
        if char in brackets:
            tokens.append(Token('bracket', char))
        elif char in operators:
            tokens.append(Token('op', char))
        elif char in numbers:
            tokens.append(Token('num', char))
        else:
            tokens.append(Token('generic', char))

    # Show time!
    editor.clear()
    for t in tokens:
        if t.name == 'bracket':
            editor.bkgdset(colours[1])
        elif t.name == 'op':
            editor.bkgdset(colours[2])
        elif t.name == 'num':
            editor.bkgdset(colours[3])
        elif t.name == 'generic':
            editor.bkgdset(curses.color_pair(0))

        for c in t.chars:
            editor.addstr(c)

    editor.getch()
    



if __name__ == '__main__':
    curses.wrapper(main)
