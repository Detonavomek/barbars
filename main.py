import click

from lib.manager import BotManager


@click.command()
@click.option('--config', help='Path to configuration file')
def run(config):
    BotManager(config).start()

if __name__ == '__main__':
    run()
