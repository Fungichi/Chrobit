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
x,y,z = 5,7,0
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
        curses.init_pair(3,curses.COLOR_BLACK, color_map[bgcolor])
        self.win.bkgd(' ', curses.color_pair(3))
    def make_bit(self):
        self.win.clear()
        for i in range(self.y-1):
            for j in range(self.x-2):
                self.win.addstr(i,j," ",curses.color_pair(self.mode))
        self.win.refresh()
    def moder(self,mode):
        self.mode = mode
        self.make_bit()
    def change_bg(self):
        pass

def setup_clock12(stdscr):
    stdscr.clear()
    curses.init_pair(3,curses.COLOR_BLACK, color_map[bgcolor])
    stdscr.bkgd(' ', curses.color_pair(3))
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
    clock_loop12(stdscr)

def clock_loop12(stdscr):
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
def setup_clock24(stdscr):
    stdscr.clear()
    curses.init_pair(3,curses.COLOR_BLACK, color_map[bgcolor])
    stdscr.bkgd(' ', curses.color_pair(3))
    stdscr.refresh()
    global column1
    global column2
    global column3
    global column4
    column1 = []
    column2 = []
    column3 = []
    column4 = []
    for i in range(2,22,5):
        bit = Pixel(5,10,i,20,1)
        bit.make_bit()
        column1.append(bit)
    for i in range(2,22,5):
        bit = Pixel(5,10,i,30,1)
        bit.make_bit()
        column2.append(bit)
    for i in range(2,22,5):
        bit = Pixel(5,10,i,40,1)
        bit.make_bit()
        column3.append(bit)
    for i in range(2,22,5):
        bit = Pixel(5,10,i,50,1)
        bit.make_bit()
        column4.append(bit)
    clock_loop24(stdscr)


def clock_loop24(stdscr):
    try:
        while True:

                        
            def intobit(inti):
                return format(inti,"4b")
            digithour = list(map(intobit,map(int,str(datetime.now().hour))))
            digit1hour = digithour[0]
            digit2hour = digithour[1]
            digitminute = list(map(intobit,map(int,str(datetime.now().minute))))
            digit1minute = digitminute[0]
            digit2minute = digitminute [1]

            for i,bit in enumerate(digit1hour):
                if bit == "1":
                    column1[i].moder(2)
                else:
                    column1[i].moder(1)

            for i,bit in enumerate(digit2hour):
                if bit == "1":
                    column2[i].moder(2)
                else:
                    column2[i].moder(1)

            for i,bit in enumerate(digit1minute):
                if bit == "1":
                    column3[i].moder(2)
                else:
                    column3[i].moder(1)

            for i,bit in enumerate(digit2minute):
                if bit == "1":
                    column4[i].moder(2)
                else:
                    column4[i].moder(1)
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
    curses.init_pair(4,curses.COLOR_WHITE,curses.COLOR_BLACK)
    stdscr.addstr(3,3,f'                   ',curses.color_pair(2) | curses.A_REVERSE)
    stdscr.addstr(5,3,f'                   ',curses.color_pair(1) | curses.A_REVERSE)
    stdscr.addstr(7,3,f'                   ')
    stdscr.addstr(9,3,f'                   ')
    stdscr.addstr(3,3,f'ON COLOR: {oncolor}',curses.color_pair(2) | curses.A_REVERSE)
    stdscr.addstr(5,3,f'OFF COLOR: {offcolor}',curses.color_pair(1) | curses.A_REVERSE)
    stdscr.addstr(7,3,f'BG COLOR: {bgcolor}',curses.color_pair(4))
    stdscr.addstr(9,3,f'HOUR MODE: {hourmode}',curses.color_pair(4))
    if selected == 0:
        stdscr.addstr(3,3,f'ON COLOR: {oncolor}',curses.color_pair(2) )
    elif selected == 1:
        stdscr.addstr(5,3,f'OFF COLOR: {offcolor}',curses.color_pair(1))
    elif selected == 2:
        stdscr.addstr(7,3,f'BG COLOR: {bgcolor}', curses.color_pair(4) | curses.A_REVERSE)
    elif selected == 3:
        stdscr.addstr(9,3,f'HOUR MODE: {hourmode}', curses.color_pair(4) | curses.A_REVERSE)

def settings_loop(stdscr):
    global x,y,z,hourmode,selected,oncolor,offcolor,bgcolor
    stdscr.attron(curses.color_pair(4))  
    stdscr.box()                         
    stdscr.attroff(curses.color_pair(4)) 
    rows, collumns = stdscr.getmaxyx()
    stdscr.addstr(0,collumns // 2 - len("Settings") // 2, "Settings",curses.color_pair(4))
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
        if hourmode == 12:
            setup_clock12(stdscr)
        else:
            setup_clock24(stdscr)
        setup_settings(stdscr)

 
    
            
wrapper(main)
