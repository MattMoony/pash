from __future__ import annotations
from pash.base import Keyword
from pash.command import Command, CascCommand
from typing import List, Callable

def _def_unknown_cmd(sh: Shell, cmdline: str) -> None:
    print('Unknown command "%s" ... ' % cmdline.split()[0])

class Shell(CascCommand):
    def __init__(self, *args, prompt: str = '$ ', interrupt_end: bool = False, 
                 unknown_cmd: Callable[[Shell, str], None] = _def_unknown_cmd,
                 **kwargs) -> None:
        super().__init__('', *args, unknown_key=unknown_cmd, **kwargs)
        self.__interrupt_end: bool = interrupt_end
        self.__exited: bool = False
        self.prompt: str = prompt

    def exit(self) -> None:
        self.__exited = True

    def add_cmd(self, cmd: Keyword) -> None:
        self._cmds.append(cmd)

    def prompt_until_exit(self) -> None:
        self.__exited = False
        while not self.__exited:
            try:
                print(self.prompt, end='')
                cmdline: str = input()
                self.parse(cmdline)
            except KeyboardInterrupt:
                print()
                if self.__interrupt_end:
                    self.__exited = True
                    break