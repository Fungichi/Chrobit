<h1 align="center">Chrobit</h1>
<h3 align="center">Binary clock in the terminal</h3>
<p align="center">
  <img src="https://github.com/Fungichi/Chrobit/blob/main/img/clock12.png" />
</p>


---

## Features

- Binary clock display in terminal
- 12-hour or 24-hour modes
- Customizable colors for ON, OFF, and background
- Real-time updates
- Interactive settings menu

---

## Prerequisites

Before installing, make sure you have:

- Python 3.6 or higher
- Terminal that supports `curses` (Linux, macOS, Windows with WSL or compatible terminal)

Install the Python `curses` module:

Linux / macOS (macOs and linux should have curses already installed)
```bash
sudo apt install python3-curses
```
macOS (Homebrew)
```bash
brew install ncurses
```
Windows
```bash
pip install windows-curses
```

##Installation
Clone the repository using `git`
```bash
git clone https://github.com/Fungichi/Chrobit.git
cd Chrobit
```

## How to use
Run the clock using Python:
```bash
python main.py
```

This program has 2 windows:
- the clock window
- the settings window

To switch from the clock window to the settings window press: 's'

To switch from the settings window to the clock window press: 'c'

## Reading the clock

| 12 hour clock  | 24 hour clock |
| ------------- | ------------- |
| <img src="https://github.com/Fungichi/Chrobit/blob/main/img/clock12%20kopie.png"></img>  | <img src="https://github.com/Fungichi/Chrobit/blob/main/img/clock24.png"></img>  |
| Read horizontally: 0111 = 7 and 110010 = 50| Read vertically: 0010 = 2, 0000 = 0, 0101 = 5 and 0000 = 0  |
| Time: 7:50 | Time: 20:50 |

> [!NOTE]
> The 12 hour clock indicates 7 in the morning but this can also be 7 in the evening, that's how a 12 hour clock works

## Changing the settings
<img src="https://github.com/Fungichi/Chrobit/blob/main/img/settings.png"></img>

The selected setting is highlighted. (HOUR MODE in the picture)

To change this setting you can use the left and right arrow keys.

To switch to another setting you can use the up and down arrow keys.

Settings get automatically saved. To see the changes press 'c'
