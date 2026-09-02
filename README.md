# finger2gemtext - A simple library for converting finger output to Gemtext

## Introduction

`finger2gemtext` is a small and simple library that provides code for
converting `finger` responses into [the hypertext markup language of the
Gemini project](https://geminiprotocol.net/docs/gemtext-specification.gmi).

## Installation

`finger2gemtext` is [available from
pypi](https://pypi.org/project/finger2gemtext/) and can be installed with your
package installer of choice.

With `pip`:

```shell
pip install finger2gemtext
```

With `uv`:

```shell
uv add finger2gemtext
```

## Quick start

The library provides a single main conversion function called
`finger_to_gemtext`. It is passed a string that is the finger response you
wish to convert, and the result is a string that is the resulting Gemtext.

A very minimal converter might look like:

```python
import fileinput
from .convert import finger_to_gemtext

def convert() -> None:
    """Parse the input from stdin or files and print the parsed Gemtext."""
    with fileinput.input() as finger_content:
        print(finger_to_gemtext("".join(finger_content)))
```

While it is primarily intended as a library to be used from other Python
code, it does contain a simple test command line tool, which can be accessed
either via the Python `-m` switch, or depending on your environment, via the
`finger2gemtext` command. For example, if you were to run this command:

```sh
finger @typed-hole.org | finger2gemtext
```

you'd get output like this:

```gemtext
[typed-hole.org]

Welcome to the Typed Hole
Uptime:  14:10:28 up 248 days, 22:12,  0 user,  load average: 0.44, 0.34, 0.44
Users currently logged in: probably julien

Available fingers:

=> /finger/username username:           get user infos
=> /finger/feed feed:                   get my latest toots
=> /finger/lobsters lobsters:           get lobste.rs hottest stories
=> /finger/weather weather:             get typed-hole.org current weather
=> /finger/temp temp:                   get typed-hole.org current CPU temperature
=> /finger/cyoa cyoa:                   finger your own adventure
=> /finger/textfile textfile:           read a random textfile from textfiles.com
=> /finger/smog smog:                   read SMOG e-zine issues
```

See [the main documentation](https://finger2gemtext.davep.dev/) for the full API.

[//]: # (README.md ends here)
