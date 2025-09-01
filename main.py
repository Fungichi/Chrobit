import curses
from curses import wrapper
from datetime import datetime
import time 

global oncolor, offcolor, bgcolor, hourmode,color_map,selected

color_map = {
        "BLACK": curses.COLOR_BLACK,
        "RED": curses.COLOR_RED,
        "GREEN": curses.COLOR_GREEN,
        "YELLOW": curses.COLOR_YELLOW,
        "BLUE": curses.COLOR_BLUE,
        "MAGENTA": curses.COLOR_MAGENTA,
        "CYAN": curses.COLOR_CYAN,
        "WHITE": curses.COLOR_WHITE
    }
x,y,z = 5,7,7
keys = list(color_map.keys())
oncolor = keys[x]
offcolor = keys[y]
bgcolor = keys[z]
hourmode = 12
selected = 0

class Pixel():
    def __init__(self,y,x,s,q,mode):
        self.x = x
        self.y = y
        self.s = s
        self.q = q
        self.mode = mode
        self.win = curses.newwin(y,x,s,q)
    def make_bit(self):
        self.win.clear()
        for i in range(self.y-1):
            for j in range(self.x-2):
                self.win.addstr(i,j," ",curses.color_pair(self.mode))
        self.win.refresh()
    def moder(self,mode):
        self.mode = mode
        self.make_bit()

def setup_clock(stdscr):
    stdscr.clear()
    stdscr.refresh()
    global row1
    global row2
    row1 = []
    row2 = []
    for i in range(20,60,10):
        bit = Pixel(5,10,5,i,2)
        bit.make_bit()
        row1.append(bit)
    for i in range(10,70,10):
        bit = Pixel(5,10,10,i,2)
        bit.make_bit()
        row2.append(bit)
    clock_loop(stdscr)

def clock_loop(stdscr):
    try:           

        while True:
            

                
            binhour = list(format(datetime.now().hour % 12,'04b'))
            binminute = list(format(datetime.now().minute,'06b'))

            for i,bit in enumerate(binhour):
                if int(bit) == 1:
                    row1[i].moder(2)
                else:
                    row1[i].moder(1)
            
            for i,bit in enumerate(binminute):
                if int(bit) == 1:
                    row2[i].moder(2)
                else:
                    row2[i].moder(1)

            time.sleep(1)
            try:
                key = stdscr.getkey()
            except curses.error:
                key = None

            if key != None:
                if key == "s":
                    break

    except KeyboardInterrupt:
        cleanup_windows()
    except Exception as e:
        cleanup_windows()
        raise e

def setup_settings(stdscr):
    cleanup_windows()
    stdscr.clear()
    stdscr.refresh()
    settings_loop(stdscr)
def update_settings(stdscr):
    curses.init_pair(1,curses.COLOR_BLACK, color_map[offcolor])
    curses.init_pair(2,curses.COLOR_BLACK, color_map[oncolor])
    curses.init_pair(3,curses.COLOR_BLACK, color_map[bgcolor])
    stdscr.addstr(3,3,f'                   ',curses.color_pair(2) | curses.A_REVERSE)
    stdscr.addstr(5,3,f'                   ',curses.color_pair(1) | curses.A_REVERSE)
    stdscr.addstr(7,3,f'                   ')
    stdscr.addstr(9,3,f'                   ')
    stdscr.addstr(3,3,f'ON COLOR: {oncolor}',curses.color_pair(2) | curses.A_REVERSE)
    stdscr.addstr(5,3,f'OFF COLOR: {offcolor}',curses.color_pair(1) | curses.A_REVERSE)
    stdscr.addstr(7,3,f'BG COLOR: {bgcolor}',curses.color_pair(3) | curses.A_REVERSE)
    stdscr.addstr(9,3,f'HOUR MODE: {hourmode}')
    if selected == 0:
        stdscr.addstr(3,3,f'ON COLOR: {oncolor}',curses.color_pair(2))
    elif selected == 1:
        stdscr.addstr(5,3,f'OFF COLOR: {offcolor}',curses.color_pair(1))
    elif selected == 2:
        stdscr.addstr(7,3,f'BG COLOR: {bgcolor}', curses.color_pair(3))
    elif selected == 3:
        stdscr.addstr(9,3,f'HOUR MODE: {hourmode}', curses.A_REVERSE)
def settings_loop(stdscr):
    global x,y,z,hourmode,selected,oncolor,offcolor,bgcolor
    stdscr.box()
    rows, collumns = stdscr.getmaxyx()
    stdscr.addstr(0,collumns // 2 - len("Settings") // 2, "Settings")
    update_settings(stdscr)
    while True:
        try:
            key = stdscr.getkey()
        except curses.error:
            key = None
        except KeyboardInterrupt:
            cleanup_windows()
        except Exception as e:
            cleanup_windows()
            raise e

        if key != None:
            if key == "c":
                break
            elif key == "KEY_LEFT" and selected == 0:
                x -= 1
            elif key == "KEY_RIGHT" and selected == 0:
                x += 1
            elif key == "KEY_LEFT" and selected == 1:
                y -= 1
            elif key == "KEY_RIGHT" and selected == 1:
                y += 1
            elif key == "KEY_LEFT" and selected == 2:
                z -= 1
            elif key == "KEY_RIGHT" and selected == 2:
                z += 1
            elif (key == "KEY_LEFT" or key == "KEY_RIGHT") and selected == 3:
                if hourmode == 12:
                    hourmode = 24
                else:
                    hourmode = 12
            elif key == "KEY_UP" and selected != 0:
                    selected -= 1
            elif key == "KEY_DOWN" and selected != 3:
                    selected += 1
            oncolor = keys[x % len(keys)]
            offcolor = keys[y % len(keys)]
            bgcolor = keys[z % len(keys)]
            update_settings(stdscr)
           
def cleanup_windows():
    global row1, row2
    if 'row1' in globals():
        for bit in row1:
            if hasattr(bit,'win'):
                bit.win.clear()
                bit.win.refresh()
                del bit.win
        row1.clear()
    if 'row2' in globals():
        for bit in row2:
            if hasattr(bit, 'win'):
                bit.win.clear()
                bit.win.refresh()
                del bit.win
        row2.clear()


    
def main(stdscr):
    curses.start_color()
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_BLACK, color_map[offcolor])
    curses.init_pair(2,curses.COLOR_BLACK, color_map[oncolor])
    stdscr.nodelay(True)
    stdscr.clear()
    stdscr.refresh()
    while True:
        setup_clock(stdscr)
        setup_settings(stdscr)

 
    
            
wrapper(main)
