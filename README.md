# pash

---

## About

Since many of my recent Python projects have included an interactive shell / command prompt of some sorts,
I've decided to write my own package for it, so that I won't have to think of a new way of handling commands everytime.

I hope it can be of some use to other Python programmers as well, as it'll hopefully make my life a lot easier.

## Usage

First, create a shell ...

```python
from pash.shell import Shell
sh = Shell(prompt='$ ')
```

... and then, simply add as many commands as you want/need!

```python
from pash.command import Command
sh.add_command(Command('ping', callback=pong))
...
```

You can even create _cascading commands_ ...

```python
from pash.command import CascCommand
sh.add_command(CascCommand('go', cmds=[
    Command('north', callback=gnorth),
    Command('south', callback=gsouth),
]))
...
```

---

... Matthias M. (April 2020)