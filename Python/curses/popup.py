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
    topw.clrtobot()
    topw.box()
    topw.getch()

    popup_width = 30
    popup_height = 20
    popup_title = ' <tip/> '
    padding_left = (popup_width - len(popup_title)) // 2
    fps = 40

    popup = curses.newwin(1, popup_width, 4, 4)
    popup.bkgdset(colors[2])
    for i in range(popup_height):
        popup.clear()
        popup.box()
        popup.addstr(0, padding_left, ' <tip/> ', curses.A_REVERSE)
        popup.refresh()
        curses.napms(1000 // fps)
        popup.resize(1 + i + 1, popup_width)

    popup.getch()


if __name__ == '__main__':
    curses.wrapper(main)
