import click
from .galactic_invaders import start_game


@click.command(help="Start the Galactic Invaders game.")
@click.option('--mode', type=click.Choice(['default', 'speed']), default='default', help='Game mode: "default" or "speed".')
@click.option('--enemies', type=int, default=50, help='Number of enemies to start with.')
def cli(mode, enemies):
    valid_modes = ['default', 'speed']
    if mode not in valid_modes:
        click.echo(
            "Wrong input for --mode option! You should enter either 'default' or 'speed'!")
        return
    if enemies < 50:
        click.echo("The number of enemies must be at least 50!")
        return
    else:
        start_game(mode, enemies)
