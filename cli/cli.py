from pydoc import locate

import click

from app import interface



@click.group()
def cli():
    pass


@cli.group(name="model")
def model_run():
    pass




@model_run.command(
    name="serve",
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,
    ),
)
def serve(
):
    interface()


if __name__ == "__main__":
    cli()
