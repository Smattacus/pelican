import click

@click.command()
@click.argument('name')
def hello(name):
   click.echo(f'Hello {name}!')

def catch_fish(fish_type):
    print(f"I've got a {fish_type}!")