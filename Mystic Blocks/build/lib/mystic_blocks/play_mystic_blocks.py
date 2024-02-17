import click
from mystic_blocks import start_game

@click.command(help="Start the Mystic Blocks game.")
@click.option('--mode', type=click.Choice(['default', 'speed']), default='default', help='Game mode: "default" or "speed".')
def cli(mode):
    valid_modes = ['default', 'speed']
    if mode not in valid_modes:
        click.echo("Wrong input for --mode option! You should enter either 'default' or 'speed'!")
        return
    else:
        start_game(mode)