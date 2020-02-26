import click
import json
import requests
import logging
import webbrowser
from PIL import Image
from io import BytesIO
from random import randint

try:
    from src import logger
except ImportError as error:
    import logger

logger = logger.setup()


@click.group()
@click.option('--debug', is_flag=True)
def cli(debug):
    if debug:
        logger.setLevel(logging.INFO)


@cli.command()
@click.option('--log-info', is_flag=True, help='Prints the webcomic metadata.')
def random(log_info):
    """
    @command : xkcd random
    @usage   : opens any random web-comic content in default imageviewer
    """
    try:
        latest_index = get_latest_feed_index()
        rand_index = randint(1, latest_index)
        response = requests.get('https://xkcd.com/{}/info.0.json'.format(rand_index)).json()
        res = requests.get(response["img"])
        img = Image.open(BytesIO(res.content))
        img.show()

        if log_info:
            logger.info(json.dumps(response))
    except requests.ConnectionError as error:
        logger.exception(error)


@cli.command()
@click.option('--log-info', is_flag=True, help='Prints the webcomic metadata.')
def latest(log_info):
    """
    @command : xkcd latest
    @usage   : opens latest web-comic content in default imageviewer
    """
    try:
        response = requests.get('https://xkcd.com/info.0.json').json()
        res = requests.get(response["img"])
        img = Image.open(BytesIO(res.content))
        img.show()

        if log_info:
            logger.info(response)
    except requests.ConnectionError as error:
        logger.exception(error)


@cli.command()
@click.option('--log-info', is_flag=True, help='Prints the webcomic metadata.')
@click.option('--index', default=1, help='Number/Index of web comic.')
def fetch(log_info, index):
    """
    @command : xkcd fetch --index=10
    @usage   : opens the web-comic content at given index in default imageviewer
    """
    try:
        endpoint = 'https://xkcd.com/{}/info.0.json'.format(index)
        with requests.Session() as session:
            content = session.get(endpoint).content.decode()
            response = json.loads(content)
            res = session.get(response["img"])
            img = Image.open(BytesIO(res.content))
            img.show()

            if log_info:
                logger.info(response)
    except requests.ConnectionError as error:
        logger.exception(error)

@cli.command()
@click.option('--blog', is_flag=True, help='Opens XKCD blog in default browser.')
@click.option('--blag', is_flag=True, help='Opens XKCD blog in default browser.')
@click.option('--fora', is_flag=True, help='Opens XKCD forums webpage in default browser.')
@click.option('--forums', is_flag=True, help='Opens XKCD forums webpage in default browser.')
@click.option('--store', is_flag=True, help='Opens XKCD merchandise store in default browser.')
@click.option('--about', is_flag=True, help='Opens XKCD info webpage in default brwoser.')
def open(blog, blag, fora, forums, store, about):
    if blog or blag:
        logger.info('Opening XKCD blog in default browser')
        webbrowser.open_new_tab('https://blog.xkcd.com/')
    elif fora or forums:
        logger.info('Opening XKCD forums in default browser')
        webbrowser.open_new_tab('https://forums.xkcd.com/')
    elif store:
        logger.info('Opening XKCD merchandise in default browser')
        webbrowser.open_new_tab('https://store.xkcd.com/')
    elif about:
        logger.info('Opening XKCD abouts webpage in default browser')
        webbrowser.open_new_tab('https://xkcd.com/about/')
    else:
        logger.warn('''Content flag required. Please use appropriate flag(s) in command.
        Use --help for command usage''')
        pass


def get_latest_feed_index():
    r = requests.get('https://xkcd.com/info.0.json').json()
    return r['num']


if __name__ == '__main__':
    cli()