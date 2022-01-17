#!/usr/bin/env python3 
'''Bubble dialogs with powerline'''


import curses


def main(screen):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    colors = []
    for i in range(16):
        curses.init_pair(i + 1, i, -1)
        colors.append(curses.color_pair(i + 1))
    colors.append(curses.color_pair(0)) # default fg bg

    lines, columns = screen.getmaxyx()

    title = ' Bubble dialogs '
    padding_left = (columns - len(title)) // 2
    win = curses.newwin(lines, columns)
    win.bkgdset(colors[8])
    win.box()
    win.addstr(0, padding_left, title)
    win.getch()


if __name__ == '__main__':
    curses.wrapper(main)
