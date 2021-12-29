#!/usr/bin/env python3 
'''Parse and highlight javascript files.'''

import curses


# Ok let's parse our code

def parse(code):
    class Token:
        def __init__(self, name, char, type_='default'):
            self.name = name
            self.type_ = type_
            self.chars = [char]

        def put_char(self, char):
            self.chars.append(char)

        def set_type(self, type_):
            self.type_ = type_

    brackets = '()[]{}'
    operators = '+-*/%<>=!'
    keywords = ['for', 'function', 'if', 'let', 'var', 'const', 'else', 'while']
    booleans = ['true', 'false']
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

    _next = None
    for i in range(len(tokens)):
        t = tokens[i]
        try:
            _next = tokens[i + 1]
        except IndexError:
            _next = None

        if t.name == 'word':
            content = ''.join(t.chars)
            if content in keywords:
                t.set_type('kw')
            elif content in booleans:
                t.set_type('bool')
            elif content == 'return':
                t.set_type('ret')
            elif _next and _next.chars[0] == '(':
                t.set_type('func')

    return tokens


