# xkcd-cli

The missing CLI for exploring [xkcd web-comic](https://xkcd.com/) from your terminal

![alt text](xkcd.png "Xkcd : A webcomic of romance, sarcasm, math, and language.")


### Installation / Quick Start

xkcd-cli is available as [pypi](https://pypi.org/project/xkci-cli/) package. 
Install using pip/pip3

`$ pip install xkci-cli==0.0.1`

### Commands

* `$ xkcd latest` - loads the latest comic in default image viewer.
* `$ xkcd random` - loads any random comic content from past.
* `$ xkcd fetch --index=0` - loads the comic at given index.

* `$ xkcd open --blag | --blog` - opens XKCD blog in default browser.
* `$ xkcd open --fora | --forums` - opens XKCD forums webpage in default browser.
* `$ xkcd open --store` - opens XKCD merchandise store in default browser.
* `$ xkcd open --about` - opens XKCD info webpage in default brwoser.

##### Usage flags

* `$ xkcd --help` - prints a help screen.
* `$ xkcd [COMMAND] --debug` - runs the commands in debug mode.
* `$ xkcd [COMMAND] --log-info` - prints the comic metadata in terminal.

### License

The MIT License (MIT)