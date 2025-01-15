"""Command to display the current RoyalFlush version."""

import click

import royalflush


@click.command(name="version")
@click.pass_context
def version_cmd(_: click.Context) -> None:
    """
    Show the current version of RoyalFlush.

    Usage:
        royalflush version

    Args:
        ctx (click.Context): The Click context object.
    """
    click.echo(f"Royal FLush version: {royalflush.__version__}")
