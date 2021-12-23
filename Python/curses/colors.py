#!/usr/bin/env python3 
'''Test your terminal'''

import curses
import time


def main(screen):
    def put(text, offset=0):
        screen.clear()
        screen.addstr(1 + offset, 4, text)
        screen.getch()


    curses.curs_set(0)
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
    screen.addch('█', curses.A_BLINK)
    screen.move(0, 0)
    screen.getch()

    for i in range(len(example)):
        l = example[i]
        n = example[i + 1]
        if l == '\n' and n != '\n':
            screen.getch()
        if l != ' ':
            time.sleep(1 / 10)
        screen.addch(l)
        screen.insstr('█', curses.A_BLINK)
        screen.refresh()

    screen.getch()


if __name__ == '__main__':
    curses.wrapper(main)
