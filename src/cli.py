import click
import json
import requests
from PIL import Image
from io import BytesIO
from random import randint

@click.group()
@click.option('--debug', is_flag=True)
def cli(debug):
    pass

def get_latest_feed_index():
    r = requests.get('https://xkcd.com/info.0.json').json()
    return r['num']

@cli.command()
@click.option('--log-info', is_flag=True)
def random(log_info):
    try:
        latest_index = get_latest_feed_index()
        rand_index = randint(1, latest_index)
        response = requests.get('https://xkcd.com/{}/info.0.json'.format(rand_index)).json()
        res = requests.get(response["img"])
        img = Image.open(BytesIO(res.content))
        img.show()

        if log_info:
            print(response)
    except requests.ConnectionError:
        pass
    

@cli.command()
@click.option('--log-info', is_flag=True)
def latest(log_info):
    try:
        response = requests.get('https://xkcd.com/info.0.json').json()
        res = requests.get(response["img"])
        img = Image.open(BytesIO(res.content))
        img.show()

        if log_info:
            print(response)
    except requests.ConnectionError:
        pass
    

@cli.command()
@click.option('--log-info', is_flag=True, )
@click.option('--index', default=1, help='Number/Index of web comic.')
def fetch(log_info, index):
    try:
        endpoint = 'https://xkcd.com/{}/info.0.json'.format(index)
        with requests.Session() as session:
            content = session.get(endpoint).content.decode()
            response = json.loads(content)
            res = session.get(response["img"])
            img = Image.open(BytesIO(res.content))
            img.show()

            if log_info:
                print(response)
    except requests.ConnectionError:
        pass
    

if __name__ == '__main__':
    cli()