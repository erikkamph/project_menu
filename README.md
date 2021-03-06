# Curses Menu
A simple menu application for command line enthusiasts written in Python
using curses to be able to write on screen. There are three different types
of menus that is available to the end user for the moment, these are:
1. Simple menu
2. Single selection menu
3. Multi selection menu

[![project_menu license information](https://img.shields.io/github/license/erikkamph/project_menu.svg)](/LICENSE.md)
[![Issues](https://img.shields.io/github/issues/erikkamph/project_menu.svg)](https://github.com/erikkamph/project_menu/issues)
[![commits-since](https://img.shields.io/github/commits-since/erikkamph/project_menu/0.1.svg)](https://github.com/erikkamph/project_menu/releases/latest)
![Made with python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)

## Table of contents
1. [TODO](#todo)
2. [Project Structure](#project-structure)
    1. [Examples](#examples)
    2. [Menu and data](#menu-and-data)
    3. [Requirements](#requirements)
3. [Installation](#installation)
    1. [Cloning the project and installing](#cloning-and-installing)
    2. [Using PyPI (Not yet supported)](#using-pypi)
    3. [As a submodule in your own project](#creating-a-submodule-in-project)
    4. [Using setup.py to install (Not yet supported)](#using-setup-file-to-install)
4. [Example Code](#example-code)
5. [Previews](#previews)
    1. [Example 1](#example-1)
    2. [Example 2](#example-2)
    3. [Example 3](#example-3)
    4. [Example 4](#example-4)
    5. [Example 5](#example-5)
    6. [Example 6](#example-6)
6. [License](#license)

### TODO
- [ ] Fix [setup.py](/src/menu_zerobeef/setup.py)
- [ ] Add feature that makes the menu scrollable
    - [ ] Fix a problem where if the user is at the end of the list, select the last item
    - [ ] Fix a problem where if the user goes upwards in the menu that prevents the user from going back down unless at 0
- [ ] Fix bugs that might appear over time

### Project Structure
```
.
├── LICENSE.md
├── README.md
├── images
│   ├── Example1.png
│   ├── Example2.png
│   ├── Example3.png
│   ├── Example4.png
│   ├── Example5.png
│   └── Example6.png
├── pyproject.toml
├── requirements.txt
├── src
│   └── menu_zerobeef
│       ├── Pipfile
│       ├── Pipfile.lock
│       ├── __init__.py
│       ├── data.py
│       ├── example.py
│       ├── main.py
│       ├── menu.py
│       └── setup.py
└── tests
```

#### Examples
The examples are located in example.py. Currently
there are three examples in that file. The exaples
that are available are:
1. Menu with submenu
2. Single selection menu
3. Multiple selection menu
A quicker example can be found under [Example Code](#example-code).

#### Menu and data
[menu.py](/src/menu_zerobeef/menu.py) and [data.py](/src/menu_zerobeef/data.py) contains the necceessary information
to create your own menus. You can choose from the same
menu types as in the [previews](#previews), or define
your own menu item by extending MenuItem class from
[data.py](/src/menu_zerobeef/data.py).

#### Requirements
Following is a shorter version of the requirements
for running the project:
```python
asttokens==2.0.5
colorama==0.4.5
executing==0.8.3
icecream==2.1.2
Pygments==2.12.0
six==1.16.0
```
More requirements can be found in [requirements.txt](/requirements.txt)

### Installation
When installing in your own project, be sure to follow one of following steps:
1. [Cloning the project and installing](#cloning-and-installing)
2. [Using PyPI (Not yet supported)](#using-pypi)
3. [As a submodule in your own project](#creating-a-submodule-in-project)
4. [Using setup.py to install](#using-setup-file-to-install)
5. [Using a release file from the repository](#using-a-release-file)

#### Cloning and installing
1. Change directory to your own project where you are going to use the module
2. `git clone https://github.com/erikkamph/project_menu`
3. Add `/project_menu/` to a `.gitignore` file as it should not be pushed to your own git repository, do this for every `.gitignore`.
4. See [Example Code](#example-code) and see what you need to change and how to use.

#### Using PyPI
[pypi.org/project/menu-zerobeef](https://pypi.org/project/menu-zerobeef/)

#### Creating a submodule in project
1. Enter the same git directory as your own project you want to add this to
2. Execute following `git submodule add https://github.com/erikkamph/project_menu`. This will add the project as a submodule for your project.
3. Check that it has been added by running `git status`
4. See [Example Code](#example-code) and see what you need to change to import it properly
5. Good work! You can now use the classes to create a menu.

##### Important regarding submodules
None of the code will follow for users of your project when using submodules.

Users that clone afterwards will need following steps:
1. `git submodule init`
2. `git submodule update`

The steps for all of this can be found at [Git - Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

#### Using setup file to install
1. Change directory to `src/menu_zerobeef`.
2. Run `python setup.py install` to install.
3. The project should be installed now.
4. See [Example Code](#example-code)

#### Using a release file
1. Go to [releases]()
2. Download the latest file that ends in `.whl`
3. In your project, if it has venv activate it.
4. `pip install <path_to_whl>` where `<path_to_whl>` is the path to the newly downloaded `.whl` file.
5. See [Example Code](#example-Code) for examples
6. You should be good to go.

### Example Code
The following is an example that can be used to
show how to implement the menu. If you the project
using local methods such as `git submodule` or `git clone`,
 you might have to change the first two rows from saying
 `from menu_zerobeef.data` in the beginning to
 `from project_menu.src.menu_zerobeef.data`.
```python
from menu_zerobeef.data import (ItemMultiSelection, ItemSingleSelection,
                                MenuItem)
from menu_zerobeef.menu import ApplicationMenu
import curses


def test(stdscr):
    curses.start_color()
    curses.use_default_colors()
    menu_title = "Muti Selection Test"
    items = [ItemMultiSelection(str(i), i) for i in range(0, 33)]
    test = ApplicationMenu(stdscr, (items, menu_title))
    test.show_menu()


curses.wrapper(test)
```

### Previews
#### Example 1
![Example 1](https://github.com/erikkamph/project_menu/blob/cc9afc3761f3e09ab285ebd130aef7c5ed307781/images/Example1.png)

#### Example 2
![Example 2](https://github.com/erikkamph/project_menu/blob/cc9afc3761f3e09ab285ebd130aef7c5ed307781/images/Example2.png)

#### Example 3
![Example 3](https://github.com/erikkamph/project_menu/blob/cc9afc3761f3e09ab285ebd130aef7c5ed307781/images/Example3.png)

#### Example 4
![Example 4](https://github.com/erikkamph/project_menu/blob/cc9afc3761f3e09ab285ebd130aef7c5ed307781/images/Example4.png)

#### Example 5
![Example 5](https://github.com/erikkamph/project_menu/blob/cc9afc3761f3e09ab285ebd130aef7c5ed307781/images/Example5.png)

#### Example 6
![Example 6](https://github.com/erikkamph/project_menu/blob/cc9afc3761f3e09ab285ebd130aef7c5ed307781/images/Example6.png)

### License
The program was licensed under the MIT license,
for more information see [LICENSE.md](/LICENSE.md)
or visit [choosealicense.com](https://choosealicense.com/licenses/mit/).

