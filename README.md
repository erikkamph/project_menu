## Table of contents
1. [Project Structure](#project-structure)
    1. [Examples](#examples)
    2. [Menu and data](#menu-and-data)
    3. [Requirements](#requirements)
2. [Installation](#installation)
3. [Previews](#previews)
    1. [Example 1](#example-1)
    2. [Example 2](#example-2)
    3. [Example 3](#example-3)
    4. [Example 4](#example-4)
    5. [Example 5](#example-5)
    6. [Example 6](#example-6)
4. [License](#license)

### Project Structure
```
.
├── README.md
├── __init__.py
├── data.py
├── example.py
├── main.py
├── menu.py
└── requirements.txt
```

#### Examples
The examples are located in example.py. Currently
there are three examples in that file. The exaples
that are available are:
1. Menu with submenu
2. Single selection menu
3. Multiple selection menu

#### Menu and data
[menu.py](/menu.py) and [data.py](/data.py) contains the necceessary information
to create your own menus. You can choose from the same
menu types as in the [previews](#previews), or define
your own menu item by extending MenuItem class from
[data.py](/data.py).

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
4. [Using setup.py to install (Not yet supported)](#using-setup-file-to-install)

#### Cloning and installing
1. Change directory to your own project where you are going to use the module
2. `git clone https://github.com/erikkamph/menu`
3. Add following lines to the file(s) where you are going to use the menu:
```python
from data import MenuItem, ItemSingleSelection, ItemMultiSelection
from menu import ApplicationMenu
```
4. See [example.py](/example.py) for examples on how to setup the menu
5. Add `/menu/` to a `.gitignore` file as it should not be pushed to your own git repository, do this for every `.gitignore`.

#### Using PyPI
This method is not yet supported.

#### Creating a submodule in project
1. Enter the same git directory as your own project you want to add this to
2. Execute following `git submodule add https://github.com/erikkamph/menu`. This will add the project as a submodule for your project.
3. Check that it has been added by running `git status`

##### Disclaimer
None of the code will follow for users of your project when using submodules.
Users that clone afterwards will need following steps:
1. `git submodule init`
2. `git submodule update`
The steps for all of this can be found at [Git - Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

#### Using setup file to install
This method is not yet supported even though there is a [setup.py](/setup.py) file in the project.
The reason for this is that there are some information missing in the [setup.py](/setup.py) file.

### Previews
#### Example 1
![Example 1](/images/Example1.png)

#### Example 2
![Example 2](/images/Example2.png)

#### Example 3
![Example 3](/images/Example3.png)

#### Example 4
![Example 4](/images/Example4.png)

#### Example 5
![Example 5](/images/Example5.png)

#### Example 6
![Example 6](/images/Example6.png)

### License
The program was licensed under the MIT license,
for more information see [LICENSE.md](/LICENSE.md)
or visit [choosealicense.com](https://choosealicense.com/licenses/mit/).
