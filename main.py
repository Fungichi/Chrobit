import curses
from curses import wrapper
from datetime import datetime
import time 


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
def setup(stdscr):
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

def main(stdscr):
    curses.start_color()
    curses.init_pair(1,curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(2,curses.COLOR_YELLOW, curses.COLOR_MAGENTA)

    stdscr.clear()
    stdscr.refresh()

    setup(stdscr)

 
            

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

        time.sleep(10)

        
        
    
    
wrapper(main)
