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

    is_comment = False
    is_ml_comment = False
    is_string = False 
    string_type = ''


    for i in range(len(code)):
        char = code[i]
        if is_string:
            tokens[-1].put_char(char)
            if char == string_type:
                string_type = ''
                is_string = False
        elif char in ['"', "'"] and not is_comment:
            string_type = char
            is_string = True
            tokens.append(Token('string', char))
        elif is_comment:
            if char == '\n':
                is_comment = False
                tokens.append(Token('wsp', char))
            else:
                tokens[-1].put_char(char)
        elif is_ml_comment:
            tokens[-1].put_char(char)
            if char == '/' and code[i-1] == '*':
                is_ml_comment = False
        elif char == '/' and not is_string and not is_comment and not is_ml_comment:
            if code[i+1] == char:
                is_comment = True
                tokens.append(Token('comment', char))
            elif code[i+1] == '*':
                is_ml_comment = True
                tokens.append(Token('mlc', char))
        elif char in brackets:
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
        elif t.name == 'string':
            editor.bkgdset(colours[4])
        elif t.name == 'comment':
            editor.bkgdset(colours[5])
        elif t.name == 'mlc':
            editor.bkgdset(colours[6])
        elif t.name == 'generic' or t.name == 'wsp':
            editor.bkgdset(curses.color_pair(0))

        for c in t.chars:
            editor.addstr(c)

    editor.getch()
    



if __name__ == '__main__':
    curses.wrapper(main)
