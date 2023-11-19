import requests
import click

@click.command()
@click.argument('amount', nargs=1, type=click.FLOAT)
@click.argument('first', nargs=1, type=click.STRING)
@click.argument('second', nargs=1, type=click.STRING)

def main(amount, first, second):
    try:
        key = "https://open.er-api.com/v6/latest/"
        data = requests.get(key+first)
        data = data.json()
        pair_price = float(data['rates'][second])
        conversion = float(amount) * pair_price
        click.echo(f'{amount:.2f} {first} is {conversion:.2f} {second}.')
    except KeyError:
        click.echo("Can't exchange that currency. Please try again.")
    
if __name__ == '__main__':
    main()

