from __future__ import annotations
from pash.base import Keyword
from typing import Union, List, Callable, Any, Tuple, Dict, Optional

def _def_callback(cmd: Command, args: List[str]) -> None:
    pass

class Command(Keyword):
    def __init__(self, cmd: str, *args, callback: Callable[..., None] = _def_callback, 
                 cbargs: Union[Tuple[()], Tuple[Any]] = (), cbkwargs: Dict[str, Any] = dict(), **kwargs) -> None:
        super().__init__(cmd, *args, **kwargs)
        self.callback: Callable[..., None] = callback
        self.cbargs: Union[Tuple[()], Tuple[Any]] = cbargs
        self.cbkwargs: Dict[str, Any] = cbkwargs

    def __call__(self, args: Union[str, List[str]]) -> None:
        self.callback(self, args if isinstance(args, list) else args.split(), *self.cbargs, **self.cbkwargs)

def _def_unkown_key(cc: CascCommand, cmdline: str) -> None:
    print('Usage: %s' % cc.usage())

class CascCommand(Keyword):
    def __init__(self, cmd: str, *args, cmds: List[Keyword] = [], unknown_key: Callable[[CascCommand, str], None] = _def_unkown_key, **kwargs) -> None:
        super().__init__(cmd, *args, **kwargs)
        self._cmds: List[Keyword] = cmds
        self.unknown_key = unknown_key
        for c in self._cmds:
            c.parent = self

    def parse(self, cmdline: str) -> None:
        if not cmdline.strip():
            self.unknown_key(self, cmdline)
            return
        c: List[Keyword] = list(filter(lambda c: c.matches(cmdline), self._cmds))
        if not c:
            self.unknown_key(self, cmdline)
            return
        if isinstance(c[0], Command):
            c[0](cmdline.split()[1:])
            return
        c[0].parse(' '.join(cmdline.split()[1:]))

    def add_cmd(self, cmd: Keyword) -> None:
        cmd.parent = self
        self._cmds.append(cmd)

    def usage(self) -> str:
        t: str = self.trace()
        return '{} [{}]'.format(t, '|'.join([c.usage().replace(t+' ', '') for c in self._cmds]))