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

def pow_num(cmd: Command, args: List[str], n: int) -> None:
    print(n**2)

def echo(cmd: Command, args: List[str], params: List[str]) -> None:
    if not params:
        return
    print(params[0])

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
e = Command('echo', callback=echo)
e.add_arg('params', type=str, nargs='*')
sh.add_cmd(e)
test = Command('pow', callback=pow_num)
test.add_arg('-n', dest='n', type=int, help='Number ... ', required=True)
sh.add_cmd(test)

sh.prompt_until_exit()