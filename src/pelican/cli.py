import click

@click.command()
@click.argument('name')
def hello(name):
   click.echo(f'Hello {name}!')

@click.command()
@click.argument('fish_type')
def catch_fish(fish_type):
    click.echo(f"I've got a {fish_type}!")
