#!/usr/bin/env python3 
'''Test your terminal'''

import curses
import time


def main(screen):
    def put(text, offset=0):
        screen.clear()
        screen.addstr(1 + offset, 4, text)
        screen.getch()


    '''
    put('Testing terminal')
    put('Can you hear a beep?')
    curses.beep()
    put('Can you see me flash?')
    curses.flash()
    put('Can change colors? [{}]'.format(curses.can_change_color()))
    put('Number of colors: [{}]'.format(curses.COLORS))
    put('Test color content')
    '''

    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    green_fg = curses.color_pair(1)
    screen.bkgdset(green_fg)

    example = '''\
This is a typewriter effect.
We'll be using this a lot.

Cool, isn't it?'''

    screen.clear()

    wait = False
    for l in example:
        if l == '\n':
            wait = True
        if l != ' ':
            time.sleep(1 / 20)
        if wait and l != '\n':
            wait = False
            screen.getch()
        screen.echochar(l)

    # Displace characters?
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
    red_bg = curses.color_pair(2)

    screen.clear()
    screen.move(0, 0)
    screen.addch(' ', red_bg | curses.A_BLINK)
    screen.move(0, 0)
    screen.getch()
    screen.insch('a')
    screen.getch()
    screen.move(0, 0)
    screen.insstr('hello world', curses.A_BLINK)
    screen.getch()



if __name__ == '__main__':
    curses.wrapper(main)
