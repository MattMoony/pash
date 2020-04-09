import shutil, random
import colorama as cr
cr.init()

def center(txt: str) -> str:
    w = shutil.get_terminal_size().columns
    mx = max([len(l) for l in txt.split('\n')])
    return '\n'.join([' '*((w-mx)//2)+l for l in txt.split('\n')])

def print_center(txt: str) -> None:
    print(center(txt))

def printc(txt: str) -> None:
    """
        Alias for `print_center(txt)`
    """
    print_center(txt)

def fancy_print(txt: str) -> None:
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
    """
        Alias for `fancy_print(txt)`
    """
    fancy_print(txt)