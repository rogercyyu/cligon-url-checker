# C.L.I.G.O.N

## Introduction

C.L.I.G.O.N or Cligon is an acronym that stands for Check if Link Is Good Or Not.
It is designed to check all website links inside a file. This program was written in Python 3.8.2.
It will return a list of good, bad, or unknown URL statuses.
- good urls are status code 200.
- bad urls are status codes 400 or 404.
- unknowns are status codes that aren't bad or good.

## Usage
To use please create a virtual environment. 
Please see [here](https://docs.python.org/3/tutorial/venv.html) or [CONTRIBUTING.md](https://github.com/rogercyyu/cligon-url-checker/blob/master/CONTRIBUTING.md) on how to set up a virtual env.

Once in your environment, please run:
```bash
pip install cligon
```
to install the program in your env. Once installed you can...

test URLs of a file:
```bash
cligon [file name with URL links]
```
get a list of usage options:
```bash
cligon
```
see the help page:
```bash
cligon -h
```

## Contributing
Please check out my repo found [here](https://github.com/rogercyyu/cligon-url-checker) and look at [CONTRIBUTING.md](https://github.com/rogercyyu/cligon-url-checker/blob/master/CONTRIBUTING.md).

## Features
- Colorized output: good = green, red = back, grey/white = unknown
- Version number argument
- Parallelism / Multi-threading (It's fast-ish)
- Grabs HEAD only
- URL timeout (default 2.5 milliseconds)
- Output JSON format
- Output only good or bad urls

## License

MIT
