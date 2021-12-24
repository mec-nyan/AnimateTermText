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
    status_fg = 244
    status_bg = 0
    logo_fg = 226
    logo_bg = 0
    mode_fg = 0
    mode_bg = 204
    inter_fg = 204
    inter_bg = 238
    git_fg = 250
    git_bg = 238
    outer_fg = 238
    outer_bg = -1

    curses.init_pair(4, inter_fg, inter_bg)
    inter = curses.color_pair(4)
    curses.init_pair(5, outer_fg, outer_bg)
    outer = curses.color_pair(5)
    curses.init_pair(6, mode_fg, mode_bg)
    mode = curses.color_pair(6)
    curses.init_pair(7, git_fg, git_bg)
    git = curses.color_pair(7)
    curses.init_pair(8, logo_fg, logo_bg)
    js = curses.color_pair(8)

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
    
    pos = ypos, xpos = editor.getyx()

    # statusline
    statusline = curses.newwin(2, columns, lines - 2, 0)
    curses.init_pair(3, status_fg, status_bg)
    status_color = curses.color_pair(3)
    statusline.bkgdset(status_color)
    statusline.clrtoeol()
    mode_text = '  NORMAL  '
    git_text = '  master '
    left_sep = ''
    right_sep = ''
    statusline.addstr(mode_text, mode) 
    statusline.addstr(left_sep, inter)
    statusline.addstr(git_text, git)
    statusline.addstr(left_sep, outer)
    statusline.addstr(' helloWorld.js ')
    statusline.addstr('  ', js)
    statusline.addstr(right_sep, outer)
    statusline.addstr(' :{:2d} :{:3d} '.format(ypos, xpos), git)
    statusline.addstr(right_sep, inter)
    statusline.addstr(' I  gnu+linux ', mode | curses.A_ITALIC)
    statusline.refresh()

    screen.getch()


if __name__ == '__main__':
    curses.wrapper(main)
