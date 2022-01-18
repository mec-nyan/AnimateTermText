#!/usr/bin/env python3 
'''Bubble dialogs with powerline'''


import curses


def main(screen):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    tl_arrow = ''
    tr_arrow = ''
    bl_arrow = ''
    br_arrow = ''
    l_arrow = ''
    r_arrow = ''
    l_empty_arrow = ''
    r_empty_arrow = ''

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

    bubble = curses.newwin(5, 20, 8, 18)
    bubble.bkgdset(colors[4])
    bubble.addstr(2, 0, l_arrow)
    bubble.refresh()
    inner_bubble = curses.newwin(5, 19, 8, 19)
    inner_bubble.bkgdset(colors[4] | curses.A_REVERSE)
    inner_bubble.clrtobot()
    inner_bubble.addstr(1, 1, 'Hey!')
    inner_bubble.addstr(3, 1, "I'm a bubble!")
    inner_bubble.refresh()

    win.getch()



if __name__ == '__main__':
    curses.wrapper(main)
