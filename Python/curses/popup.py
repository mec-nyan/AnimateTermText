#!/usr/bin/env python3 
'''Popup curses windows'''


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

    screen.bkgdset(colors[4])
    title = ' Popup windows '
    screen.box()
    screen.addstr(0, (columns - len(title)) // 2, title)
    screen.noutrefresh()

    topw_h = lines -4
    topw_w = columns - 4
    topw_y = 2 
    topw_x = 2
    topw = curses.newwin(topw_h, topw_w, topw_y, topw_x)
    topw.bkgdset(colors[-1])
    topw.addstr('Trying out several popup ideas in python with curses.')
    topw.addstr(topw_h - 1, 0, 'Press any key...')
    topw.getch()

    # Popup: vertical animation
    topw.move(0, 0)
    topw.clrtoeol()
    topw.addstr(0, 0, 'Animated popup border window')
    topw.noutrefresh()

    popup_width = 30
    popup_height = 20
    popup_y = 4
    popup_x = 4
    popup_title = ' <tip/> '
    padding_left = (popup_width - len(popup_title)) // 2
    fps = 40

    popup = curses.newwin(1, popup_width, popup_y, popup_x)
    popup.bkgdset(colors[2])
    for i in range(popup_height):
        popup.clear()
        popup.box()
        popup.addstr(0, padding_left, ' <tip/> ', curses.A_REVERSE)
        popup.refresh()
        curses.napms(1000 // fps)
        popup.resize(1 + i + 1, popup_width)

    popup.getch()

    while popup_x < 40:
        topw.clear()
        topw.addstr(0, 0, 'Move the popup window')
        topw.addstr(topw_h - 1, 0, 'Press any key...')
        topw.refresh()
        popup.mvwin(popup_y, popup_x)
        popup.refresh()
        popup_x += 1
        curses.napms(1000 // fps)
    popup.getch()

    # Post it-like notes 
    topw.clear()
    topw.addstr('Post-it-like notes')
    topw.addstr(topw_h - 1, 0, 'Press any key...')
    topw.noutrefresh()

    colored_bg = []
    start = 17
    for i in range(16):
        curses.init_pair(start, 234, i)
        colored_bg.append(curses.color_pair(start))
        start += 1

    postit_h = 10 
    postit_w = 30
    postit_y = (topw_h - postit_h) // 2
    postit_x = (topw_w - postit_w) // 2
    postit = curses.newwin(postit_h, postit_w, postit_y, postit_x)
    postit.bkgdset(colored_bg[4])
    postit.clear()
    postit.attron(curses.A_ITALIC)
    note = [
        "I'm a note!",
        "",
        "And this is a list:",
        "  ◽ One thing for sure",
        "  ◽ you should've known",
        "  ◽ is that, in the end",
    ]
    for i in range(len(note)):
        postit.addstr(1 + i, 1, note[i])
    postit.refresh()

    postit.getch()

    topw.clear()
    topw.addstr('Post-it-like notes')
    topw.addstr(topw_h - 1, 0, 'Press any key...')
    topw.noutrefresh()

    # Animate with mask
    topw.move(0, 0)
    topw.clear()
    topw.addstr('Vertical animation')
    topw.addstr(topw_h - 1, 0, 'Press any key...')
    topw.getch()

    mask_h = 0
    mask_w = postit_w
    mask = postit.derwin(mask_h, mask_w, 0, 0)

    fps = 25
    while mask_h < postit_h:
        mask_h += 1
        mask.resize(mask_h, mask_w)
        mask.refresh()
        curses.napms(1000 // fps)

    mask.getch()

    topw.move(0, 0)
    topw.clear()
    topw.addstr('Horizontal animation')
    topw.addstr(topw_h - 1, 0, 'Press any key...')
    topw.getch()

    mask_h = postit_h
    mask_w = 0

    fps = 60
    while mask_w < postit_w:
        mask_w += 1
        mask.resize(mask_h, mask_w)
        mask.refresh()
        curses.napms(1000 // fps)

    mask.getch()
    


if __name__ == '__main__':
    curses.wrapper(main)
