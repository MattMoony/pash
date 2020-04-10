from pash.shell import Shell
from pash.command import Command, CascCommand
from typing import List
import os, sys

def ping(cmd: Command, args: List[str]) -> None:
    print('Pong!')

def clear(cmd: Command, args: List[str]) -> None:
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

def shargs(cmd: Command, args: List[str]) -> None:
    print(args)

def bye(cmd: Command, args: List[str]) -> None:
    sh.exit()

sh: Shell = Shell(prompt='> ', interrupt_end=True)
sh.add_cmd(Command('ping', callback=ping))
sh.add_cmd(CascCommand('a', cmds=[
    CascCommand('b', cmds=[
        Command('c', callback=ping), 
        Command('d', callback=clear)
    ]), 
    Command('c', callback=bye),
]))
sh.add_cmd(Command('clear', 'cls', callback=clear))
sh.add_cmd(Command('shargs', callback=shargs))
sh.add_cmd(Command('exit', 'quit', 'bye', callback=bye))

sh.prompt_until_exit()