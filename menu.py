"""
This module is used for creating and showing menus.
"""
import curses

from data import ItemMultiSelection, ItemSingleSelection, MenuItem


class ApplicationMenu():
    """
    TODO: Write a docstring
    """

    def __init__(self, stdscr, args=()):
        """
        Initializes a menu for different usecases.

        This function initializes the settings for
        a menu with different settings. Settings
        such as multiselection, singleselection or
        just a plain menu.

        Parameters
        ----------
        self : class
            A pointer to the class itself to be able
            to access all the neccessary items set
            in this function.
        """
        self.stdscr = stdscr
        self.cursor_position = 0
        self.items = args[0]
        self.menu_title = args[1]
        self.loop = True
        self.init_scr_x = args[2] if len(args) > 2 else 1
        self.init_scr_y = args[3] if len(args) > 3 else 2
        curses.init_pair(1, curses.COLOR_BLACK, -1)

    def show_menu(self):
        """
        TODO: Write a docstring
        """
        data = None
        self.remark_items()
        while self.loop:
            self.stdscr.clear()
            self.stdscr.addstr(self.init_scr_y, self.init_scr_x,
                               self.menu_title,
                               curses.color_pair(1) + curses.A_BOLD)
            for k, menu_item in enumerate(self.items):
                self.stdscr.addstr(self.init_scr_y + 1 + k, self.init_scr_x,
                                   menu_item.title if menu_item.title in ("Cancel", "Done")\
                                   else str(menu_item), menu_item.get_style())
            data = self.actions()
        if data is not None:
            return data

    def actions(self):
        """
        TODO: Write a docstring
        """
        key = self.stdscr.getkey()
        current_item = self.items[self.cursor_position]
        if current_item.title in ("Cancel", "Exit") and key == "\n"\
                or key in ("q", "Q"):
            self.exit_menu()
            return None

        if key in ("KEY_UP", "KEY_DOWN"):
            self.cursor_position = (self.cursor_position + 1) % len(self.items)\
                if key == "KEY_DOWN" else (self.cursor_position - 1) % len(self.items)\
                if key == "KEY_UP" else self.cursor_position
            self.remark_items()

        if isinstance(current_item, MenuItem) and key == "\n"\
                and not isinstance(current_item, ItemSingleSelection)\
                and not isinstance(current_item, ItemMultiSelection):
            current_item.take_action()

        if isinstance(current_item, ItemSingleSelection) and key == "\n"\
                and not isinstance(current_item, ItemMultiSelection):
            self.exit_menu()
            return current_item.title

        if isinstance(current_item, ItemMultiSelection):
            data = None
            if key == "\n" and current_item.title != "Done":
                self.items[self.cursor_position].select()
            elif key == "\n" and current_item.title == "Done":
                data = [i.title for i in self.items if i.is_selected]
                self.exit_menu()
            return data
        return None

    def exit_menu(self):
        """
        TODO: Write a docstring
        """
        self.loop = False

    def remark_items(self):
        """
        TODO: Write a docstring
        """
        for item in self.items:
            item.set_active(self.cursor_position)
