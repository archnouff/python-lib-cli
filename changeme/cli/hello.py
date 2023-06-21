import click


@click.command()
@click.option('--name', '-n', type=str, default='world')
def main(name: str):
    print(f'Hello {name}!')


if __name__ == '__main__':
    main()
