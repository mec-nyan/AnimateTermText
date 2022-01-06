#!/usr/bin/env python3 
'''Get terminal size (columns and lines) and split in rects (windows)'''

import curses
from js_parser import parse


def main(screen):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    lines, columns = screen.getmaxyx()
    
    # This depend on the terminal (currently using dracula theme)
    black = 0
    red = 1 
    green = 2 
    yellow = 3
    purple = 4  # terminal default: blue
    pink = 5    # "         "     : maganta
    light_blue = 6
    white_ish = 7
    blue = 8
    alt_red = 9
    alt_green = 10
    alt_yellow = 11
    alt_purple = 12
    alt_pink = 13
    alt_light_blue = 14
    white = 15

    colors = []
    for i in range(16):
        curses.init_pair(i + 1, i, -1)
        colors.append(curses.color_pair(i + 1))

    # Editor windows
    editor = curses.newwin(lines -2, columns - 6, 0, 6)

    # line numbers
    linum = curses.newwin(lines - 1, 6)
    linum.bkgdset(colors[8])
    linum.clear()
    for i in range(lines - 2):
        linum.addstr('{:4} ▏'.format(i))
    linum.refresh()
    
    ypos, xpos = 0, 0 # use getyx()

    # statusline
    statusline = curses.newwin(2, columns, lines - 2, 0)
    mode_text = '  INSERT  '
    git_text = '  master '
    left_sep = ''
    right_sep = ''
    file_name = ' helloWorld.js '
    file_icon = '  '
    right_msg = ' utf-8 '
    rightmost = ' {late}[nite](devs) '
    linecol = '  {:2d}  {:3d} '.format(ypos, xpos)
    filler = columns - (len(mode_text) + len(git_text) + len(file_name) + len(file_icon) + len(right_msg) + len(linecol) + len(rightmost) + 5)
    curses.init_pair(20, black, light_blue)
    mode = curses.color_pair(20)
    statusline.addstr(mode_text, mode) 
    curses.init_pair(21, light_blue, blue)
    inter = curses.color_pair(21)
    statusline.addstr(left_sep, inter)
    curses.init_pair(22, white, blue)
    git = curses.color_pair(22)
    statusline.addstr(git_text, git)
    curses.init_pair(23, blue, -1)
    outer = curses.color_pair(23)
    statusline.addstr(left_sep, outer)
    statusline.addstr(file_name)
    for i in range(filler):
        statusline.addstr(' ')
    curses.init_pair(24, yellow, -1)
    js = curses.color_pair(24)
    statusline.addstr(file_icon, js)
    statusline.addstr(right_sep, outer)
    statusline.addstr(right_msg, git)
    statusline.addstr(right_sep, inter)
    statusline.addstr(linecol, mode)
    curses.init_pair(25, yellow, light_blue)
    rtr = curses.color_pair(25)
    statusline.addstr(right_sep, rtr)
    curses.init_pair(26, black, yellow)
    right = curses.color_pair(26)
    statusline.addstr(rightmost, right)
    statusline.refresh()


    with open('helloWorld.js') as f:
        code = f.read()

    tokens = parse(code)

    while tokens:
        t = tokens.pop(0)

        if t.name == 'bracket':
            editor.bkgdset(colors[7])
        elif t.name == 'op':
            editor.bkgdset(colors[5])
        elif t.name == 'num':
            editor.bkgdset(colors[11])
        elif t.name == 'string':
            editor.bkgdset(colors[3])
        elif t.name == 'comment':
            if t.type_ == 'pause':
                editor.getch()
                continue
            editor.bkgdset(colors[0])
        elif t.name == 'mlc':
            editor.bkgdset(colors[14])
        elif t.name == 'word':
            if t.type_ == 'kw':
                editor.bkgdset(colors[5])
            elif t.type_ == 'bool':
                editor.bkgdset(colors[6])
            elif t.type_ == 'ret':
                editor.bkgdset(colors[1])
            elif t.type_ == 'func':
                editor.bkgdset(colors[2])
            else:
                editor.bkgdset(colors[-1])
        elif t.name == 'generic' or t.name == 'wsp':
            editor.bkgdset(colors[-1])

        fps = 20
        for c in t.chars:
            editor.addstr(c)
            editor.refresh()
            curses.napms(1000 // fps)

    editor.getch()




if __name__ == '__main__':
    curses.wrapper(main)
