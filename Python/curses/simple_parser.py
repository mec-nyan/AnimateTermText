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

    colours.append(curses.color_pair(0))

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
    keywords = ['for', 'if', 'let', 'var', 'const', 'else', 'while']
    tokens = []

    is_comment = False
    is_ml_comment = False
    is_string = False 
    is_number = False
    is_word = False
    string_type = ''

    stream = list(code)
    char, previous, _next = None, None, None

    while stream:
        char = stream.pop(0)
        if stream:
            _next = stream[0]
        else:
            _next = None

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
            if char == '/' and previous == '*':
                is_ml_comment = False
        elif char == '/' and not is_string and not is_comment and not is_ml_comment:
            if _next == char:
                is_comment = True
                tokens.append(Token('comment', char))
            elif _next == '*':
                is_ml_comment = True
                tokens.append(Token('mlc', char))
        elif is_number:
            if char.isdigit() or char in ',.':
                tokens[-1].put_char(char)
            else:
                is_number = False
                stream.insert(0, char)
                continue
        elif is_word:
            if char.isidentifier():
                tokens[-1].put_char(char)
            else:
                is_word = False
                stream.insert(0, char)
                continue
        elif char.isdigit() and not previous.isidentifier():
            is_number = True
            tokens.append(Token('num', char))
        elif char in brackets:
            tokens.append(Token('bracket', char))
        elif char in operators:
            tokens.append(Token('op', char))
        elif char.isidentifier():
            is_word = True
            tokens.append(Token('word', char))
        else:
            tokens.append(Token('generic', char))

        previous = char

    # Show time!
    editor.clear()
    previous, _next = None, None
    while tokens:
        t = tokens.pop(0)
        if tokens:
            _next = tokens[0]
        else:
            _next = None

        if t.name == 'bracket':
            editor.bkgdset(colours[7])
        elif t.name == 'op':
            editor.bkgdset(colours[5])
        elif t.name == 'num':
            editor.bkgdset(colours[11])
        elif t.name == 'string':
            editor.bkgdset(colours[2])
        elif t.name == 'comment':
            editor.bkgdset(colours[0])
        elif t.name == 'mlc':
            editor.bkgdset(colours[14])
        elif t.name == 'word':
            if ''.join(t.chars) in keywords:
                editor.bkgdset(colours[5])
            elif previous and previous.chars[0] == '.' and _next and _next.chars[0] == '(':
                editor.bkgdset(colours[12])
            else:
                editor.bkgdset(colours[-1])
        elif t.name == 'generic' or t.name == 'wsp':
            editor.bkgdset(colours[-1])

        for c in t.chars:
            editor.addstr(c)

        previous = t

    editor.getch()
    



if __name__ == '__main__':
    curses.wrapper(main)
