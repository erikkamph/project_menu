#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses

from icecream import ic

from example import multi_selection, normal_menu, scroll_test, single_selection

menus = {1: normal_menu, 2: single_selection, 3: multi_selection, 4: scroll_test}

if __name__ == "__main__":
    print("1. Menu with submenus")
    print("2. Single selection menu")
    print("3. Multiple choice Menu")
    print("4. Scrolling single selection menu test")
    a = input("Which example do you want to run?")
    b = curses.wrapper(menus[int(a)])
    ic(b)
