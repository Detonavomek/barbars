import click

from lib.bot import Bot


@click.command()
@click.option('--config', help='Path to configuration file')
def run(config):
    Bot(config).start()

if __name__ == '__main__':
    run()
