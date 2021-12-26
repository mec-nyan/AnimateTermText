#!/usr/bin/env python3 
'''Popup curses windows'''


import curses


def main(screen):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    colors = [curses.color_pair(0)]
    for i in range(16):
        curses.init_pair(i + 1, i, -1)
        colors.append(curses.color_pair(i + 1))


    lines, columns = screen.getmaxyx()

    topw = curses.newwin(lines, columns)
    topw.bkgdset(colors[1])
    topw.box()
    topw.getch()

    popup = curses.newwin(20, 20, 4, 4)
    popup.bkgdset(colors[2])
    popup.box()
    popup.getch()


if __name__ == '__main__':
    curses.wrapper(main)
