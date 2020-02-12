import click
import requests
from PIL import Image
from io import BytesIO
from random import randint

@click.group()
def cli():
    pass

def get_latest_feed_index():
    r = requests.get('https://xkcd.com/info.0.json').json()
    return r['num']

@click.command()
def random():
    latest_index = get_latest_feed_index()
    rand_index = randint(1, latest_index)
    response = requests.get('https://xkcd.com/{}/info.0.json'.format(rand_index)).json()
    res = requests.get(response["img"])
    img = Image.open(BytesIO(res.content))
    img.show()

@click.command()
def latest():
    response = requests.get('https://xkcd.com/info.0.json').json()
    res = requests.get(response["img"])
    img = Image.open(BytesIO(res.content))
    img.show()

cli.add_command(latest)
cli.add_command(random)