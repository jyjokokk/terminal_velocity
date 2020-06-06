# Terminal Velocity

## Python 3 Fork

The goal of this fork is to bring Terminal Velocity to the Python 3 era,
and possibly implement some additional functionalities I've personally
missed, and fix some of the issues still present in the application
(eg. the 2 empty printed lines when exiting the application, etc.).

**Goals**

1. Refactor the code for Python3
2. Release a version installable by pip3
3. Documentation & unit testing
4. Add note renaming and deletion
5. Fix the printing error
6. Implement option for encryption
11. man-page

For more information, see the [original archived repository](https://github.com/vhp/terminal_velocity),
or read the new README below (wip).

-------

Terminal Velocity is a fast note-taking app for the UNIX terminal, that
focuses on letting you create or find a note as quickly and easily as
possible, then uses your `$EDITOR` to open and edit the note. It is
heavily inspired by the OS X app [Notational
Velocity](http://notational.net/). For screenshots and features, see the
[Terminal Velocity website](https://github.com/vhp/terminal_velocity).

## Installation

### pip - Python package manager

**TODO**

### From Source

Ensure python modules `urwid`, `setuptools`  and `chardet` are installed. Python-dev also.

```
apt install python-setuptools python-chardet python-urwid python-dev
```

Clone the repository from:

    git@github.com:jyjokokk/terminal_velocity.git
    or
    https://github.com/jyjokokk/terminal_velocity

Move into terminal_velocity directory you just cloned and run the following:

    sudo python setup.py install

## Releasing to PyPi

**TODO**

