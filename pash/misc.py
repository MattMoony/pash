"""Miscellaneous functions for using pash"""

import shutil, random, sys, os
from typing import List
from enum import Enum
import colorama as cr
cr.init()

def center(txt: str) -> str:
    """Centers text appropriate for the current terminal width."""
    w = shutil.get_terminal_size().columns
    mx = max([len(l) for l in txt.split('\n')])
    return '\n'.join([' '*((w-mx)//2)+l for l in txt.split('\n')])

def print_center(txt: str) -> None:
    """Prints the centered text obtained from `center()`"""
    print(center(txt))

def printc(txt: str) -> None:
    """Alias for `print_center(txt)`"""
    print_center(txt)

def fancy_print(txt: str) -> None:
    """Prints the given text in a "fancy" way; it centers it, and gives it random splashes of colour."""
    txt = center(txt)
    col = [ cr.Fore.LIGHTRED_EX, cr.Fore.LIGHTGREEN_EX, cr.Fore.LIGHTBLUE_EX, cr.Fore.LIGHTBLACK_EX, cr.Fore.LIGHTYELLOW_EX, cr.Fore.LIGHTWHITE_EX, cr.Fore.LIGHTCYAN_EX, cr.Fore.LIGHTMAGENTA_EX, ]
    fin = ''
    while txt:
        fin += col[random.randint(0,len(col)-1)]
        r = min(random.randint(1,8), len(txt))
        fin += txt[:r]
        txt = txt[r:]
    print(fin+cr.Fore.RESET)

def fprint(txt: str) -> None:
    """Alias for `fancy_print(txt)`"""
    fancy_print(txt)

def clear() -> None:
    """Clears the console appropriate to the OS in use."""
    if sys.platform == 'win32':
        os.system('cls')
        return
    os.system('clear')

"""The possible table alignments (left, right)."""
TALIGN: Enum = Enum('TALIGN', 'LEFT RIGHT')

def print_table(tab: List[List[str]], align: TALIGN = TALIGN.RIGHT) -> None:
    """Prints the given 2d-string list in a table fashion; evenly spaced columns, etc."""
    w = shutil.get_terminal_size().columns
    ms = [max(c)+1 for c in zip(*[[len(x) for x in r] for r in tab])]
    for r in tab:
        print(' '+' '.join([('{:'+('>' if align == TALIGN.RIGHT else '')+str(ms[i])+'s}').format(c) for i, c in enumerate(r)]))