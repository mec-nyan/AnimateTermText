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

    tl_corner = ord('╭')
    tr_corner = ord('╮')
    br_corner = ord('╯')
    bl_corner = ord('╰')


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
    win.border()
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
    win.clrtobot()
    win.border()
    win.addstr(0, padding_left, title)
    win.refresh()

    pane_h = lines - 2
    pane_w = (columns - 4) // 3
    pane_y = 1 
    pane_x = 2
    pane = curses.newwin(pane_h, pane_w, pane_y, pane_x)
    pane.bkgdset(colors[4])
    pane.box()
    pane.getch()

    message_w = pane_w - 16
    message_h = 5
    message_y = pane_y + 2
    message_x = pane_x + 3
    message1 = curses.newwin(message_h, message_w, message_y, message_x)
    message1.bkgdset(colors[4] | curses.A_REVERSE)
    message1.clrtobot()
    message1.addstr(1, 1, 'This is a message.')
    message1.getch()


    bm_h = 5
    bm_w = pane_w - 14
    bm_y = pane_y + message_h + 3
    bm_x = pane_x + 2
    bubble_msg = curses.newwin(bm_h, bm_w, bm_y, bm_x)
    bubble_msg.bkgdset(colors[4])
    bubble_msg.addstr(4, 0, bl_arrow)
    bubble_msg.refresh()
    inner_msg = curses.newwin(bm_h, bm_w - 2, bm_y, bm_x + 1)
    inner_msg.bkgdset(colors[4] | curses.A_REVERSE)
    inner_msg.clrtobot()
    inner_msg.addstr(1, 1, 'this is a bubble message')
    inner_msg.refresh()

    win.getch()

    bm_h = 5
    bm_w = pane_w - 14
    bm_y = 17
    bm_x = 14
    bubble_msg2 = curses.newwin(bm_h, bm_w, bm_y, bm_x)
    bubble_msg2.bkgdset(colors[5])
    bubble_msg2.addstr(4, bm_w-2, br_arrow)
    bubble_msg2.refresh()
    inner_msg2 = curses.newwin(bm_h, bm_w - 2, bm_y, bm_x)
    inner_msg2.bkgdset(colors[5] | curses.A_REVERSE)
    inner_msg2.clrtobot()
    inner_msg2.addstr(1, 1, 'this is a bubble message')
    inner_msg2.refresh()

    win.getch()




if __name__ == '__main__':
    curses.wrapper(main)
