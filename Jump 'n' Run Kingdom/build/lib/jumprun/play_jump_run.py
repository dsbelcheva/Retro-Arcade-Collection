import click
from .jump_run import start_game

@click.command(help="Start the Jump 'n' Run Kingdom game.")
@click.option('--total-coin', type=int, default=100, help='Total number of coins to collect in the game.')
def cli(total_coin):
    if total_coin<100:
        click.echo("The total number of coins should be greater or equal to 100!")
        return
    else:
        start_game(total_coin)