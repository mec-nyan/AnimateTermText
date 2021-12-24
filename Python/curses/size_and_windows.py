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
    editor_fg = 250 
    editor_bg = 235
    linum_fg = 237
    linum_bg = 235
    status_fg = 39
    status_bg = 0
    logo_fg = 226
    logo_bg = 0
    mode_fg = 0
    mode_bg = 39
    inter_fg = 39
    inter_bg = 238
    git_fg = 250
    git_bg = 238
    outer_fg = 238
    outer_bg = -1
    right_tr_fg = 221
    right_tr_bg = 39
    right_fg = 0
    right_bg = 221

    string_fg = 105
    kw_fg = 39
    bracket_fg = 213
    op_fg = 78
    semi_fg = 168
    func_fg = 36
    num_fg = 37

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
    curses.init_pair(9, right_tr_fg, right_tr_bg)
    rtr = curses.color_pair(9)
    curses.init_pair(10, right_fg, right_bg)
    right = curses.color_pair(10)
    curses.init_pair(11, string_fg, editor_bg)
    string = curses.color_pair(11)
    curses.init_pair(12, kw_fg, editor_bg)
    kw = curses.color_pair(12)
    curses.init_pair(13, bracket_fg, editor_bg)
    bracket = curses.color_pair(13)
    curses.init_pair(14, op_fg, editor_bg)
    op = curses.color_pair(14)
    curses.init_pair(15, semi_fg, editor_bg)
    semi = curses.color_pair(15)
    curses.init_pair(16, func_fg, editor_bg)
    func = curses.color_pair(16)
    curses.init_pair(17, num_fg, editor_bg)
    num = curses.color_pair(17)

    # Editor windows
    editor = curses.newwin(lines -1, columns - 6, 0, 6)
    curses.init_pair(2, editor_fg, editor_bg)
    editor_color = curses.color_pair(2)
    editor.bkgdset(editor_color)
    editor.clear()
    # sample text
    sample = '''\
`let` x = 0;

`for` (`let` i = 0; i < 10; ++i) {
  `if` (i % 2 === 0) {
    console.log("i is even");
  } `else` {
    console.log("i is odd");
  }
}'''
    editor.move(4, 0)
    is_str = False
    is_kw = False
    is_fun = False
    brackets = '()[]{}'
    ops = '+-*/%=!<>|&'
    nums = '0123456789'
    for c in sample:
        if c in brackets and not is_str:
            editor.addstr(c, bracket)
            is_fun = False
            continue
        elif c in ops and not is_str:
            editor.addstr(c, op)
            continue
        elif c == ';':
            editor.addstr(c, semi)
            continue
        elif c in nums:
            editor.addstr(c, num)
            continue
        elif c == '`':
            is_kw = not is_kw
            continue
        elif c == '"':
            is_str = not is_str
            if not is_str:
                editor.addstr(c)
                continue
        elif c == '.':
            is_fun = True

        if is_kw:
            editor.bkgdset(kw)
        elif is_str:
            editor.bkgdset(string)
        elif is_fun:
            editor.bkgdset(func)
        else:
            editor.bkgdset(editor_color)
        editor.addstr(c)
    editor.refresh()

    # line numbers
    curses.init_pair(1, linum_fg, linum_bg)
    linum_color = curses.color_pair(1)

    linum = curses.newwin(lines - 1, 6)
    linum.bkgdset(linum_color)
    linum.clear()
    for i in range(lines - 2):
        linum.addstr('{:4} ▏'.format(i))
    linum.refresh()
    
    pos = ypos, xpos = editor.getyx()

    # statusline
    statusline = curses.newwin(2, columns, lines - 2, 0)
    curses.init_pair(3, status_fg, status_bg)
    status_color = curses.color_pair(3)
    statusline.bkgdset(editor_color)
    statusline.clear()
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
    statusline.addstr(mode_text, mode) 
    statusline.addstr(left_sep, inter)
    statusline.addstr(git_text, git)
    statusline.addstr(left_sep, outer)
    statusline.addstr(file_name, status_color)
    for i in range(filler):
        statusline.addstr(' ', status_color)
    statusline.addstr(file_icon, js)
    statusline.addstr(right_sep, outer)
    statusline.addstr(right_msg, git)
    statusline.addstr(right_sep, inter)
    statusline.addstr(linecol, mode)
    statusline.addstr(right_sep, rtr)
    statusline.addstr(rightmost, right)
    statusline.refresh()

    screen.getch()


if __name__ == '__main__':
    curses.wrapper(main)
