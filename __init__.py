"""
This menu module is used to create
a menu using curses in a terminal.
The menu itself has three different
modes and these are:
    1. Menu with submenus
    2. Single selection menu
    3. Multiple choice menu
Each has it's own customization
and visualization when it presents
the menu for the end user.

The following structure is
the structure of the project:
Project root (/)
├── __init__.py (To make it an importable module)
├── example.py (Example menus for those interested)
├── data.py (The different menu items for the menu)
├── main.py (Used to start a demo using examples)
└── menu.py (Contains the menu class itself)

The customizations available uses a set of colors.
Following colorpairs is used when presenting the
menu items to the end user along with when it is
used:
1. Active but not selected
    FG: White
    BG: Black
2. Not active and not selected
    FG: Black
    BG: Transparent
3. Selected but not active
    FG: Green
    BG: Transparent
4. Selected and active
    FG: Green
    BG: Blackk
"""

from menu.data import ItemMultiSelection, ItemSingleSelection, MenuItem
from menu.example import multi_selection, single_selection, normal_menu
from menu.menu import ApplicationMenu
