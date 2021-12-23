#!/usr/bin/env python3
'''Refreshing python curses'''

import curses
import time


def main(stdscr):
    def put(msg):
        stdscr.clear()
        stdscr.addstr(2, 4, msg)
        stdscr.getch()


    curses.curs_set(0)
    put("Testing terminal")
    put("Can change colors? {}".format(curses.can_change_color()))
    put("Number of colors: {}".format(curses.COLORS))

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    red_bg = curses.color_pair(1)
    stdscr.bkgdset(red_bg)
    put("red bg")
    curses.init_color(1, 1000, 0, 0)
    put("really red")

    
    red, green, blue = 255, 0, 0
    while True:
        curses.init_color(1, int((1000 / 255) * red), int((1000 / 255) * green), int((1000 / 255) * blue))
        stdscr.refresh()
        time.sleep(1 / 30)
        if red > 0 and green < 255 and blue == 0:
            red -= 1 
            green += 1
        elif  green > 0 and blue < 255 and red == 0:
            green -= 1 
            blue += 1 
        elif blue > 0 and red < 255 and green == 0:
            blue -= 1 
            red += 1 



if __name__ == "__main__":
    curses.wrapper(main)
