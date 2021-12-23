#!/usr/bin/env python3
''' A simple curses app in Python3. '''

import curses
import time


def write(win, text, color, delay=0.05):
    win.attron(color)
    for letter in text:
        win.addch(letter)
        win.refresh()
        if letter == '\n':
            time.sleep(delay * 10)
        elif letter == '\t':
            pass
        else:
            time.sleep(delay)
        

def colorize(win, text, colors, delay=0.07):
    color = colors[0]
    sigil = False
    for letter in text:
        if letter == '~':
            sigil = True
            continue
        if sigil:
            sigil = False
            color = colors[int(letter)]
            win.attron(color)
            continue
        win.addch(letter)
        win.refresh()
        if letter == '\n':
            time.sleep(delay * 10)
        elif letter in ('\t', ' '):
            pass
        else:
            time.sleep(delay)


def parse_and_colorize(win, text, colors, delay=0.05):
    operators = ['=', '+=', '-=', '==', '<', '>', '>=', '<=']   # TODO: include all operators
    keywords = ['function', 'if', 'for', 'else', 'return']      # id
    brackets = ['[', ']', '(', ')', '{', '}']
    color = colors[0]   # default color
    lines = text.split('\n')
    for line in lines:
        words = text.split(' ')  # leave tabs untouched
        for word in words:
            if word in operators:
                pass
        
                
    code = '''\
function sumArray(arr) {
\tsum = 0;
\tfor (let i = 0; i < arr.length; ++i) {
\t\tif (Array.isArray(arr[i]) {
\t\t\tsum += sumArray(arr[i]);
\t\t} else {
\t\t\tsum += arr[i];
\t\t}
\treturn sum;
}'''

                

def main(screen):

    curses.curs_set(0)

    # colors
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, 1, -1)
    curses.init_pair(2, 2, -1)
    curses.init_pair(3, 3, -1)
    curses.init_pair(4, 4, -1)
    curses.init_pair(5, 5, -1)
    curses.init_pair(6, 6, -1)
    curses.init_pair(7, 7, -1)
    curses.init_pair(8, 250, -1)
    red = curses.color_pair(1)
    green = curses.color_pair(2)
    yellow = curses.color_pair(3)
    blue = curses.color_pair(4)
    magenta = curses.color_pair(5)
    cyan = curses.color_pair(6)
    white = curses.color_pair(7)
    gray = curses.color_pair(8)

    colors = [white, red, green, yellow, blue, magenta, cyan]

    # tabsize
    curses.set_tabsize(2)

    code = '''\
~4function ~2sumArray~0(arr) ~5{~0
\tsum ~6= ~00;
\t~4for ~0(~4let ~0i = 0; i < arr.~2length~0; ++i) ~5{
\t\t~2if~0 (Array.~2isArray~0(arr[i]) ~5{
\t\t\t~0sum ~3+=~0 sumArray(arr[i]);
\t\t~5} ~2else ~5{
\t\t\t~0sum ~3+=~0 arr[i];
\t\t~5}
\t~1return ~0sum;
~5}'''

    colorize(screen, code, colors)

    screen.getch()



if __name__ == '__main__':
    curses.wrapper(main)
