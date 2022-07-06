"""
TODO: Write a docstring
"""
import curses
from icecream import ic
from data import MenuItem, ItemSingleSelection, ItemMultiSelection
from menu import ApplicationMenu


def multi_selection(stdscr):
    """
    TODO: Write a docstring
    """
    curses.start_color()
    curses.use_default_colors()
    items = [
        "system", "os", "windows", "linux", "mac", "apple", "pear", "dog",
        "Cancel", "Done"
    ]
    multi_select_items = [
        ItemMultiSelection(t, p) for p, t in enumerate(items)
    ]
    menu_title = "Multiple choice menu example. Which of these are an os or contains os?"
    menu = ApplicationMenu(stdscr, (multi_select_items, menu_title))
    return menu.show_menu()


def single_selection(stdscr):
    """
    TODO: Write a docstring
    """
    curses.start_color()
    curses.use_default_colors()
    items = [
        "system", "os", "windows", "linux", "mac", "apple", "pear", "dog",
        "Cancel"
    ]
    single_select_items = [
        ItemSingleSelection(t, p) for p, t in enumerate(items)
    ]
    menu_title = "Single selection menu example. Which one is related to apple?"

    menu = ApplicationMenu(stdscr, (single_select_items, menu_title))
    return menu.show_menu()


def normal_menu(stdscr):
    """
    TODO: Write a docstring
    """
    curses.start_color()
    curses.use_default_colors()
    sub_menu = [(print, "SubFirst"), (print, "SubSecond"), (None, "Exit")]
    me = [MenuItem(*t, p, None) for p, t in enumerate(sub_menu)]
    sub_title = "Submenu"
    sub_app_menu = ApplicationMenu(stdscr, (me, sub_title))
    items = [(ic, "First"), (ic, "Second"), (ic, "Third"),
             (sub_app_menu.show_menu, "SubMenu"), (None, "Exit")]
    menu = [MenuItem(*t, k, None) for k, t in enumerate(items)]
    menu_title = "Main menu"
    menu = ApplicationMenu(stdscr, (menu, menu_title))
    return menu.show_menu()
