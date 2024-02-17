import click
from .epic_race import *

@click.command(help="Start the Epic Race game.")
@click.option('--number_of_cars', type=int, default=10, help='Total number of cars to play agains in the game.')
def cli(number_of_cars):
    if number_of_cars<10:
        click.echo("The total number of coins should be greater or equal to 10!")
        return
    else:
        game = Game(number_of_cars)
        game.run()