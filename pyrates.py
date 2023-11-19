import requests
import click

def list_rates(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    key = "https://open.er-api.com/v6/latest/"
    first = 'EUR'
    data = requests.get(key+first)
    data = data.json()
    rates_raw = data['rates']
    rates = []

    for x in rates_raw:
        rates.append(x[:4])

    cols = 5
    length = len(rates)
    rows = int(length/cols)

    for i in range(rows):
        sublist = rates[i*cols : i*cols + cols]
        click.echo(*sublist) 
    ctx.exit()

@click.command()
@click.option('-l', is_flag=True, callback=list_rates, expose_value=False, is_eager=True)
@click.argument('amount', nargs=1, type=click.FLOAT)
@click.argument('first', nargs=1, type=click.STRING)
@click.argument('second', nargs=1, type=click.STRING)

def main(amount, first, second):
    key = "https://open.er-api.com/v6/latest/"
    data = requests.get(key+first)
    data = data.json()
    rates = data['rates']
    pair_price = float(data['rates'][second])
    conversion = float(amount) * pair_price
    click.echo(f'{amount:.2f} {first} is {conversion:.2f} {second}.')
    
if __name__ == '__main__':
    main()

