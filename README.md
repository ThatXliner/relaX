<p align="center"><a href="https://travis-ci.com/ThatXliner/relaX"><img src="https://travis-ci.com/ThatXliner/relaX.svg?branch=master" alt="Build Status"></a>
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>
  <img src="https://img.shields.io/github/languages/code-size/ThatXliner/relaX" alt="GitHub code size in bytes">
  <img alt="GitHub" src="https://img.shields.io/github/license/ThatXliner/relaX">
  <img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/relax-library">
  <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/relax-library">
  <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/relax-library">
  <img alt="GitHub issues" src="https://img.shields.io/github/issues/ThatXliner/relax">
</p>

---

[The relaX library](#the-relax-library) | [What is this](#what-is-this) | [Getting started](#getting-started) | [Installation](#installation) | [Usage](#usage) | [Contributing](#contributing) | [License (MIT)](#license-mit) | [FAQ](#faq)

---

# The relaX library

> _"A collection of usefulness..."_


NOTICE: relaX is still in its Alpha stage. Features and APIs may change drastically. You are welcome to contribute!

## What is this

The relaX library is a collection of useful functions, objects, and utilities for any python programmer. It is meant to **provide intuitive and easy-to-use functionality for all purposes**. Need a configuration file system that'll set itself up?

```python
import relaX.fig
```

is as easy as that.

RelaX was made so you could relax, instead of scratching your head.

### Why you should relax...

**NOTICE: This project is currently still in pre-alpha. Any contributions would be greatly appreciated. You can learn more about how to contribute [here](#contributing).**

You should be reassured that this program should work on _most_ computers. This is compatible with:

> - CPython versions **3.5 to 3.10** (In the future, this will change from 3.6)
> - PyPy3 compatible
> - MacOS python3.7 for _Xcode versions_ **9.4** _to_ **11**, python3.8 for _Xcode version_ **12**
> - Ubuntu versions tested for support: **_14.04_**, **_16.04_**, **_18.04_**, **_20.04_**

All of the above is certified via [Travis-CI](https://travis-ci.com/). Our build status (<sub>[![Build Status](https://travis-ci.com/ThatXliner/relaX.svg?branch=master)](https://travis-ci.com/ThatXliner/relaX)</sub>) is the result of running `pytest` over the `tests` directory in our [repo](https://github.com/ThatXliner/relaX) over a variety of python versions and OSes.

## Getting started

Hooked? Here's some tips to get you started.

### Installation

You can install this package from source via git.

But the recommended way to install this is to use `pip install relaX-library` (or `python3 -m pip install relaX-library`).

#### via `git clone`

You can clone this repository, run `cd relaX`, and then run `pip install .` (or `python3 -m pip install .`).

Here's the complete installation script:

```bash
/usr/bin/git clone https://github.com/ThatXliner/relaX.git
/bin/bash cd relaX
/usr/bin/pip3 install .
/usr/bin/python3 -m pip install .
```

or, a one-liner installation script:

```bash
/usr/bin/git clone https://github.com/ThatXliner/relaX.git && /bin/bash cd relaX && /usr/bin/pip3 install . ; /usr/bin/python3 -m pip install .
```

NOTE: If you don't have `pip` or `/usr/bin/pip` or `/usr/bin/pip3` and have tried `/usr/bin/python3 -m pip`, you will need to install pip manually. Execute the following command in your terminal (shell):

```bash
{/usr/bin/curl https://bootstrap.pypa.io/get-pip.py | /usr/bin/python3} || {wget https://bootstrap.pypa.io/get-pip.py | /usr/bin/python3} ||  {/usr/bin/curl https://bootstrap.pypa.io/get-pip.py | /usr/bin/python} ||  {wget https://bootstrap.pypa.io/get-pip.py | /usr/bin/python}
```

### via `pip install` (recommended)

You can easily install this package via `pip install relaX-library` (or `python3 -m pip install relaX-library`).

### Usage

#### relaX.fig

#### relaX.time

## Contributing

### Code style: black

We don't need to chatter about the code style: use black and try to **keep it 90 or under characters per line**. Keep that in mind. Comment writing guides, naming guidelines, and docstring conventions are WIP.


But try to stick with `snake_case`.

## License (MIT)

MIT license.

I, Bryan, feel that everyone should be able to use technology and code, not needing to worry about anything else.

**We ❤️ open-source**

```text
MIT License

Copyright (c) 2020 ThatXliner (Bryan Hu)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## FAQ

### Getting pip

### Available platforms
