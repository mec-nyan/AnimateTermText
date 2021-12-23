#!/usr/bin/env python3 
'''Get terminal size (columns and lines) and split in rects (windows)'''

import curses


def main(screen):
    curses.curs_set(0)
    lines, columns = screen.getmaxyx()
    screen.addstr(f'Size:\n\tlines: { lines }\n\tcolumns: { columns }')
    screen.getch()

    curses.start_color()
    curses.use_default_colors()

    # Colors
    editor_fg = curses.COLOR_GREEN
    editor_bg = 235
    linum_fg = 111
    linum_bg = 236
    status_fg = 63
    status_bg = -1
    mode_fg = 0
    mode_bg = 204
    inter_fg = 204
    inter_bg = 237
    outer_fg = 237
    outer_bg = -1

    curses.init_pair(4, inter_fg, inter_bg)
    inter = curses.color_pair(4)
    curses.init_pair(5, outer_fg, outer_bg)
    outer = curses.color_pair(5)
    curses.init_pair(6, mode_fg, mode_bg)
    mode = curses.color_pair(6)

    # Editor windows
    editor = curses.newwin(lines -1, columns - 5, 0, 4)
    curses.init_pair(2, editor_fg, editor_bg)
    editor_color = curses.color_pair(2)
    editor.bkgdset(editor_color)
    editor.clear()
    editor.refresh()

    # line numbers
    curses.init_pair(1, linum_fg, linum_bg)
    linum_color = curses.color_pair(1)

    linum = curses.newwin(lines - 1, 5)
    linum.bkgdset(linum_color)
    linum.clear()
    for i in range(lines - 2):
        linum.addstr('{:4} '.format(i))
    linum.refresh()
    
    # statusline
    statusline = curses.newwin(1, columns, lines - 2, 0)
    curses.init_pair(3, status_fg, status_bg)
    status_color = curses.color_pair(3)
    statusline.bkgdset(status_color)
    statusline.clrtoeol()
    statusline.addstr('  [ mode ]  ', mode) 
    statusline.addstr(' smile ', inter)
    statusline.addstr('', outer)
    statusline.refresh()

    screen.getch()


if __name__ == '__main__':
    curses.wrapper(main)
