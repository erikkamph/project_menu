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
menu.py and data.py contains the necceessary information
to create your own menus. You can choose from the same
menu types as in the [examples](#examples), or define
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
